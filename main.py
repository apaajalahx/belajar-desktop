#!/bin/python3
# code by fb.me/dinar1337

from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QGridLayout,QWidget, \
    QVBoxLayout, QTabWidget, QStatusBar, QColumnView, QTextBrowser,QGraphicsView
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication, QMetaObject
import sys,os

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        try:
            self.setObjectName("MainWindow")
            self.resize(653, 588)
            self.centralwidget = QWidget(self)
            self.centralwidget.setObjectName("centralwidget")
            self.verticalLayout = QVBoxLayout(self.centralwidget)
            self.verticalLayout.setObjectName("verticalLayout")
            self.Page = QTabWidget(self.centralwidget)
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(11)
            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            self.Page.setFont(font)
            self.Page.setMouseTracking(False)
            self.Page.setTabPosition(QTabWidget.North)
            self.Page.setTabShape(QTabWidget.Rounded)
            self.Page.setMovable(True)
            self.Page.setTabBarAutoHide(False)
            self.Page.setObjectName("Page")
            self.home = QWidget()
            self.home.setObjectName("home")
            self.gridLayout = QGridLayout(self.home)
            self.gridLayout.setObjectName("gridLayout")
            self.columnView = QColumnView(self.home)
            self.columnView.setObjectName("columnView")
            self.gridLayout.addWidget(self.columnView, 0, 0, 1, 1)
            self.textBrowser = QTextBrowser(self.home)
            self.textBrowser.setObjectName("textBrowser")
            self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
            self.columnView1 = QColumnView(self.home)
            self.columnView1.setObjectName("columnView1")
            self.gridLayout.addWidget(self.columnView1, 0, 2, 1, 1)
            self.columnView1 = QColumnView(self.home)
            self.columnView1.setObjectName("columnView1")
            self.gridLayout.addWidget(self.columnView1, 1, 1, 1, 1)
            self.columnView1 = QColumnView(self.home)
            self.columnView1.setObjectName("columnView1")
            self.gridLayout.addWidget(self.columnView1, 2, 1, 1, 1)
            self.graphicsView = QGraphicsView(self.home)
            self.graphicsView.setObjectName("graphicsView")
            self.graphicsView.setStyleSheet('background-color:red')
            self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
            self.Page.addTab(self.home, "")
            self.profile = QWidget()
            self.profile.setObjectName("profile")
            self.Page.addTab(self.profile, "")
            self.verticalLayout.addWidget(self.Page)
            self.setCentralWidget(self.centralwidget)
            self.statusbar = QStatusBar(self)
            self.statusbar.setObjectName("statusbar")
            self.setStatusBar(self.statusbar)
            self.retranslateUi()
            self.Page.setCurrentIndex(0)
            QMetaObject.connectSlotsByName(self)
        except Exception as e:
            exc_type, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f'Error type : {exc_type}')
            print(f'Error At Line: {exc_tb.tb_lineno}, File: {fname} ')
            print(f'Error Massage: {e}')

    def retranslateUi(self):
        try:
            _translate = QCoreApplication.translate
            self.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">KONTOL NJEPAT</p></body></html>"))
            self.Page.setTabText(self.Page.indexOf(self.home), _translate("MainWindow", "Home"))
            self.Page.setTabText(self.Page.indexOf(self.profile), _translate("MainWindow", "Profile"))
        except Exception as e:
            exc_type, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f'Error type : {exc_type}')
            print(f'Error At Line: {exc_tb.tb_lineno}, File: {fname} ')
            print(f'Error Massage: {e}')