from PyQt5 import QtCore, QtGui, QtWidgets
from Start import *

from PyQt5 import QtWidgets

     
class Ui_Encrypt(object):

    def openStart(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

        
    def setupUi(self, Encrypt):
        Encrypt.setObjectName("Encrypt")
        Encrypt.resize(534, 450)
        self.textEdit_original = QtWidgets.QTextEdit(Encrypt)
        self.textEdit_original.setGeometry(QtCore.QRect(10, 40, 511, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_original.setFont(font)
        self.textEdit_original.setObjectName("textEdit_original")
        
        self.label_original = QtWidgets.QLabel(Encrypt)
        self.label_original.setGeometry(QtCore.QRect(10, 0, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_original.setFont(font)
        self.label_original.setObjectName("label_original")
        
        self.lineEdit_key = QtWidgets.QLineEdit(Encrypt)
        self.lineEdit_key.setGeometry(QtCore.QRect(280, 140, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_key.setFont(font)
        self.lineEdit_key.setObjectName("lineEdit_key")
        
        self.label_key = QtWidgets.QLabel(Encrypt)
        self.label_key.setGeometry(QtCore.QRect(10, 140, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_key.setFont(font)
        self.label_key.setObjectName("label_key")
        
        self.label_key_support = QtWidgets.QLabel(Encrypt)
        self.label_key_support.setGeometry(QtCore.QRect(10, 170, 231, 21))
        self.label_key_support.setObjectName("label_key_support")
        
        self.label_btn = QtWidgets.QLabel(Encrypt)
        self.label_btn.setGeometry(QtCore.QRect(10, 210, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_btn.setFont(font)
        self.label_btn.setObjectName("label_btn")
        
        self.Encrypt_btn = QtWidgets.QPushButton(Encrypt)
        self.Encrypt_btn.setGeometry(QtCore.QRect(370, 200, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Encrypt_btn.setFont(font)
        self.Encrypt_btn.setObjectName("Encrypt_btn")
        
        self.label_Encrypt = QtWidgets.QLabel(Encrypt)
        self.label_Encrypt.setGeometry(QtCore.QRect(10, 270, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Encrypt.setFont(font)
        self.label_Encrypt.setObjectName("label_Encrypt")
        
        self.textEdit_Encrypt = QtWidgets.QTextEdit(Encrypt)
        self.textEdit_Encrypt.setGeometry(QtCore.QRect(10, 310, 511, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_Encrypt.setFont(font)
        self.textEdit_Encrypt.setObjectName("textEdit_Encrypt")
        
        self.btn_Exit = QtWidgets.QPushButton(Encrypt)
        self.btn_Exit.setGeometry(QtCore.QRect(380, 410, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Exit.setFont(font)
        self.btn_Exit.setObjectName("btn_Exit")

        self.retranslateUi(Encrypt)
        QtCore.QMetaObject.connectSlotsByName(Encrypt)

        self.btn_Exit.clicked.connect(self.Exit)
        self.Encrypt_btn.clicked.connect(self.Crypt)
        mytext = self.textEdit_original.toPlainText()
        

    def Exit(self):
        self.openStart()

    def retranslateUi(self, Encrypt):
        _translate = QtCore.QCoreApplication.translate
        Encrypt.setWindowTitle(_translate("Encrypt", "Шифрование"))
        self.label_original.setText(_translate("Encrypt", "Введите текст для шифрования:"))
        self.label_key.setText(_translate("Encrypt", "Введите ключ для шифрования:"))
        self.label_key_support.setText(_translate("Encrypt", "(Используйте для ключа цифры)"))
        self.label_btn.setText(_translate("Encrypt", "Нажмите на кнопку для шифрования текста."))
        self.Encrypt_btn.setText(_translate("Encrypt", "Зашифровать"))
        self.label_Encrypt.setText(_translate("Encrypt", "Зашифрованный текст:"))
        self.btn_Exit.setText(_translate("Encrypt", "Выход"))

    def pop_window(self,text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("{}".format(text))
        msg.setInformativeText('{}'.format(text))
        msg.setWindowTitle("{}".format(text))

        msg.exec_()

    def Crypt(self):
        key = self.lineEdit_key.text()
        text = self.textEdit_original.toPlainText()
        if len(key) < 1 or len(text) < 1:
            self.pop_window('Введите текст в поле ввода и ключ! ')
        else:
            key_length = len(key)
            result = ""
            lines = len(text) // key_length + 1 # количество списков в вашей матрице
            for n in key: # каждая цифра из ключа
                for x in range(lines): # каждый список из воображаемой матрицы
                    index = int(n) + (key_length * x - 1) # позиция в исходной строке
                    try: # на случай выхода за пределы строки
                        result = result + text[index]
                    except:
                        result = result + " " # если нужен пробел
                        pass
            self.textEdit_Encrypt.setPlainText(result)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Encrypt = QtWidgets.QDialog()
    ui = Ui_Encrypt()
    ui.setupUi(Encrypt)
    
    Encrypt.show()
    sys.exit(app.exec_())
