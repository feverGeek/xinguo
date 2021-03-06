# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import pyqtSignal, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit, QPushButton
import udpTrans


class Ui_Dialog(QDialog):
    signalMsgBoxPrompt = pyqtSignal(str)
    signalMsgTip = pyqtSignal(str)
    signalStatusAreaTip = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 391)
        self.horizontalLayout_3 = QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_status = QLabel(Dialog)
        self.label_status.setStyleSheet("font: 75 20pt \"Bitstream Charter\";\n"
"text-decoration: underline;")
        self.label_status.setObjectName("label_status")
        self.verticalLayout_2.addWidget(self.label_status)
        self.textEditStatus = QTextEdit(Dialog)
        self.textEditStatus.setObjectName("textEditStatus")
        self.verticalLayout_2.addWidget(self.textEditStatus)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_recv = QPushButton()
        self.pushButton_recv.setObjectName("pushButton_recv")
        self.label_author = QLabel(Dialog)
        self.label_author.setObjectName("label_author")
        self.horizontalLayout_2.addWidget(self.label_author)
        self.horizontalLayout_2.addWidget(self.pushButton_recv)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_recv = QLabel(Dialog)
        self.label_recv.setStyleSheet("font: 75 20pt \"Bitstream Charter\";\n"
"text-decoration: underline;")
        self.label_recv.setObjectName("label_recv")
        self.horizontalLayout.addWidget(self.label_recv)
        self.pushButton_clear = QPushButton(Dialog)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEditRecv = QTextEdit(Dialog)
        self.textEditRecv.setObjectName("textEditRecv")
        self.verticalLayout.addWidget(self.textEditRecv)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "client"))
        self.label_status.setText(_translate("Dialog", "状态区"))
        self.label_author.setText(_translate("Dialog", "Written by xinguo \n"
"     Zeta"))
        self.label_recv.setText(_translate("Dialog", "接收区"))
        self.pushButton_clear.setText(_translate("Dialog", "清除消息"))
        self.pushButton_recv.setText(_translate("Dialog", "打开接收"))

    def slot_status_area_tip(self, msg):
        """
        状态区显示信息
        :param msg:
        :return:
        """
        self.textEditStatus.append(msg)

    def slot_recv_area_tip(self, msg):
        """
        接收区显示信息
        :param msg:
        :return:
        """
        self.textEditRecv.append(msg)

    def slot_msg_box_prompt(self, msg):
        """
        message box 弹窗
        :param msg:
        :return:
        """
        QMessageBox.question(self, 'Message', msg, QMessageBox.Yes | QMessageBox.No)

    def slot_clear_recv(self):
        """
        清除接收区
        :return:
        """
        self.textEditRecv.clear()

    def slot_recv(self):
        """
        打开接收
        :return:
        """
        udpTrans.used_flag = True
        print(udpTrans.used_flag)
        self.pushButton_recv.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

