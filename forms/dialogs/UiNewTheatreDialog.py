# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms\ui files\UiNewCinemaDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewTheatreDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(381, 310)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.name_ed = QtWidgets.QLineEdit(Dialog)
        self.name_ed.setGeometry(QtCore.QRect(30, 74, 141, 20))
        self.name_ed.setObjectName("name_ed")
        self.city_ed = QtWidgets.QLineEdit(Dialog)
        self.city_ed.setGeometry(QtCore.QRect(200, 74, 151, 20))
        self.city_ed.setObjectName("city_ed")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 105, 331, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.admin_pass_ed = QtWidgets.QLineEdit(Dialog)
        self.admin_pass_ed.setGeometry(QtCore.QRect(30, 132, 321, 20))
        self.admin_pass_ed.setObjectName("admin_pass_ed")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 163, 331, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pass_confirm_ed = QtWidgets.QLineEdit(Dialog)
        self.pass_confirm_ed.setGeometry(QtCore.QRect(30, 193, 321, 20))
        self.pass_confirm_ed.setObjectName("pass_confirm_ed")
        self.message_lb = QtWidgets.QLabel(Dialog)
        self.message_lb.setGeometry(QtCore.QRect(30, 219, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.message_lb.setFont(font)
        self.message_lb.setText("")
        self.message_lb.setObjectName("message_lb")

        self.retranslateUi(Dialog)
        # self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Новый Кинотеатр"))
        self.label_2.setText(_translate("Dialog", "Название"))
        self.label_3.setText(_translate("Dialog", "Город"))
        self.label_4.setText(_translate("Dialog", "Пароль для администратора"))
        self.label_5.setText(_translate("Dialog", "Повторите пароль"))
