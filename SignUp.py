from PyQt5 import QtCore, QtGui, QtWidgets
from Login import *
from PyQt5 import QtWidgets
import sqlite3

class Ui_SignUp(object):
    
    def openLogin(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_login()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def setupUi(self, SignUp):
        
        SignUp.setObjectName("SignUp")
        SignUp.resize(400, 397)
        SignUp.setStyleSheet("")
        self.NickD_enter = QtWidgets.QLineEdit(SignUp)
        self.NickD_enter.setGeometry(QtCore.QRect(100, 80, 280, 30))
        self.NickD_enter.setObjectName("NickD_enter")
        
        self.LoginD_enter = QtWidgets.QLineEdit(SignUp)
        self.LoginD_enter.setGeometry(QtCore.QRect(100, 140, 280, 30))
        self.LoginD_enter.setObjectName("LoginD_enter")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(SignUp)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 210, 280, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.btnSignUp_1 = QtWidgets.QPushButton(SignUp)
        self.btnSignUp_1.setGeometry(QtCore.QRect(80, 270, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSignUp_1.setFont(font)
        self.btnSignUp_1.setObjectName("btnSignUp_1")
        
        self.TitleD = QtWidgets.QLabel(SignUp)
        self.TitleD.setGeometry(QtCore.QRect(0, 0, 400, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TitleD.setFont(font)
        self.TitleD.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.TitleD.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleD.setObjectName("TitleD")
        
        self.NickD = QtWidgets.QLabel(SignUp)
        self.NickD.setGeometry(QtCore.QRect(20, 70, 70, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NickD.setFont(font)
        self.NickD.setObjectName("NickD")
        
        self.LoginD = QtWidgets.QLabel(SignUp)
        self.LoginD.setGeometry(QtCore.QRect(20, 140, 70, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LoginD.setFont(font)
        self.LoginD.setObjectName("LoginD")
        
        self.PasswordD = QtWidgets.QLabel(SignUp)
        self.PasswordD.setGeometry(QtCore.QRect(20, 210, 70, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PasswordD.setFont(font)
        self.PasswordD.setObjectName("PasswordD")
        
        self.btnSignUp_2 = QtWidgets.QPushButton(SignUp)
        self.btnSignUp_2.setGeometry(QtCore.QRect(80, 337, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSignUp_2.setFont(font)
        self.btnSignUp_2.setObjectName("btnSignUp_2")

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

        self.btnSignUp_2.clicked.connect(self.btn_exit)
        self.btnSignUp_1.clicked.connect(self.database)


    def btn_exit(self):
        self.openLogin()

    def pop_message(self,text):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()
        

    def database(self):
        try:
            txt_nickname_v=self.NickD_enter.text()
            txt_username_v=self.LoginD_enter.text()
            txt_password_v=self.lineEdit_3.text()

            if ((len(txt_nickname_v) > 3) and (len(txt_username_v) > 3) and (len(txt_password_v) > 3)):
                conn=sqlite3.connect('login.db')
                cursor = conn.cursor()
                
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS credentials
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    nickname TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL)""")

                cursor.execute('SELECT username FROM credentials WHERE username = ?', (txt_username_v,))
                result = cursor.fetchone()

                if result is not None:
                    self.pop_message("Такой логин уже существует! ")
                    
                else:

                    cursor.execute("""
                        INSERT INTO credentials
                        (nickname,
                        username,
                        password)
                    VALUES
                    (?,?,?)
                    """,(txt_nickname_v,txt_username_v,txt_password_v))
                    
                    conn.commit()
                    cursor.close()
                    conn.close()
                    self.pop_message("Данные добавлены в базу данных! ")
                    
            else:
                self.pop_message("""Введите данные в поля и длина ника, логина и пароля должна быть больше 3! """)           
        except:
            self.pop_messege('Введите данные!')

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "Регистрация"))
        self.btnSignUp_1.setText(_translate("SignUp", "Завершить регистрацию"))
        self.TitleD.setText(_translate("SignUp", "Регистрация. Укажите свой ник, логин и пароль."))
        self.NickD.setText(_translate("SignUp", "Ник:"))
        self.LoginD.setText(_translate("SignUp", "Логин:"))
        self.PasswordD.setText(_translate("SignUp", "Пароль:"))
        self.btnSignUp_2.setText(_translate("SignUp", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUp = QtWidgets.QDialog()
    ui = Ui_SignUp()
    ui.setupUi(SignUp)

    
    SignUp.show()
    sys.exit(app.exec_())
