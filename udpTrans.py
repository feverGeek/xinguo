from socket import socket, AF_INET, SOCK_DGRAM
import client_ui
from threading import Thread
from datetime import datetime
from requests import get
from subprocess import Popen, PIPE
import re
from sys import platform

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
            if platform == 'win32':
                # p = Popen(['Ping -n 1 www.baidu.com'], stdout=PIPE,stderr=PIPE, shell=True)
                # out = p.stdout.read().decode()
                # regex = re.compile('已接收 = 1')
                # if regex.findall(out)[0] == '已接收 = 1':
                #     return True
                # else:
                #     return False
                # 暂时留坑
                return True
            elif platform == 'linux':
                p = Popen(['ping -c 1 -W 1 www.baidu.com'], stdout=PIPE,stderr=PIPE,shell=True)
                out = p.stdout.read().decode()
                regex = re.compile('1 received')
                if regex.findall(out)[0] == '1 received':
                    return True
                else:
                    return False
        except Exception:
            return False

    def udp_server_start(self):
        self.serverThread = Thread(target=self.udp_server_concurrency)
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
            recvMsg, self.remoteAddr = self.udpSocket.recvfrom(1024)
            if used_flag:
                print("recv open")
                recvMsg = 'http://' + recvMsg.decode()
                print(recvMsg)
                time_now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                msg = '{}\n来自IP:{}端口:{}:\n{}\n'.format(time_now,
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
                        print("download")
                        msg = time_now + '\n图片成功接收\n'
                        self.signalStatusAreaTip.emit(msg)
                        recvMsg = ''
                    else:
                        msg = time_now + '\n下载失败\n'
                        self.signalMsgBoxPrompt.emit(msg)
                        self.signalStatusAreaTip.emit(msg)
                    self.udp_send_unused()
                except Exception:
                    msg = '下载失败'
                    self.signalMsgBoxPrompt.emit(msg)

            else:
                self.udp_send_used()

    def udp_download(self, url):
        """
        图片下载
        :param url: 图片链接
        :return: 成功返回图片路径
                 失败返回None
        """
        try:
            r = get(url)
            if r.status_code != 200:
                return None
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
    # insUdpTrans.udp_server_start()
    insUdpTrans.udp_download("http://img.hcfyww.net/1554639887611.bmp")
