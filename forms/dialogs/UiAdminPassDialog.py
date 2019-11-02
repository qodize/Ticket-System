# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms\ui files\UiAdminPassDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminPassDialog(object):
    def setupUi(self, AdminPassDialog):
        AdminPassDialog.setObjectName("AdminPassDialog")
        AdminPassDialog.resize(401, 162)
        self.buttonBox = QtWidgets.QDialogButtonBox(AdminPassDialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 120, 351, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.password_line = QtWidgets.QLineEdit(AdminPassDialog)
        self.password_line.setGeometry(QtCore.QRect(20, 80, 361, 31))
        self.password_line.setObjectName("password_line")
        self.header_lb = QtWidgets.QLabel(AdminPassDialog)
        self.header_lb.setGeometry(QtCore.QRect(70, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.header_lb.setFont(font)
        self.header_lb.setObjectName("header_lb")
        self.message_lb = QtWidgets.QLabel(AdminPassDialog)
        self.message_lb.setGeometry(QtCore.QRect(140, 50, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.message_lb.setFont(font)
        self.message_lb.setObjectName("message_lb")

        self.retranslateUi(AdminPassDialog)
        #  self.buttonBox.accepted.connect(AdminPassDialog.accept)
        self.buttonBox.rejected.connect(AdminPassDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AdminPassDialog)

    def retranslateUi(self, AdminPassDialog):
        _translate = QtCore.QCoreApplication.translate
        AdminPassDialog.setWindowTitle(_translate("AdminPassDialog", "Dialog"))
        self.header_lb.setText(_translate("AdminPassDialog", "Пароль Администратора"))
        self.message_lb.setText(_translate("AdminPassDialog", "Введите пароль"))
