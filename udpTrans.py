from socket import *
import client_ui
import threading
import stopThreading
import datetime
import requests
import time


class UdpTrans(client_ui.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.address = '127.0.0.1'
        self.port = 6910
        self.udpSocket = socket(AF_INET, SOCK_DGRAM)
        self.serverThread = None
        self.remoteAddr = None
        self.__running = True

    def udp_server_start(self):
        self.serverThread = threading.Thread(target=self.udp_server_concurrency)
        self.serverThread.setDaemon(True)
        self.serverThread.start()
        msg = 'UDP服务器正在监听{}端口'.format(self.port)
        self.signalStatusAreaTip.emit(msg)

    def udp_server_concurrency(self):
        try:
            self.udpSocket.bind((self.address, self.port))
        #     while self.__login.isSet():
        #         self.udpSocket.sendto('login'.encode('utf-8'), (self.address, self.port))
        except Exception:
            msg = '请检查natapp是否开启,如果开启查看端口是否被占用'
            self.signalMsgBoxPrompt.emit(msg)

        while self.__running:
            print("123")
            time.sleep(1)
        # while self.__running.is_set():
        #     print("1")
        #     recvMsg, self.remoteAddr = self.udpSocket.recvfrom(1024, 10)
        #     recvMsg = 'http://' + recvMsg.decode()
        #     print(recvMsg)
        #     msg = '来自IP:{}端口:{}:\n{}\n'.format(self.remoteAddr[0], self.remoteAddr[1], recvMsg)
        #     self.signalMsgTip.emit(msg)
        #     self.udp_send_common()
        #     self.udp_send_used()
        #     self.udp_download(recvMsg)
        #     self.udp_send_unused()

    def udp_download(self, url):
        r = requests.get(url)
        img = r.content
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        imgName = nowTime + '.bmp'
        with open('./img/{}'.format(imgName), 'wb') as f:
            f.write(img)
        f.close()
        return './img/' + imgName

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

    def udp_send_unused(self):
        """
        提示用户和服务器机器未被占用
        :return:
        """
        self.udpSocket.sendto('0'.encode('utf-8'), self.remoteAddr)

    def udp_close(self):
        """
        udp服务器下线
        :return:
        """
        # msg = '正在断开连接'
        # self.signalStatusAreaTip.emit(msg)
        self.udpSocket.close()
        print(self.__running)
        self.__running = False  # stop thread
        print(self.__running)

        stopThreading.stop_thread(self.serverThread)

if __name__ == '__main__':
    insUdpTrans = UdpTrans()
    insUdpTrans.udp_server_start()
