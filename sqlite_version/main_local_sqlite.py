import sqlite3 as sql
import sys

import fpdf
import os

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, \
    QLabel, QLineEdit, QPushButton, QTableWidgetItem, QDialogButtonBox, QWidget

from SignInWidget_local_sqlite import SignInWidget
from forms import Ui_MainWindow
from forms.dialogs.UiNewSessionDialog import Ui_NewSessionDialog
from forms.windows.UiSellWidget import Ui_SellWidget

ADD = 'ADD'
DEL = 'DEL'
HALL_COLUMN_COUNT = 7
ALL_COLUMN_COUNT = 8


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sign_in_window = SignInWidget(self)
        self.sign_in_window.show()
        self.r_u_shure_del_dialog = AreYouShureToDel(self)

        self.new_session_btn.clicked.connect(self.add_session)
        self.delete_session_btn.clicked.connect(self.r_u_shure_del_dialog.show)
        self.edit_session_btn.clicked.connect(self.edit_session)

        self.halls_comboBox.currentIndexChanged.connect(self.updatehall)
        self.con = sql.connect("db\\Theatres.db")

        self.new_hall_btn.clicked.connect(self.add_hall)
        self.del_hall_btn.clicked.connect(self.del_hall)
        self.sell_tickets_btn.clicked.connect(self.sell_ticket)

    def add_session(self):
        self.new_session_dialog = SessionDialog(self.current_hall_name)
        self.new_session_dialog.show()

    def edit_session(self):
        items = self.hall_sessions_tb.selectedItems()
        self.edit_session_dialog = SessionDialog(self.current_hall_name, items)

    def collect_info(self, id, name):
        self.theatre_id  = id
        self.theatre_name = name
        self.theatreName_lb.setText(self.theatre_name)
        self.halls_comboBox.clear()
        cur = self.con.cursor()
        res = cur.execute(f"""SELECT name from halls
                            WHERE parent_theatre=(SELECT id from theatres
                                                WHERE theatres.name like '{self.theatre_name}')""").fetchall()
        names = [str(x[0]) for x in res]
        [self.halls_comboBox.addItem(name) for name in names]
        cur.close()
        self.updatehall()
        self.update_all_sessions_tb()

    def add_hall(self):
        self.add_hall_dialog = HallDialog(self.theatre_id, ADD)
        self.add_hall_dialog.show()

    def del_hall(self):
        self.del_hall_dialog = HallDialog(self.theatre_id, DEL)
        self.del_hall_dialog.show()

    def updatehall(self):
        self.current_hall_name = self.halls_comboBox.currentText()
        self.hall_name_lb.setText(self.current_hall_name)
        self.hall_name_lb.resize(self.hall_name_lb.sizeHint())
        cur = self.con.cursor()
        res = cur.execute(f"""SELECT date, "film name", "start time", duration,
                                "free sits", "ticket price", id from Sessions
                            WHERE "hall id"=(SELECT id from halls
                                            WHERE name like '{self.current_hall_name}')""").fetchall()
        self.hall_sessions_tb.setRowCount(len(res))
        for i in range(len(res)):
            for j in range(HALL_COLUMN_COUNT):
                self.hall_sessions_tb.setItem(i, j, QTableWidgetItem(f'{res[i][j]}'))

    def update_all_sessions_tb(self):
        cur = self.con.cursor()
        res = cur.execute(f"""SELECT date, "film name", "start time", duration,
                                    "hall id", "free sits", "ticket price", id from Sessions
                            WHERE "hall id" IN (SELECT id from halls
                                        WHERE parent_theatre=(SELECT id from theatres
                                                            WHERE name like '{self.theatre_name}'))""").fetchall()
        self.all_sessions_tb.setRowCount(len(res))
        for i in range(len(res)):
            for j in range(ALL_COLUMN_COUNT):
                if j == 4:
                    hall_name = cur.execute(f"""SELECT name from halls
                                            WHERE id={res[i][j]}""").fetchone()[0]
                    self.all_sessions_tb.setItem(i, j, QTableWidgetItem(f'{hall_name}'))
                else:
                    self.all_sessions_tb.setItem(i, j, QTableWidgetItem(f'{res[i][j]}'))
        cur.close()

    def del_session(self):
        selected = self.hall_sessions_tb.selectedItems()
        if not selected:
            pass
        else:
            session_id = selected[-1].text()
            cur = self.con.cursor()
            cur.execute(f"""DELETE from Sessions
                            WHERE id={session_id}""")
            self.con.commit()
            cur.close()
            self.update_all_sessions_tb()
            self.updatehall()

    def sell_ticket(self):
        items = self.all_sessions_tb.selectedItems()
        if len(items) > ALL_COLUMN_COUNT:
            self.message_lb.setText('Выберите только один сеанс.')
            self.message_lb.resize(self.message_lb.sizeHint())
        elif items:
            self.sell_ticket_widget = SellTicket(items)
            self.sell_ticket_widget.show()
        else:
            self.message_lb.setText('Выберите сеанс.')
            self.message_lb.resize(self.message_lb.sizeHint())


class HallDialog(QDialog):
    def __init__(self, theatre_id, mode):
        super().__init__()
        self.theatre_id = theatre_id
        self.mode = mode
        self.setupUi()
        self.btn.clicked.connect(self.confirm)

    def setupUi(self):
        self.setGeometry(400, 400, 350, 225)
        self.lb = QLabel(self)
        self.lb.move(115, 10)
        self.lb.setText("Название")
        font = QFont()
        font.setPointSize(14)
        self.lb.setFont(font)
        self.lb.resize(self.lb.sizeHint())
        self.name_line = QLineEdit(self)
        self.name_line.move(25, 40)
        self.name_line.resize(250, 25)
        if self.mode == ADD:
            self.lb2 = QLabel(self)
            self.lb2.move(15, 70)
            font.setPointSize(10)
            self.lb2.setFont(font)
            self.lb2.setText("Кол-во сидений в ряду |   Кол-во рядов")
            self.lb2.resize(self.lb2.sizeHint())
            self.wid_line = QLineEdit(self)
            self.wid_line.move(40, 100)
            self.wid_line.resize(100, 25)
            self.heg_line = QLineEdit(self)
            self.heg_line.move(160, 100)
            self.heg_line.resize(100, 25)
        self.btn = QPushButton(self)
        self.btn.resize(100, 30)
        self.btn.move(25, 150)
        font = QFont()
        font.setPointSize(12)
        self.btn.setFont(font)
        self.btn.setText("ОК")
        self.message_lb = QLabel(self)
        self.message_lb.move(25, 190)
        self.message_lb.resize(self.message_lb.sizeHint())

    def confirm(self):
        self.con = sql.connect("db\\Theatres.db")
        cur = self.con.cursor()
        res = cur.execute(f"""SELECT name from halls
                             WHERE parent_theatre={self.theatre_id}""").fetchall()
        names = [str(x[0]) for x in res]
        self.name = self.name_line.text()
        if self.mode == ADD:
            self.width, self.height = self.wid_line.text(), self.heg_line.text()
            if self.name in names:
                self.message_lb.setText('Зал с таким названием уже существует')
                self.message_lb.resize(self.message_lb.sizeHint())
            elif not self.width.isdigit() or not self.height.isdigit():
                self.message_lb.setText('Неправильно введены ширина или высота')
                self.message_lb.resize(self.message_lb.sizeHint())
            else:
                cur.execute(f"""INSERT INTO halls(name, parent_theatre, width, height)
                                VALUES('{self.name}', {self.theatre_id}, {self.width}, {self.height})""")
                self.con.commit()
                self.close()

        elif self.mode == DEL:
            if self.name not in names:
                self.message_lb.setText('Нет зала с таким названием')
                self.message_lb.resize(self.message_lb.sizeHint())
            else:
                cur.execute(f"""DELETE from halls
                            WHERE name like '{self.name}' and parent_theatre={self.theatre_id}""")
                self.con.commit()
                self.close()
        cur.close()
        self.con.close()
        main_window.collect_info(main_window.theatre_id, main_window.theatre_name)


class SessionDialog(QDialog, Ui_NewSessionDialog):
    def __init__(self, hall_name, items=None):
        super().__init__()
        self.setupUi(self)
        self.show()
        if items is None:
            self.hall_name = hall_name
            self.date_edit.setDate(QtCore.QDate.currentDate())
            self.buttonBox.accepted.connect(self.add_session)
        else:
            if not items:
                self.reject()
            else:
                date = items[0].text()  # yyyy.mm.dd
                year, month, day = [int(x) for x in date.split('.')]
                self.date = QtCore.QDate(year, month, day)

                self.film_name = items[1].text()

                time = items[2].text()  # hh.mm
                hours, mins = [int(x) for x in time.split(':')]
                self.start_time = QtCore.QTime(hours, mins)

                self.duration = int(items[3].text())
                self.free_sits = int(items[4].text())
                self.ticket_price = int(items[5].text())
                self.session_id = int(items[6].text())

                self.set_info()
                self.buttonBox.accepted.connect(self.update_session)

    def update_session(self):
        self.collect_info()
        con = sql.connect('db\\Theatres.db')
        cur = con.cursor()
        cur.execute(f"""UPDATE Sessions
                        SET date='{self.date}',
                        "film name"='{self.film_name}',
                        "start time"='{self.start_time}',
                        duration={self.duration},
                        "ticket price"={self.ticket_price}
                        WHERE id={self.session_id}""")
        con.commit()
        cur.close()
        con.close()
        main_window.update_all_sessions_tb()
        main_window.updatehall()
        self.close()

    def collect_info(self):
        self.date = self.date_edit.text()
        self.film_name = str(self.film_name_edit.text())
        self.start_time = self.start_time_edit.text()
        self.duration = int(self.duration_box.text())
        self.ticket_price = int(self.price_box.text())

    def set_info(self):
        self.date_edit.setDate(self.date)
        self.film_name_edit.setText(self.film_name)
        self.start_time_edit.setTime(self.start_time)
        self.duration_box.setValue(self.duration)
        self.price_box.setValue(self.ticket_price)

    def add_session(self):
        self.collect_info()
        # print(self.date, self.film_name, self.start_time, self.duration, self.ticket_price)
        if not self.film_name:
            self.message_lb.setText('Вы ввели пустое название фильма!')
        else:
            con = sql.connect("db\\Theatres.db")
            cur = con.cursor()
            hall_id = cur.execute(f"""SELECT id from halls WHERE name like '{self.hall_name}'""").fetchone()[0]
            free_sits = cur.execute(f"""SELECT height, width from halls WHERE id={hall_id}""").fetchall()[0]
            free_sits = free_sits[0] * free_sits[1]
            cur.execute(f"""INSERT INTO Sessions(date, "film name", "start time", duration,
                                        "hall id", "free sits", "ticket price") 
                            VALUES ('{self.date}', '{self.film_name}', '{self.start_time}',
                            {self.duration}, {hall_id}, {free_sits}, {self.ticket_price})""")
            con.commit()
            cur.close()
            con.close()
            main_window.update_all_sessions_tb()
            main_window.updatehall()
            self.close()


class AreYouShureToDel(QDialog):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        ##setupUi
        self.setGeometry(400, 400, 381, 210)
        self.label = QLabel("Вы уверены?", self)
        self.label.setGeometry(75, 50, 200, 50)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(20, 160, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        ##
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.accepted.connect(MainWindow.del_session)


class SellTicket(QWidget, Ui_SellWidget):
    def __init__(self, items):
        super().__init__()
        self.setupUi(self)
        self.con = sql.connect("db\\Theatres.db")

        self.date, self.film_name, self.start_time,\
        self.duration, self.hall_name, self.free_sits, self.ticket_price,\
        self.session_id = [item.text() for item in items]

        self.set_info()
        self.numbers = []

        cur = self.con.cursor()
        self.hall_id = cur.execute(f"""SELECT id from halls
                                        WHERE name like '{self.hall_name}'""").fetchone()[0]
        column_count, row_count = cur.execute(f"""SELECT width, height from halls
                                        WHERE id={self.hall_id}""").fetchone()
        self.seats_table.setColumnCount(column_count)
        self.seats_table.setRowCount(row_count)
        self.booked_seats = cur.execute(f"""SELECT row, column from booked_seats
                                                WHERE session_id={self.session_id}""").fetchall()
        for i in range(row_count):
            for j in range(column_count):
                if (i, j) in self.booked_seats:
                    url = "icons\\booked_seat.png"
                else:
                    url = "icons\\default_seat.png"
                icon = QtGui.QIcon(QtGui.QPixmap(QtGui.QPixmap(url).scaled(45, 45, QtCore.Qt.IgnoreAspectRatio)))
                item = QTableWidgetItem(icon, "")
                self.seats_table.setItem(i, j, item)
        self.seats_table.itemSelectionChanged.connect(self.update_chosen_seats)

        self.sell_tickets_btn.clicked.connect(self.sell_tickets)

    def sell_tickets(self):
        cur = self.con.cursor()
        if self.numbers:
            for row, col in self.numbers:
                cur.execute(f"""INSERT INTO booked_seats (session_id, row, column)
                                VALUES ({self.session_id}, {row}, {col})""")
                self.con.commit()
        self.booked_seats = cur.execute(f"""SELECT row, column from booked_seats
                                                        WHERE session_id={self.session_id}""").fetchall()

        cur.execute(f"""UPDATE Sessions
                        SET "free sits"=(SELECT width from halls WHERE id={self.hall_id}) *
                        (SELECT height from halls WHERE id={self.hall_id}) - {len(self.booked_seats)}
                        WHERE id={self.session_id}""")
        self.con.commit()
        self.close()
        main_window.updatehall()
        main_window.update_all_sessions_tb()
        self.make_pdf()

    def make_pdf(self):
        ticket_pdf = fpdf.FPDF(format='A5')
        ticket_pdf.add_font('DejaVu', '', 'DejaVu_Sans\\DejaVuSans.ttf', True)
        ticket_pdf.set_font('DejaVu', size=10)
        i = 0
        for row, col in self.numbers:
            i += 1
            ticket_pdf.add_page()
            ticket_pdf.text(10, 10, f'Кинотеатр: {main_window.theatre_name}')
            ticket_pdf.text(10, 20, f'Фильм: {self.film_name}')
            ticket_pdf.text(10, 30, f'Дата, время: {self.date}, {self.start_time}')
            ticket_pdf.text(10, 40, f'Зал: {self.hall_name}')
            ticket_pdf.text(10, 50, f'Ряд, место: {row}, {col}')
            ticket_pdf.text(10, 60, '-------------------------------------')
            ticket_pdf.text(10, 70, f'№ {int(self.free_sits) - i} (отрежет контролер)')
        ticket_pdf.output('tickets.pdf')
        os.startfile('tickets.pdf')

    def set_info(self):
        self.film_name_lb.setText(self.film_name)
        self.date_lb.setText(self.date)
        self.time_lb.setText(self.start_time)
        self.hall_name_lb.setText(f"Зал {self.hall_name}")

    def update_chosen_seats(self):
        items = self.seats_table.selectedItems()
        self.numbers = sorted([(item.row(), item.column()) for item in items])
        self.chosen_seats_pte.clear()
        for row, col in self.numbers:
            self.chosen_seats_pte.appendPlainText(f"Ряд {row + 1}, Место {col + 1}\n")

        for row, col in self.booked_seats:
            self.seats_table.item(row, col).setSelected(False)

        self.total_cost_lb.setText("Итого: " + str(int(self.ticket_price) * (len(self.numbers))))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
