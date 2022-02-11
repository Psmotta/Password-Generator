"""
Software developed by: Psmotta

Version 0.3

This software was developed for better understanding Python language
and its an open source code for all students lern more about it.

Created by: PyQt5 UI code generator 5.15.6

Date (m/d/Y)
Date of criation: 02/05/2022
Date of version: 03/10/2022

"""


from cgitb import text
from gettext import gettext
from re import S
from typing import Text
from webbrowser import get
import file_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
import random
import pyperclip as pc


class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(825, 627)
        window.setMinimumSize(QtCore.QSize(825, 627))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo/icon/key2.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.all_frame = QtWidgets.QFrame(self.centralwidget)
        self.all_frame.setStyleSheet("\n"
                                     "background-color: rgb(0, 0, 0);")
        self.all_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.all_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.all_frame.setObjectName("all_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.all_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.password_frame = QtWidgets.QFrame(self.all_frame)
        self.password_frame.setMaximumSize(QtCore.QSize(800, 600))
        self.password_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 20px;")
        self.password_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.password_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.password_frame.setObjectName("password_frame")
        self.label_Tprincipal = QtWidgets.QLabel(self.password_frame)
        self.label_Tprincipal.setGeometry(QtCore.QRect(154, 30, 491, 61))
        self.label_Tprincipal.setStyleSheet("font: 75 26pt \"Cambria\";\n"
                                            "background-position: center;")
        self.label_Tprincipal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Tprincipal.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Tprincipal.setObjectName("label_Tprincipal")
        self.image = QtWidgets.QFrame(self.password_frame)
        self.image.setGeometry(QtCore.QRect(0, 10, 151, 131))
        self.image.setStyleSheet("background-image: url(:/Logo/icon/key2.ico);\n"
                                 "background-repeat: no-repeat;\n"
                                 "background-position: center;")
        self.image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image.setObjectName("image")
        self.Lenght = QtWidgets.QComboBox(self.password_frame)
        self.Lenght.setGeometry(QtCore.QRect(430, 140, 191, 22))
        self.Lenght.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.Lenght.setEditable(False)
        self.Lenght.setObjectName("Lenght")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Lenght.setItemText(24, "28")
        self.Lenght.addItem("")
        self.Lenght.addItem("")
        self.Low = QtWidgets.QCheckBox(self.password_frame)
        self.Low.setGeometry(QtCore.QRect(180, 130, 181, 31))
        self.Low.setStyleSheet("font: 75 14pt \"Cambria\";")
        self.Low.setObjectName("Low")
        self.Upper = QtWidgets.QCheckBox(self.password_frame)
        self.Upper.setGeometry(QtCore.QRect(180, 180, 221, 31))
        self.Upper.setStyleSheet("font: 75 14pt \"Cambria\";")
        self.Upper.setObjectName("Upper")
        self.Symbols = QtWidgets.QCheckBox(self.password_frame)
        self.Symbols.setGeometry(QtCore.QRect(180, 230, 211, 21))
        self.Symbols.setStyleSheet("font: 75 14pt \"Cambria\";")
        self.Symbols.setObjectName("Symbols")
        self.Number = QtWidgets.QCheckBox(self.password_frame)
        self.Number.setGeometry(QtCore.QRect(180, 270, 221, 31))
        self.Number.setStyleSheet("font: 75 14pt \"Cambria\";")
        self.Number.setObjectName("Number")
        self.password_text = QtWidgets.QLineEdit(self.password_frame)
        self.password_text.setGeometry(QtCore.QRect(160, 380, 491, 61))
        self.password_text.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                         "font: 75 12pt \"Arial\";\n"
                                         "border: 2px solid rgb(160, 160, 160);")
        self.password_text.setAlignment(QtCore.Qt.AlignCenter)
        self.password_text.setObjectName("password_text")
        self.label_Tpassword = QtWidgets.QLabel(self.password_frame)
        self.label_Tpassword.setGeometry(QtCore.QRect(50, 390, 101, 41))
        self.label_Tpassword.setStyleSheet("font: 75 17pt \"Cambria\";\n"
                                           "background-position: center;\n"
                                           "border-radius: 0 px;")
        self.label_Tpassword.setObjectName("label_Tpassword")
        self.Button_generate = QtWidgets.QPushButton(self.password_frame)
        self.Button_generate.setGeometry(QtCore.QRect(300, 480, 201, 51))
        self.Button_generate.setStyleSheet("QPushButton {\n"
                                           "    background-color: rgb(198, 198, 198);\n"
                                           "    font: 75 12pt \"Cambria\";\n"
                                           "    border: 2px solid rgb(160, 160, 160);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(160, 160, 160);\n"
                                           "    font: 75 12pt \"Cambria\";\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(230, 230, 230);\n"
                                           "    font: 75 12pt \"Cambria\";\n"
                                           "}")
        self.Button_generate.setObjectName("Button_generate")
        self.Button_generate.clicked.connect(self.password_generator)
        self.button_Copy = QtWidgets.QPushButton(self.password_frame)
        self.button_Copy.setGeometry(QtCore.QRect(660, 380, 75, 61))
        self.button_Copy.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(198, 198, 198);\n"
                                       "    font: 75 12pt \"Cambria\";\n"
                                       "    border: 2px solid rgb(160, 160, 160);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(160, 160, 160);\n"
                                       "    font: 75 12pt \"Cambria\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(230, 230, 230);\n"
                                       "    font: 75 12pt \"Cambria\";\n"
                                       "}")
        self.button_Copy.setObjectName("button_Copy")
        self.button_Copy.clicked.connect(self.copy_password)
        self.label_Tpassword_2 = QtWidgets.QLabel(self.password_frame)
        self.label_Tpassword_2.setGeometry(QtCore.QRect(20, 580, 181, 20))
        self.label_Tpassword_2.setStyleSheet("font: 75 10pt \"Cambria\";\n"
                                             "background-position: center;\n"
                                             "border-radius: 20 px;")
        self.label_Tpassword_2.setObjectName("label_Tpassword_2")
        self.label_Tpassword_3 = QtWidgets.QLabel(self.password_frame)
        self.label_Tpassword_3.setGeometry(QtCore.QRect(650, 580, 131, 20))
        self.label_Tpassword_3.setStyleSheet("font: 75 10pt \"Cambria\";\n"
                                             "background-position: center;\n"
                                             "border-radius: 20 px;")
        self.label_Tpassword_3.setObjectName("label_Tpassword_3")
        self.horizontalLayout.addWidget(self.password_frame)
        self.verticalLayout.addWidget(self.all_frame)
        window.setCentralWidget(self.centralwidget)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

        #
        # FUNCTIONS
        #

    def password_generator(self):

        low = "abcdefghijklmnopqrstuvwxyz"
        up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        NUMBER = "0123456789"
        Symbol = "[]{}%#()*/$&"
        all = ""

        length = int(self.Lenght.currentText())

        if self.Low.isChecked():

            all += low

        if self.Upper.isChecked():

            all += up

        if self.Number.isChecked():

            all += NUMBER

        if self.Symbols.isChecked():

            all += Symbol

        if(len(all) < length):
            self.password_text.setText("Box filds are not checked enough!")

        else:

            password = "".join(random.sample(all, length))
            self.password_text.setText(password)

    def copy_password(self):

        pc.copy(self.password_text.text())

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Password Generator"))
        self.label_Tprincipal.setText(_translate(
            "window", "Random Password Generator"))
        self.Lenght.setItemText(0, _translate("window", "Lenght"))
        self.Lenght.setItemText(1, _translate("window", "5"))
        self.Lenght.setItemText(2, _translate("window", "6"))
        self.Lenght.setItemText(3, _translate("window", "7"))
        self.Lenght.setItemText(4, _translate("window", "8"))
        self.Lenght.setItemText(5, _translate("window", "9"))
        self.Lenght.setItemText(6, _translate("window", "10"))
        self.Lenght.setItemText(7, _translate("window", "11"))
        self.Lenght.setItemText(8, _translate("window", "12"))
        self.Lenght.setItemText(9, _translate("window", "13"))
        self.Lenght.setItemText(10, _translate("window", "14"))
        self.Lenght.setItemText(11, _translate("window", "15"))
        self.Lenght.setItemText(12, _translate("window", "16"))
        self.Lenght.setItemText(13, _translate("window", "17"))
        self.Lenght.setItemText(14, _translate("window", "18"))
        self.Lenght.setItemText(15, _translate("window", "19"))
        self.Lenght.setItemText(16, _translate("window", "20"))
        self.Lenght.setItemText(17, _translate("window", "21"))
        self.Lenght.setItemText(18, _translate("window", "22"))
        self.Lenght.setItemText(19, _translate("window", "23"))
        self.Lenght.setItemText(20, _translate("window", "24"))
        self.Lenght.setItemText(21, _translate("window", "25"))
        self.Lenght.setItemText(22, _translate("window", "26"))
        self.Lenght.setItemText(23, _translate("window", "27"))
        self.Lenght.setItemText(25, _translate("window", "29"))
        self.Lenght.setItemText(26, _translate("window", "30"))
        self.Low.setText(_translate("window", "Low (ex. abcdefgh)"))
        self.Upper.setText(_translate("window", "Upper (ex. ABCDEFGH)"))
        self.Symbols.setText(_translate("window", "Symbols (ex. #$%&)"))
        self.Number.setText(_translate("window", "Numbers (ex. 123456)"))
        self.label_Tpassword.setText(_translate("window", "Password"))
        self.Button_generate.setText(_translate(
            "window", "Generate your password"))
        self.button_Copy.setText(_translate("window", "Copy"))
        self.label_Tpassword_2.setText(_translate(
            "window", "Software developed by: Psmotta"))
        self.label_Tpassword_3.setText(
            _translate("window", "Software version: v0.3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
