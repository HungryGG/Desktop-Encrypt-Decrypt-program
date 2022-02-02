from PyQt5 import QtCore, QtGui, QtWidgets
from SignUp import *
from Start import *
from Encrypt import *
from Decrypt import *

from PyQt5 import QtWidgets
import sqlite3

class Ui_login(object):

    def openSignUp(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SignUp()
        self.ui.setupUi(self.window)
        self.window.show()


    def openStart(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(643, 367)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-40, 0, 741, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setStatusTip("")
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.Login = QtWidgets.QLabel(Dialog)
        self.Login.setGeometry(QtCore.QRect(290, 80, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Login.setFont(font)
        self.Login.setObjectName("Login")
        
        self.login_enter = QtWidgets.QLineEdit(Dialog)
        self.login_enter.setGeometry(QtCore.QRect(140, 110, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_enter.setFont(font)
        self.login_enter.setMouseTracking(False)
        self.login_enter.setText("")
        self.login_enter.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.login_enter.setObjectName("login_enter")
        
        self.Password = QtWidgets.QLabel(Dialog)
        self.Password.setGeometry(QtCore.QRect(290, 150, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        
        self.Password_enter = QtWidgets.QLineEdit(Dialog)
        self.Password_enter.setGeometry(QtCore.QRect(140, 190, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Password_enter.setFont(font)
        self.Password_enter.setText("")
        self.Password_enter.setObjectName("Password_enter")
        
        self.btn_1 = QtWidgets.QPushButton(Dialog)
        self.btn_1.setGeometry(QtCore.QRect(200, 230, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        
        self.btn_2 = QtWidgets.QPushButton(Dialog)
        self.btn_2.setGeometry(QtCore.QRect(200, 300, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btn_2.clicked.connect(self.btn_SignUp)
        self.btn_1.clicked.connect(self.btn_login)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Главная страница"))
        self.label.setText(_translate("Dialog", "Программа для шифрования и расшифрования"))
        self.Login.setText(_translate("Dialog", "Логин"))
        self.Password.setText(_translate("Dialog", "Пароль"))
        self.btn_1.setText(_translate("Dialog", "Войти"))
        self.btn_2.setText(_translate("Dialog", "Зарегистрироваться"))

    def pop_window(self,text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("{}".format(text))
        msg.setInformativeText('{}'.format(text))
        msg.setWindowTitle("{}".format(text))

        msg.exec_()


    def btn_Start(self):
        self.openStart()
              
    def btn_SignUp(self):
        self.openSignUp()

    def btn_login(self):
        
        if (len(self.Password_enter.text()) <= 1 or (len(self.login_enter.text()) <= 1)):
            self.pop_window('Введите данные!')

        else:
            username2 = self.login_enter.text()
            password2 = self.Password_enter.text()

            conn = sqlite3.connect('login.db')
            cur = conn.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS credentials(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL)''')
            cur.execute('SELECT username FROM credentials WHERE username = ? AND password = ?', (username2,password2,))
            result = cur.fetchone()

            if result is None:
                self.pop_window('Пользователь не найден!')
            else:
                self.btn_Start()
                  

if __name__ == "__main__":
    
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_login()
    ui.setupUi(Dialog)

    Dialog.show()
    sys.exit(app.exec_())
