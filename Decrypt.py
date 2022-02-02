from PyQt5 import QtCore, QtGui, QtWidgets
from Start import *

from PyQt5 import QtWidgets

class Ui_Decrypt(object):

    def openStart(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def setupUi(self, Decrypt):
        Decrypt.setObjectName("Decrypt")
        Decrypt.resize(553, 445)
        self.label_Decrypt = QtWidgets.QLabel(Decrypt)
        self.label_Decrypt.setGeometry(QtCore.QRect(10, 0, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Decrypt.setFont(font)
        self.label_Decrypt.setObjectName("label_Decrypt")
        
        self.textEdit_Decrypt = QtWidgets.QTextEdit(Decrypt)
        self.textEdit_Decrypt.setGeometry(QtCore.QRect(10, 40, 531, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_Decrypt.setFont(font)
        self.textEdit_Decrypt.setObjectName("textEdit_Decrypt")
        
        self.label_keyD = QtWidgets.QLabel(Decrypt)
        self.label_keyD.setGeometry(QtCore.QRect(10, 130, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_keyD.setFont(font)
        self.label_keyD.setObjectName("label_keyD")
        
        self.label_key_support = QtWidgets.QLabel(Decrypt)
        self.label_key_support.setGeometry(QtCore.QRect(10, 170, 231, 21))
        self.label_key_support.setObjectName("label_key_support")
        
        self.label_key_support_2 = QtWidgets.QLabel(Decrypt)
        self.label_key_support_2.setGeometry(QtCore.QRect(270, 170, 271, 21))
        self.label_key_support_2.setObjectName("label_key_support_2")
        
        self.lineEdit_key = QtWidgets.QLineEdit(Decrypt)
        self.lineEdit_key.setGeometry(QtCore.QRect(280, 130, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_key.setFont(font)
        self.lineEdit_key.setObjectName("lineEdit_key")
        
        self.label_OrigD = QtWidgets.QLabel(Decrypt)
        self.label_OrigD.setGeometry(QtCore.QRect(10, 270, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_OrigD.setFont(font)
        self.label_OrigD.setObjectName("label_OrigD")
        
        self.textEdit_OrigD = QtWidgets.QTextEdit(Decrypt)
        self.textEdit_OrigD.setGeometry(QtCore.QRect(10, 310, 531, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_OrigD.setFont(font)
        self.textEdit_OrigD.setObjectName("textEdit_OrigD")
        
        self.btn_ExitD = QtWidgets.QPushButton(Decrypt)
        self.btn_ExitD.setGeometry(QtCore.QRect(400, 400, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_ExitD.setFont(font)
        self.btn_ExitD.setObjectName("btn_ExitD")
        
        self.label_btn = QtWidgets.QLabel(Decrypt)
        self.label_btn.setGeometry(QtCore.QRect(10, 220, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_btn.setFont(font)
        self.label_btn.setObjectName("label_btn")
        
        self.Decrypt_btn = QtWidgets.QPushButton(Decrypt)
        self.Decrypt_btn.setGeometry(QtCore.QRect(390, 210, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Decrypt_btn.setFont(font)
        self.Decrypt_btn.setObjectName("Decrypt_btn")

        self.retranslateUi(Decrypt)
        QtCore.QMetaObject.connectSlotsByName(Decrypt)

        self.btn_ExitD.clicked.connect(self.ExitD)
        self.Decrypt_btn.clicked.connect(self.Decrypt)

    def ExitD(self):
        self.openStart()

    def retranslateUi(self, Decrypt):
        _translate = QtCore.QCoreApplication.translate
        Decrypt.setWindowTitle(_translate("Decrypt", "Расшифрование"))
        self.label_Decrypt.setText(_translate("Decrypt", "Введите текст для расшифрования:"))
        self.label_keyD.setText(_translate("Decrypt", "Введите ключ для расшифрования:"))
        self.label_key_support.setText(_translate("Decrypt", "(Используйте для ключа цифры)"))
        self.label_key_support_2.setText(_translate("Decrypt", "(Ключ нужен тот же, что и при шифровании)"))
        self.label_OrigD.setText(_translate("Decrypt", "Расшифрованный текст:"))
        self.btn_ExitD.setText(_translate("Decrypt", "Выход"))
        self.label_btn.setText(_translate("Decrypt", "Нажмите на кнопку для расшифрования текста."))
        self.Decrypt_btn.setText(_translate("Decrypt", "Расшифровать"))

    def pop_window(self,text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("{}".format(text))
        msg.setInformativeText('{}'.format(text))
        msg.setWindowTitle("{}".format(text))

        msg.exec_()

    def Decrypt(self):
        key = self.lineEdit_key.text()
        text = self.textEdit_Decrypt.toPlainText()
        if len(key) < 1 or len(text) < 1:
            self.pop_window('Введите текст в поле ввода и ключ! ')
        else:
            key_length = len(key)
            result = ""
            row = len(text) // key_length
            lines = len(text) // row # количество списков в вашей матрице
            q = 0
            i = 0
            j = 0
            x = str()
            ret = []
            matrix = [[0 for x in range(row)] for y in range(lines)] #Создаём матрицу
            for x in text:
                matrix[i][j] = x
                j=j+1
                if j%row == 0:
                    j=0
                    i=i+1
            while q != row:
                for n in key:
                    ret += matrix[(int(n))-1][q]
                q=q+1
            sret = ''.join(ret)
            self.textEdit_OrigD.setPlainText(sret) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Decrypt = QtWidgets.QDialog()
    ui = Ui_Decrypt()
    ui.setupUi(Decrypt)
    Decrypt.show()
    sys.exit(app.exec_())
