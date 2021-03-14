import sys
from forms import Ui_SignInWidget, Ui_AdminPassDialog, Ui_OwnerPassDialog, Ui_NewTheatreDialog
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QTableWidgetItem, QAbstractItemView
import sqlite3 as sql
import psycopg2 as psql
from db import db_credentials as db_cred

COLUMN_COUNT = 2
db_con = psql.connect(
    dbname=db_cred.DBNAME,
    user=db_cred.USER,
    password=db_cred.PASSWORD,
    host=db_cred.HOST
)


class NewTheatreDialog(QDialog, Ui_NewTheatreDialog):
    def __init__(self, SignInWidget):
        super().__init__()
        self.setupUi(self)
        self.SignInWidget = SignInWidget
        self.buttonBox.accepted.connect(self.check)

    # метод для проверки корректности введенных данных
    def check(self):
        self.name = self.name_ed.text()
        self.city = self.city_ed.text()
        self.admin_pass = self.admin_pass_ed.text()
        self.admin_pass_rep = self.pass_confirm_ed.text()
        cur = db_con.cursor()
        cur.execute(f"""SELECT * from main.theatres 
                                WHERE name like '{self.name}'""")
        res = cur.fetchone()
        print('check()')

        if self.name == '':
            self.message_lb.setText("Введите название кинотеатра")
        #  если в БД уже есть кинотеатр с таким именем - вывести ошибку
        elif res:
            self.message_lb.setText("Кинотеатр с таким именем уже существует")
        #  если поле "город" оставлено пустым
        elif self.city == '':
            self.message_lb.setText("Введите город")
        elif self.admin_pass == '':
            self.message_lb.setText("Введен пустой пароль")
        # если введенные пароли не совпадают
        elif self.admin_pass != self.admin_pass_rep:
            self.message_lb.setText("Введенные пароли не совпадают")
        else:
            print(self.name, self.city, self.admin_pass)
            cur.execute(f"""INSERT INTO main.theatres(name, city, password)
                            VALUES('{self.name}', '{self.city}', '{self.admin_pass}')""")
            db_con.commit()
            self.close()
            self.SignInWidget.fill_theatres_table()
        cur.close()


class OwnerPassDialog(QDialog, Ui_OwnerPassDialog):
    def __init__(self, func):
        super().__init__()
        self.setupUi(self)
        self.PASSWORD = "123"
        self.func = func
        self.buttonBox.accepted.connect(self.check_line)

    #  проверка пароля
    def check_line(self):
        entered_password = self.password_line.text()
        #  если ввели пустой пароль, выводим ошибку в поле сообщения
        if not entered_password:
            self.message_lb.setText("Ошибка. Введен пустой пароль")
            self.message_lb.resize(self.message_lb.sizeHint())
        #  если пароль неверный - выводим в поле сообщения ошибку
        elif entered_password != self.PASSWORD:
            self.message_lb.setText("Пароль неверный. Введите заново")
            self.message_lb.resize(self.message_lb.sizeHint())
        else:
            self.func()
            self.close()
        self.password_line.setText("")


class AdminPassDialog(QDialog, Ui_AdminPassDialog):
    def __init__(self, func):
        self.theatre = ''  # театр, в который входим
        self.func = func  # функция, которую вызывать при правильном пароле

        super().__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.check_line)

    #  проверка пароля
    def check_line(self):
        cur = db_con.cursor()
        cur.execute(f"""SELECT password from main.theatres
                                         WHERE name like '{self.theatre}'""")
        res = cur.fetchone()
        self.password = str(res[0])

        entered_password = self.password_line.text()
        self.password_line.setText('')
        # print(self.password, entered_password)
        #  если ввели пустой пароль, выводим ошибку в поле сообщения
        if not entered_password:
            self.message_lb.setText("Ошибка. Введен пустой пароль")
            self.message_lb.resize(self.message_lb.sizeHint())
        #  если пароль неверный - выводим в поле сообщения ошибку
        elif entered_password != self.password:
            self.message_lb.setText("Пароль неверный. Введите заново")
            self.message_lb.resize(self.message_lb.sizeHint())
        else:
            print('complete')
            self.func()
            self.close()


class SignInWidget(QWidget, Ui_SignInWidget):
    def __init__(self, MainWindow):
        super().__init__()
        self.setupUi(self)
        self.fill_theatres_table()
        self.MainWindow = MainWindow
        self.theatre_name = ''

        self.admin_pass = AdminPassDialog(self.sign_in)
        self.owner_pass_add = OwnerPassDialog(self.add_theatre)
        self.owner_pass_del = OwnerPassDialog(self.delete_theatre)
        #  Назначаем методы кнопкам
        self.sign_in_btn.clicked.connect(self.sign_in_pass_order)
        self.add_btn.clicked.connect(self.owner_pass_add.show)
        self.del_btn.clicked.connect(self.owner_pass_del.show)
        self.theatresTable.clicked.connect(self.set_theatre_name)

    # метод заполнения таблицы театров
    def fill_theatres_table(self):
        cur = db_con.cursor()
        cur.execute("SELECT * from main.theatres")
        res = cur.fetchall()
        self.theatresTable.setRowCount(len(res))
        for i in range(len(res)):
            for j in range(COLUMN_COUNT):
                self.theatresTable.setItem(i, j, QTableWidgetItem(f"{res[i][j + 1]}"))
        cur.close()

    def sign_in_pass_order(self):
        if self.theatresTable.selectedItems():
            self.admin_pass.theatre = self.theatre_name
            self.admin_pass.show()
        else:
            self.message_lb.setText('Выберете Кинотеатр')

    #  метод входа в систему
    def sign_in(self):
        self.MainWindow.show()
        cur = db_con.cursor()
        cur.execute(f"""SELECT id from main.theatres
                            WHERE name like '{self.theatre_name}'""")
        res = cur.fetchone()
        _id = res[0]
        self.MainWindow.collect_info(_id, self.theatre_name)
        self.close()

    #  метод добавления кинотеатра
    def add_theatre(self):
        self.new_thetre = NewTheatreDialog(self)
        self.new_thetre.show()

    #  метод удаления кинотеатра
    def delete_theatre(self):
        cur = db_con.cursor()
        theatre = self.theatre_name
        cur.execute(f"""SELECT id from main.theatres
                            WHERE name like '{self.theatre_name}'""")
        res = cur.fetchone()
        theatre_id = res[0]
        # удаляем сессии этого кинотеатра
        cur.execute(f"""DELETE from main.sessions
                        WHERE "hall id" IN (SELECT id from main.halls
                                            WHERE parent_theatre = {theatre_id})""")
        db_con.commit()
        # удаляем залы этого кинотеатра
        cur.execute(f"""DELETE from main.halls
                        WHERE parent_theatre = {theatre_id}""")
        db_con.commit()
        # удаляем сам кинотеатр
        cur.execute(f"""DELETE from main.theatres
                        WHERE name like '{theatre}'""")
        self.fill_theatres_table()
        db_con.commit()
        cur.close()

    def set_theatre_name(self):
        self.theatre_name = self.theatresTable.selectedItems()[0].text()


# debug ######################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = SignInWidget("")
    form.show()
    sys.exit(app.exec())
