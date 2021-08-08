# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insreport.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QAction
import requests,secrets
from time import sleep
import threading
r = requests.Session()
cookie = secrets.token_hex(8)*2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(308, 610)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -1, 311, 621))
        self.frame.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 30, 191, 61))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 25 21pt \"Segoe UI Light\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 110, 271, 31))
        self.lineEdit.setStyleSheet("border:none;\n"
"background-color: rgb(249, 249, 249);\n"
"border-radius:3px;\n"
"font: 25 9pt \"Segoe UI Light\";")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 160, 271, 31))
        self.lineEdit_2.setStyleSheet("border:none;\n"
"background-color: rgb(249, 249, 249);\n"
"border-radius:3px;\n"
"font: 25 9pt \"Segoe UI Light\";")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 240, 101, 61))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("font: 25 8pt \"Segoe UI Light\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(110, 240, 81, 61))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("font: 25 8pt \"Segoe UI Light\";")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 210, 271, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border:none;\n"
"    background-color: rgb(85, 85, 255);\n"
"border-radius:3px;\n"
"font: 10pt \"Segoe UI Historic\";\n"
"color:white;\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"border:2px solid rgb(227, 227, 227);;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.thelog)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 290, 271, 31))
        self.lineEdit_3.setStyleSheet("border:none;\n"
"background-color: rgb(249, 249, 249);\n"
"border-radius:3px;\n"
"font: 25 9pt \"Segoe UI Light\";")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 570, 271, 23))
        self.lcdNumber.setStyleSheet("border:none;\n"
"background-color: rgb(85, 85, 255);\n"
"border-radius:3px;\n"
"font: 8pt \"Segoe UI Historic\";\n"
"\n"
"")
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(20, 340, 95, 20))
        self.radioButton.setStyleSheet("font: 25 9pt \"Segoe UI Light\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 370, 95, 20))
        self.radioButton_2.setStyleSheet("font: 25 9pt \"Segoe UI Light\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 400, 181, 20))
        self.radioButton_3.setStyleSheet("font: 25 9pt \"Segoe UI Light\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 430, 191, 20))
        self.radioButton_4.setStyleSheet("font: 25 9pt \"Segoe UI Light\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 460, 231, 20))
        self.radioButton_5.setStyleSheet("font: 25 9pt \"Segoe UI Light\";")
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 490, 181, 20))
        self.radioButton_6.setStyleSheet("font: 25 9pt \"Segoe UI Light\";")
        self.radioButton_6.setObjectName("radioButton_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 10, 16, 16))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 15, 79);\n"
"border:none;\n"
"border-radius:8px;")
        self.pushButton_2.setText("")
        self.pushButton_2.clicked.connect(self.exit_window)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 10, 16, 16))
        self.pushButton_3.setStyleSheet("background-color: rgb(38, 214, 29);\n"
"border:none;\n"
"border-radius:8px;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(241, 260, 41, 21))
        self.spinBox.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 25 9pt \"Segoe UI Light\";\n"
"border-radius:1px;")
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(200, 260, 31, 21))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("font: 25 8pt \"Segoe UI Light\";")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 530, 271, 31))
        self.pushButton_4.clicked.connect(self.thst)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"border:none;\n"
"    background-color: rgb(85, 85, 255);\n"
"border-radius:3px;\n"
"font: 10pt \"Segoe UI Historic\";\n"
"color:white;\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"border:2px solid rgb(227, 227, 227);;\n"
"\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "InstaReport"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "   Username "))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "   Password"))
        self.label_2.setText(_translate("MainWindow", "Loggin Status :"))
        self.label_3.setText(_translate("MainWindow", ". . . ."))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "   Target"))
        self.radioButton.setText(_translate("MainWindow", "Spam"))
        self.radioButton_2.setText(_translate("MainWindow", "Self Injury"))
        self.radioButton_3.setText(_translate("MainWindow", "Hate Speech or Symbols"))
        self.radioButton_4.setText(_translate("MainWindow", "Sale or Promotion of drugs"))
        self.radioButton_5.setText(_translate("MainWindow", "Me"))
        self.radioButton_6.setText(_translate("MainWindow", "Harassment or buylling"))
        self.label_4.setText(_translate("MainWindow", "Sleep"))
        self.pushButton_4.setText(_translate("MainWindow", "Start"))

    def login(self):
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
            'x-csrftoken': 'missing', 'mid': cookie}
        data = {'username': self.lineEdit.text(),
                'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(self.lineEdit_2.text()),
                'queryParams': '{}',
                'optIntoOneTap': 'false', }
        req_login = r.post(url, headers=headers, data=data)
        if ("userId") in req_login.text:
            r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
            self.label_3.setText("Logged")
        else:
            self.label_3.setText("Failed Logged")

    def start(self):
        if self.radioButton.isChecked()==True:
            url_id = 'https://www.instagram.com/{}/?__a=1'.format(self.lineEdit_3.text())
            req_id = r.get(url_id).json()
            user_id = str(req_id['logging_page_id'])
            idd = user_id.split('_')[1]
            done = 1
            while True:
                url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
                datas = {'source_name': '', 'reason_id': 1, 'frx_context': ''}  # spam
                report = r.post(url_report, data=datas).text
                sleep(self.spinBox.value())
                done = done + 1
                self.lcdNumber.display(str(done))
                self.lcdNumber.repaint()
        elif self.radioButton_2.isChecked()==True:
            url_id = 'https://www.instagram.com/{}/?__a=1'.format(self.lineEdit_3.text())
            req_id = r.get(url_id).json()
            user_id = str(req_id['logging_page_id'])
            idd = user_id.split('_')[1]
            done = 1
            while True:
                url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
                datas = {'source_name': '', 'reason_id': 2, 'frx_context': ''}  # spam
                report = r.post(url_report, data=datas).text
                sleep(self.spinBox.value())
                done = done+1
                self.lcdNumber.display(str(done))
                self.lcdNumber.repaint()
        elif self.radioButton_3.isChecked()==True:
            url_id = 'https://www.instagram.com/{}/?__a=1'.format(self.lineEdit_3.text())
            req_id = r.get(url_id).json()
            user_id = str(req_id['logging_page_id'])
            idd = user_id.split('_')[1]
            done = 1
            while True:
                url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
                datas = {'source_name': '', 'reason_id': 6, 'frx_context': ''}  # spam
                report = r.post(url_report, data=datas).text
                sleep(self.spinBox.value())
                done = done + 1
                self.lcdNumber.display(str(done))
                self.lcdNumber.repaint()
        elif self.radioButton_4.isChecked()==True:
            url_id = 'https://www.instagram.com/{}/?__a=1'.format(self.lineEdit_3.text())
            req_id = r.get(url_id).json()
            user_id = str(req_id['logging_page_id'])
            idd = user_id.split('_')[1]
            done = 1
            while True:
                url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
                datas = {'source_name': '', 'reason_id': 3, 'frx_context': ''}  # spam
                report = r.post(url_report, data=datas).text
                sleep(self.spinBox.value())
                done = done + 1
                self.lcdNumber.display(str(done))
                self.lcdNumber.repaint()
        elif self.radioButton_5.isChecked()==True:
            url_id = 'https://www.instagram.com/{}/?__a=1'.format(self.lineEdit_3.text())
            req_id = r.get(url_id).json()
            user_id = str(req_id['logging_page_id'])
            idd = user_id.split('_')[1]
            done = 1
            while True:
                url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
                datas = {'source_name': '', 'reason_id': 8, 'frx_context': ''}  # spam
                report = r.post(url_report, data=datas).text
                sleep(self.spinBox.value())
                done = done + 1
                self.lcdNumber.display(str(done))
                self.lcdNumber.repaint()
        elif self.radioButton_6.isChecked()==True:
            url_id = 'https://www.instagram.com/{}/?__a=1'.format(self.lineEdit_3.text())
            req_id = r.get(url_id).json()
            user_id = str(req_id['logging_page_id'])
            idd = user_id.split('_')[1]
            done = 1
            while True:
                url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
                datas = {'source_name': '', 'reason_id': 7, 'frx_context': ''}  # spam
                report = r.post(url_report, data=datas).text
                sleep(self.spinBox.value())
                done = done + 1
                self.lcdNumber.display(str(done))
                self.lcdNumber.repaint()
        else:
            pass
    def thelog(self):
        t = threading.Thread(target=self.login())
        t.start()
    def thst(self):
        tt = threading.Thread(target=self.start())
        tt.start()

    def exit_window(self, event):
        close = QtWidgets.QMessageBox.question(self,
                                               "QUIT?",
                                               "Are you sure want to STOP and EXIT?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            # event.accept()
            event.accept()
        else:
            pass
    def thex(self):
        ttt = threading.Thread(target=self.exit_window)
        ttt.start()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
