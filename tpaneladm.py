# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tpaneladm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1339, 700)
        MainWindow.setStyleSheet("background-color: rgb(120, 145, 226)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-40, 0, 1450, 70))
        self.label.setStyleSheet("font: 20pt \"Open Sans\";\n"
"color: rgb(255, 255, 255);\n"
"  width: 100px;\n"
"  margin: 0 auto;\n"
"  background-color: rgb(76, 1, 101);\n"
"  height: 300px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1120, 10, 161, 51))
        self.label_2.setStyleSheet("font: 17pt \"Open Sans\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 70, 681, 30))
        self.label_3.setStyleSheet("font: 20pt \"Open Sans\";\n"
"color:rgb(90, 8, 80);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 100, 1000, 20))
        self.label_4.setStyleSheet("color:rgb(255, 169, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 130, 850, 20))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(260, 190, 911, 20))
        self.label_8.setObjectName("label_8")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(720, 320, 300, 35))
        self.pushButton_14.setStyleSheet("background-color: rgb(255, 255, 255) ;\n"
"border-radius: 4px;\n"
" border: 1px solid black;\n"
"  padding: 5px;\n"
"")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(210, 320, 500, 35))
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 255, 255) ;\n"
"border-radius: 4px;\n"
" border: 1px solid black;\n"
"  padding: 5px;\n"
"")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(210, 400, 350, 35))
        self.pushButton_12.setStyleSheet("background-color: rgb(255, 255, 255) ;\n"
"border-radius: 4px;\n"
" border: 1px solid black;\n"
"  padding: 5px;\n"
"")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(590, 400, 250, 35))
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 255, 255) ;\n"
"border-radius: 4px;\n"
" border: 1px solid black;\n"
"  padding: 5px;\n"
"")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(880, 400, 150, 35))
        self.pushButton_10.setStyleSheet(" background-color: rgb(64, 64, 64);\n"
"color:rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 290, 181, 18))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 370, 181, 18))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(610, 370, 181, 18))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(750, 290, 181, 18))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1450, 447, 58, 131))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1339, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Панель Администратора"))
        self.label_2.setText(_translate("MainWindow", "Отмена"))
        self.label_3.setText(_translate("MainWindow", "Изменить данные пользователей"))
        self.label_4.setText(_translate("MainWindow", "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"))
        self.label_5.setText(_translate("MainWindow", "№                                          ИМЯ                                        Логин                                   Пароль                          Роль в системе                "))
        self.label_8.setText(_translate("MainWindow", "  1                                      Сидор                                        опла213                                    123                                     Аналитик             "))
        self.pushButton_10.setText(_translate("MainWindow", "Изменить"))
        self.label_6.setText(_translate("MainWindow", "Введите имя фамилию"))
        self.label_7.setText(_translate("MainWindow", "Введите логин"))
        self.label_9.setText(_translate("MainWindow", "Введите пароль"))
        self.label_10.setText(_translate("MainWindow", "Введите роль"))
            