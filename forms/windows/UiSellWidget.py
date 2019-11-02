# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms\ui files\UiSellWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SellWidget(object):
    def setupUi(self, SellWidget):
        SellWidget.setObjectName("SellWidget")
        SellWidget.resize(689, 515)
        self.label = QtWidgets.QLabel(SellWidget)
        self.label.setGeometry(QtCore.QRect(4, 290, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.chosen_seats_lb = QtWidgets.QLabel(SellWidget)
        self.chosen_seats_lb.setGeometry(QtCore.QRect(30, 140, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chosen_seats_lb.setFont(font)
        self.chosen_seats_lb.setObjectName("chosen_seats_lb")
        self.total_cost_lb = QtWidgets.QLabel(SellWidget)
        self.total_cost_lb.setGeometry(QtCore.QRect(30, 200, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.total_cost_lb.setFont(font)
        self.total_cost_lb.setObjectName("total_cost_lb")
        self.time_lb = QtWidgets.QLabel(SellWidget)
        self.time_lb.setGeometry(QtCore.QRect(30, 80, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.time_lb.setFont(font)
        self.time_lb.setObjectName("time_lb")
        self.sell_tickets_btn = QtWidgets.QPushButton(SellWidget)
        self.sell_tickets_btn.setGeometry(QtCore.QRect(30, 230, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sell_tickets_btn.setFont(font)
        self.sell_tickets_btn.setObjectName("sell_tickets_btn")
        self.film_name_lb = QtWidgets.QLabel(SellWidget)
        self.film_name_lb.setGeometry(QtCore.QRect(30, 19, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.film_name_lb.setFont(font)
        self.film_name_lb.setObjectName("film_name_lb")
        self.date_lb = QtWidgets.QLabel(SellWidget)
        self.date_lb.setGeometry(QtCore.QRect(30, 50, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.date_lb.setFont(font)
        self.date_lb.setObjectName("date_lb")
        self.hall_plan_sa = QtWidgets.QScrollArea(SellWidget)
        self.hall_plan_sa.setGeometry(QtCore.QRect(180, 51, 500, 450))
        self.hall_plan_sa.setWidgetResizable(True)
        self.hall_plan_sa.setObjectName("hall_plan_sa")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 498, 448))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.hall_plan_sa.setWidget(self.scrollAreaWidgetContents)
        self.hall_number_lb = QtWidgets.QLabel(SellWidget)
        self.hall_number_lb.setGeometry(QtCore.QRect(30, 110, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.hall_number_lb.setFont(font)
        self.hall_number_lb.setObjectName("hall_number_lb")

        self.retranslateUi(SellWidget)
        QtCore.QMetaObject.connectSlotsByName(SellWidget)

    def retranslateUi(self, SellWidget):
        _translate = QtCore.QCoreApplication.translate
        SellWidget.setWindowTitle(_translate("SellWidget", "Продать билеты"))
        self.chosen_seats_lb.setText(_translate("SellWidget", "Выбранные места: "))
        self.total_cost_lb.setText(_translate("SellWidget", "Итоговая сумма: "))
        self.time_lb.setText(_translate("SellWidget", "Время:"))
        self.sell_tickets_btn.setText(_translate("SellWidget", "Продать Билеты"))
        self.film_name_lb.setText(_translate("SellWidget", "Фильм: "))
        self.date_lb.setText(_translate("SellWidget", "Дата: "))
        self.hall_number_lb.setText(_translate("SellWidget", "Зал:"))
