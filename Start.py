from PyQt5 import QtCore, QtGui, QtWidgets
from Encrypt import *
from Decrypt import *

from PyQt5 import QtWidgets


class Ui_Dialog(object):

    def openEncrypt(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Encrypt()
        self.ui.setupUi(self.window)
        self.window.show()

    def openDecrypt(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Decrypt()
        self.ui.setupUi(self.window)
        self.window.show()
       
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(629, 400)
        self.label_Title = QtWidgets.QLabel(Dialog)
        self.label_Title.setGeometry(QtCore.QRect(0, 0, 691, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Title.setFont(font)
        self.label_Title.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label_Title.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.label_Title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Title.setTextFormat(QtCore.Qt.AutoText)
        self.label_Title.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_Title.setObjectName("label_Title")
        
        self.label_Title2 = QtWidgets.QLabel(Dialog)
        self.label_Title2.setGeometry(QtCore.QRect(0, 40, 731, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Title2.setFont(font)
        self.label_Title2.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.label_Title2.setObjectName("label_Title2")
        
        self.label_Encrypt = QtWidgets.QLabel(Dialog)
        self.label_Encrypt.setGeometry(QtCore.QRect(60, 110, 590, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Encrypt.setFont(font)
        self.label_Encrypt.setObjectName("label_Encrypt")
        
        self.label_Decrypt = QtWidgets.QLabel(Dialog)
        self.label_Decrypt.setGeometry(QtCore.QRect(60, 170, 590, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Decrypt.setFont(font)
        self.label_Decrypt.setObjectName("label_Decrypt")
        
        self.btn_exit = QtWidgets.QPushButton(Dialog)
        self.btn_exit.setGeometry(QtCore.QRect(520, 340, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName("btn_exit")
        
        self.btn_Decrypt = QtWidgets.QPushButton(Dialog)
        self.btn_Decrypt.setGeometry(QtCore.QRect(370, 250, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Decrypt.setFont(font)
        self.btn_Decrypt.setObjectName("btn_Decrypt")
        
        self.btn_Encrypt = QtWidgets.QPushButton(Dialog)
        self.btn_Encrypt.setGeometry(QtCore.QRect(60, 250, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Encrypt.setFont(font)
        self.btn_Encrypt.setObjectName("btn_Encrypt")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.btn_Encrypt.clicked.connect(self.btnEncrypt)
        self.btn_Decrypt.clicked.connect(self.btnDecrypt)
        self.btn_exit.clicked.connect(self.btnexit)

    def btnEncrypt(self):
        self.openEncrypt()
              
    def btnDecrypt(self):
        self.openDecrypt()
        
    def btnexit(self):
        Dialog.hide()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_Title.setText(_translate("Dialog", "      Здравствуйте! Данная программа была cоздана для шифрования или  "))
        self.label_Title2.setText(_translate("Dialog", "       расшифровывания с помощью метода простой табличной перестановки."))
        self.label_Encrypt.setText(_translate("Dialog", "Если вы хотите зашифровать текст нажмите на кнопку \"Encrypt\"."))
        self.label_Decrypt.setText(_translate("Dialog", "Если вы хотите расшифровать текст нажмите на кнопку \"Decrypt\"."))
        self.btn_exit.setText(_translate("Dialog", "Выход"))
        self.btn_Decrypt.setText(_translate("Dialog", "Decrypt"))
        self.btn_Encrypt.setText(_translate("Dialog", "Encrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    
    Dialog.show()
    sys.exit(app.exec_())
