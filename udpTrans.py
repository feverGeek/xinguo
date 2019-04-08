from socket import *
import client_ui
import threading
import datetime
import requests
import subprocess
import re

used_flag = True


class UdpTrans(client_ui.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.address = '127.0.0.1'
        self.port = 6910
        self.udpSocket = socket(AF_INET, SOCK_DGRAM)
        self.serverThread = None
        self.remoteAddr = None

    def network_check(self):
        """
        网络检查
        :return:
        """
        try:
            p = subprocess.Popen(['ping -c 1 -W 1 www.baidu.com'], stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            out = p.stdout.read().decode()
            regex = re.compile('1 received')
            if regex.findall(out)[0] == '1 received':
                return True
            else:
                return False
        except Exception:
            return False

    def udp_server_start(self):
        self.serverThread = threading.Thread(target=self.udp_server_concurrency)
        self.serverThread.setDaemon(True)
        self.serverThread.start()
        msg = 'UDP服务器正在监听{}端口'.format(self.port)
        self.signalStatusAreaTip.emit(msg)

    def udp_server_concurrency(self):
        recvMsg = ''
        try:
            self.udpSocket.bind((self.address, self.port))
        except Exception:
            msg = '请检查natapp是否开启,如果开启查看端口是否被占用'
            self.signalMsgBoxPrompt.emit(msg)

        while True:
            if used_flag:
                print("recv open")
                recvMsg, self.remoteAddr = self.udpSocket.recvfrom(1024)
                recvMsg = 'http://' + recvMsg.decode()
                print(recvMsg)
                msg = '{}\n来自IP:{}端口:{}:\n{}\n'.format(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
                                                       self.remoteAddr[0],
                                                       self.remoteAddr[1],
                                                       recvMsg)
                self.udp_send_used()
                self.udp_set_used()
                self.pushButton_recv.setEnabled(False)
                with open('./log/log', 'a+') as f:
                    f.write(msg+'\n')
                f.close()
                self.signalMsgTip.emit(msg)
                self.udp_send_common()
                try:
                    if self.udp_download(recvMsg):
                        msg = '图片成功接收'
                        self.signalStatusAreaTip.emit(msg)
                        recvMsg = ''
                    self.udp_send_unused()
                except Exception:
                    msg = '下载失败'
                    self.signalMsgBoxPrompt.emit(msg)
            else:
                recvMsg, self.remoteAddr = self.udpSocket.recvfrom(1024)
                self.udp_send_used()

    def udp_download(self, url):
        """
        图片下载
        :param url: 图片链接
        :return: 成功返回图片路径
                 失败返回None
        """
        try:
            r = requests.get(url)
            img = r.content
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            imgName = nowTime + '.bmp'
            with open('./img/{}'.format(imgName), 'wb') as f:
                f.write(img)
            f.close()
            return './img/' + imgName
        except Exception:
            return None

    def udp_send_common(self):
        """
        提示用户和服务器消息正常接收
        :return:
        """
        self.udpSocket.sendto('0'.encode('utf-8'), self.remoteAddr)

    def udp_send_used(self):
        """
        提示用户和服务器机器被占用
        :return:
        """
        self.udpSocket.sendto('2'.encode('utf-8'), self.remoteAddr)

    def udp_set_used(self):
        global used_flag
        used_flag = False

    def udp_send_unused(self):
        """
        提示用户和服务器机器未被占用
        :return:
        """
        self.udpSocket.sendto('0'.encode('utf-8'), self.remoteAddr)
        print("here")
        self.pushButton_recv.setEnabled(True)


if __name__ == '__main__':
    insUdpTrans = UdpTrans()
    insUdpTrans.udp_server_start()
