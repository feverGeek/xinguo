# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 391)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_status = QtWidgets.QLabel(Dialog)
        self.label_status.setStyleSheet("font: 75 20pt \"Bitstream Charter\";\n"
"text-decoration: underline;")
        self.label_status.setObjectName("label_status")
        self.verticalLayout_2.addWidget(self.label_status)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_author = QtWidgets.QLabel(Dialog)
        self.label_author.setObjectName("label_author")
        self.horizontalLayout_2.addWidget(self.label_author)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_login = QtWidgets.QPushButton(Dialog)
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout_3.addWidget(self.pushButton_login)
        self.pushButton_exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.verticalLayout_3.addWidget(self.pushButton_exit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_recv = QtWidgets.QLabel(Dialog)
        self.label_recv.setStyleSheet("font: 75 20pt \"Bitstream Charter\";\n"
"text-decoration: underline;")
        self.label_recv.setObjectName("label_recv")
        self.horizontalLayout.addWidget(self.label_recv)
        self.pushButton_clear = QtWidgets.QPushButton(Dialog)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "client"))
        self.label_status.setText(_translate("Dialog", "状态区"))
        self.label_author.setText(_translate("Dialog", "Written by xinguo \n"
"     Zeta"))
        self.pushButton_login.setText(_translate("Dialog", "上线"))
        self.pushButton_exit.setText(_translate("Dialog", "退出"))
        self.label_recv.setText(_translate("Dialog", "接收区"))
        self.pushButton_clear.setText(_translate("Dialog", "清除消息"))

