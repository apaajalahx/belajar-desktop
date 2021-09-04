#!/bin/python3
# code by fb.me/dinar1337
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
import sys, os
from session.session import create_session, delete_session, load_session
from main import Main


class Application(QMainWindow):
    def __init__(self):
        super(Application,self).__init__()
        if load_session():
            self.index()
        else:
            self.quit()
            self.screen = Main()
            self.screen.show()
    
    def index(self):
        uic.loadUi('ui/login.ui',self)
        self.setWindowTitle('HOME')
        self.setWindowIcon(QIcon("ui/icon"))
        self.login_ = self.findChild(QPushButton, 'Login') # Find the button
        self.login_.clicked.connect(self.login)
        self.cencel = self.findChild(QPushButton, 'Cencel')
        self.cencel.clicked.connect(self.quit)
        self.username = self.findChild(QLineEdit, 'username')
        self.password = self.findChild(QLineEdit, 'password')
        self.show()

    def login(self):
        try:
            if len(self.username.text()) <= 0 or len(self.password.text()) <= 0:
                self._error('Error Login','Username Atau password tidak boleh kosong!!!')
            else:
                print(0)
        except Exception as e:
            exc_type, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f'Error type : {exc_type}')
            print(f'Error At Line: {exc_tb.tb_lineno}, File: {fname} ')
            print(f'Error Massage: {e}')

    def _error(self, title, massage):
        QMessageBox.about(self,title,massage)

    def quit(self):
        self.close()

app = QApplication(sys.argv)
window = Application()
app.exec_()