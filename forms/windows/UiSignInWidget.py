# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms\ui files\UiSignInWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView


class Ui_SignInWidget(object):
    def setupUi(self, SignInWidget):
        SignInWidget.setObjectName("SignInWidget")
        SignInWidget.resize(406, 432)
        self.theatresTable = QtWidgets.QTableWidget(SignInWidget)
        self.theatresTable.setGeometry(QtCore.QRect(20, 80, 221, 301))
        self.theatresTable.setLineWidth(1)
        self.theatresTable.setAlternatingRowColors(False)
        self.theatresTable.setRowCount(0)
        self.theatresTable.setColumnCount(2)
        self.theatresTable.setObjectName("theatresTable")
        self.theatresTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.theatresTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        item = QtWidgets.QTableWidgetItem()
        self.theatresTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.theatresTable.setHorizontalHeaderItem(1, item)
        self.del_btn = QtWidgets.QPushButton(SignInWidget)
        self.del_btn.setGeometry(QtCore.QRect(260, 330, 131, 51))
        self.del_btn.setObjectName("del_btn")
        self.sign_in_btn = QtWidgets.QPushButton(SignInWidget)
        self.sign_in_btn.setGeometry(QtCore.QRect(260, 190, 131, 51))
        self.sign_in_btn.setObjectName("sign_in_btn")
        self.add_btn = QtWidgets.QPushButton(SignInWidget)
        self.add_btn.setGeometry(QtCore.QRect(260, 260, 131, 51))
        self.add_btn.setObjectName("add_btn")
        self.message_lb = QtWidgets.QLabel(SignInWidget)
        self.message_lb.setGeometry(QtCore.QRect(110, 50, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.message_lb.setFont(font)
        self.message_lb.setObjectName("message_lb")
        self.header = QtWidgets.QLabel(SignInWidget)
        self.header.setGeometry(QtCore.QRect(100, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.header.setFont(font)
        self.header.setObjectName("header")

        self.retranslateUi(SignInWidget)
        QtCore.QMetaObject.connectSlotsByName(SignInWidget)

    def retranslateUi(self, SignInWidget):
        _translate = QtCore.QCoreApplication.translate
        SignInWidget.setWindowTitle(_translate("SignInWidget", "Вход"))
        item = self.theatresTable.horizontalHeaderItem(0)
        item.setText(_translate("SignInWidget", "Кинотеатр"))
        item = self.theatresTable.horizontalHeaderItem(1)
        item.setText(_translate("SignInWidget", "Город"))
        self.del_btn.setText(_translate("SignInWidget", "Удалить Кинотеатр"))
        self.sign_in_btn.setText(_translate("SignInWidget", "Войти"))
        self.add_btn.setText(_translate("SignInWidget", "Новый Кинотеатр"))
        self.message_lb.setText(_translate("SignInWidget", "Выберете Кинотеатр из списка"))
        self.header.setText(_translate("SignInWidget", "Вход в Учетную запись"))
