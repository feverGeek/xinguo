from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt
import sys
import udpTrans
import stopThreading


class MainWindow(udpTrans.UdpTrans):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.setupUi(self.window)
        self.window_connect()

    def window_show(self):
        self.window.show()

    def window_connect(self):
        self.signalMsgBoxPrompt.connect(self.slot_msg_box_prompt)
        self.signalMsgTip.connect(self.slot_recv_area_tip)
        self.pushButton_clear.clicked.connect(self.slot_clear_recv)
        # self.pushButton_exit.clicked.connect(QCoreApplication.quit)
        self.signalStatusAreaTip.connect(self.slot_status_area_tip)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            print("close")
            stopThreading.stop_thread(self.serverThread)
            QApplication.quit()
            self.udp_close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()
    mainwindow = MainWindow(dialog)
    mainwindow.window_show()
    mainwindow.udp_server_start()
    sys.exit(app.exec_())



