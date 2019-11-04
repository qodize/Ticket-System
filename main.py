import sys
import sqlite3 as sql
from forms import Ui_MainWindow
from SignInWidget import SignInWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton, QTableWidgetItem
from PyQt5.QtGui import QFont


ADD = 'ADD'
DEL = 'DEL'
HALL_COLUMN_COUNT = 6
ALL_COLUMN_COUNT = 7


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
            self.lb2.move(60, 70)
            self.lb2.setFont(font)
            self.lb2.setText("Ширина        Высота")
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
        res = cur.execute("""SELECT name from halls""").fetchall()
        names = [str(x[0]) for x in res]
        print(names)
        self.name = self.name_line.text()
        print(self.name)
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


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sign_in_window = SignInWidget(self)
        self.sign_in_window.show()
        self.halls_comboBox.currentIndexChanged.connect(self.pp)
        self.con = sql.connect("db\\Theatres.db")

        self.new_hall_btn.clicked.connect(self.add_hall)
        self.del_hall_btn.clicked.connect(self.del_hall)

    def pp(self):
        pass

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
        res = cur.execute(f"""SELECT date, "film id", "start time", duration, "free sits", "ticket price" from Sessions
                            WHERE "hall id"=(SELECT id from halls
                                            WHERE name like '{self.current_hall_name}')""").fetchall()
        self.hall_sessions_tb.setRowCount(len(res))
        for i in range(len(res)):
            for j in range(HALL_COLUMN_COUNT):
                self.hall_sessions_tb.setItem(i, j, QTableWidgetItem(f'{res[i][j]}'))

    def update_all_sessions_tb(self):
        cur = self.con.cursor()
        res = cur.execute(f"""SELECT date, "film id", "start time", duration,
                                    "hall id", "free sits", "ticket price" from Sessions
                            WHERE "hall id"=(SELECT id from halls
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
