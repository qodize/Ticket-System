# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms\ui files\UiOwnerPassDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OwnerPassDialog(object):
    def setupUi(self, OwnerPassDialog):
        OwnerPassDialog.setObjectName("OwnerPassDialog")
        OwnerPassDialog.resize(400, 170)
        self.buttonBox = QtWidgets.QDialogButtonBox(OwnerPassDialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 120, 351, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.password_line = QtWidgets.QLineEdit(OwnerPassDialog)
        self.password_line.setGeometry(QtCore.QRect(20, 80, 361, 31))
        self.password_line.setObjectName("password_line")
        self.message_lb = QtWidgets.QLabel(OwnerPassDialog)
        self.message_lb.setGeometry(QtCore.QRect(140, 50, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.message_lb.setFont(font)
        self.message_lb.setObjectName("message_lb")
        self.header_lb = QtWidgets.QLabel(OwnerPassDialog)
        self.header_lb.setGeometry(QtCore.QRect(110, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.header_lb.setFont(font)
        self.header_lb.setObjectName("header_lb")

        self.retranslateUi(OwnerPassDialog)
        # self.buttonBox.accepted.connect(OwnerPassDialog.accept)
        self.buttonBox.rejected.connect(OwnerPassDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OwnerPassDialog)

    def retranslateUi(self, OwnerPassDialog):
        _translate = QtCore.QCoreApplication.translate
        OwnerPassDialog.setWindowTitle(_translate("OwnerPassDialog", "Dialog"))
        self.message_lb.setText(_translate("OwnerPassDialog", "Введите пароль"))
        self.header_lb.setText(_translate("OwnerPassDialog", "Пароль Владельца"))
