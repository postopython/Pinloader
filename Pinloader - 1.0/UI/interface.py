# -*- coding: utf-8 -*-


from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QFileDialog
from PySide2.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 500)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setWindowIcon(QIcon("UI/logo.png"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(30,30,30);")
        self.centralwidget.setObjectName("centralwidget")

        self.name = QtWidgets.QLabel(self.centralwidget) #название программы под лого
        self.name.setGeometry(QtCore.QRect(10, 200, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.name.setFont(font)
        self.name.setStyleSheet("color: rgb(255, 255, 255);")
        self.name.setObjectName("name")

        self.text_link = QtWidgets.QLabel(self.centralwidget) #текст, указывающий, что надо ввести ссылку на доску
        self.text_link.setGeometry(QtCore.QRect(14, 290, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.text_link.setFont(font)
        self.text_link.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(38,38,38);")
        self.text_link.setAlignment(QtCore.Qt.AlignCenter)
        self.text_link.setObjectName("text_link")

        self.logo = QtWidgets.QLabel(self.centralwidget) #логотип
        self.logo.setGeometry(QtCore.QRect(50, 20, 181, 171))
        self.logo.setText("")
        self.logo.setPixmap(
            QtGui.QPixmap("UI/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.violetbackground1 = QtWidgets.QLabel(self.centralwidget) #фиолетовый фон позади кнопок
        self.violetbackground1.setGeometry(QtCore.QRect(11, 287, 512, 46))
        self.violetbackground1.setStyleSheet("background-color: rgb(136,68,236);")
        self.violetbackground1.setText("")
        self.violetbackground1.setObjectName("violetbackground1")

        self.violetbackground2 = QtWidgets.QLabel(self.centralwidget) #фиолетовый фон позади кнопок
        self.violetbackground2.setGeometry(QtCore.QRect(11, 340, 512, 46))
        self.violetbackground2.setStyleSheet("background-color: rgb(136,68,236);")
        self.violetbackground2.setText("")
        self.violetbackground2.setObjectName("violetbackground2")

        self.text_folder = QtWidgets.QLabel(self.centralwidget) #текст, намекающий, что надо выбрать папку
        self.text_folder.setGeometry(QtCore.QRect(14, 343, 201, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.text_folder.setFont(font)
        self.text_folder.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(38,38,38);")
        self.text_folder.setAlignment(QtCore.Qt.AlignCenter)
        self.text_folder.setObjectName("text_folder")

        self.boardlink = QtWidgets.QLineEdit(self.centralwidget)
        self.boardlink.setGeometry(QtCore.QRect(239, 290, 281, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.boardlink.setFont(font)
        self.boardlink.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "selection-background-color: rgb(136,68,236);")
        self.boardlink.setObjectName("boardlink")

        self.createfolder = QtWidgets.QCheckBox(self.centralwidget) #чекбокс "Создать новую папку"
        self.createfolder.setGeometry(QtCore.QRect(24, 396, 141, 40))
        self.createfolder.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.createfolder.setFont(font)
        self.createfolder.setMouseTracking(False)
        self.createfolder.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.createfolder.setAutoFillBackground(False)
        self.createfolder.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "selection-color: rgb(136,68,236);\n"
                                        "background-color: rgb(38,38,38);")
        self.createfolder.setObjectName("createfolder")

        self.violetbackground3 = QtWidgets.QLabel(self.centralwidget) #фиолетовый фон позади кнопок
        self.violetbackground3.setGeometry(QtCore.QRect(11, 393, 512, 46))
        self.violetbackground3.setStyleSheet("background-color: rgb(136,68,236);")
        self.violetbackground3.setText("")
        self.violetbackground3.setObjectName("violetbackground3")

        self.foldername = QtWidgets.QLineEdit(self.centralwidget) #название папки при создании новой папки
        self.foldername.setGeometry(QtCore.QRect(169, 396, 351, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.foldername.setFont(font)
        self.foldername.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "selection-background-color: rgb(136,68,236);\n"
                                      "color: rgb(0, 0, 0);")
        self.foldername.setInputMethodHints(QtCore.Qt.ImhNone)
        self.foldername.setPlaceholderText("Укажите название папки")
        self.foldername.setObjectName("foldername")

        self.blackbackground1 = QtWidgets.QLabel(self.centralwidget) #чёрный фон позади чекбокса
        self.blackbackground1.setGeometry(QtCore.QRect(14, 396, 150, 40))
        self.blackbackground1.setText("")
        self.blackbackground1.setObjectName("blackbackground1")

        self.tagline1 = QtWidgets.QLabel(self.centralwidget) #"Скопировал ссылку"
        self.tagline1.setGeometry(QtCore.QRect(270, 50, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tagline1.setFont(font)
        self.tagline1.setStyleSheet("color: rgb(255, 255, 255);")
        self.tagline1.setObjectName("tagline1")

        self.tagline2 = QtWidgets.QLabel(self.centralwidget) #"Выбрал папку"
        self.tagline2.setGeometry(QtCore.QRect(270, 90, 171, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tagline2.setFont(font)
        self.tagline2.setStyleSheet("color: rgb(255, 255, 255);")
        self.tagline2.setObjectName("tagline2")

        self.tagline3 = QtWidgets.QLabel(self.centralwidget) #"Загрузил картинки"
        self.tagline3.setGeometry(QtCore.QRect(270, 130, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tagline3.setFont(font)
        self.tagline3.setStyleSheet("color: rgb(255, 255, 255);")
        self.tagline3.setObjectName("tagline3")

        self.button = QtWidgets.QPushButton(self.centralwidget) #кнопка "загрузить"
        self.button.setGeometry(QtCore.QRect(11, 446, 512, 46))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button.setFont(font)
        self.button.setStyleSheet("background-color: rgb(136,68,236);\n"
                                  "color: rgb(255, 255, 255);")
        self.button.setObjectName("button")

        self.button_folder = QtWidgets.QPushButton(self.centralwidget) #кнопка, вызывающая окно проводника для выбора папки
        self.button_folder.setGeometry(QtCore.QRect(219, 343, 301, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_folder.setFont(font)
        self.button_folder.setStyleSheet("background-color: rgb(255,255,255);\n"
                                         "color: rgb(0,0,0);")
        self.button_folder.setObjectName("button_folder")
        self.button_folder.clicked.connect(self.choice_folder)

        self.path = "" #путь до выбранной пользователем папки

        self.violetbackground3.raise_()
        self.blackbackground1.raise_()
        self.violetbackground1.raise_()
        self.name.raise_()
        self.text_link.raise_()
        self.logo.raise_()
        self.violetbackground2.raise_()
        self.text_folder.raise_()
        self.boardlink.raise_()
        self.createfolder.raise_()
        self.foldername.raise_()
        self.tagline1.raise_()
        self.tagline2.raise_()
        self.tagline3.raise_()
        self.button.raise_()
        self.button_folder.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "MainWindow"))
        self.name.setText(self._translate("MainWindow", "Pinloader"))
        self.text_link.setText(self._translate("MainWindow", "Вставьте ссылку на доску"))
        self.text_folder.setText(self._translate("MainWindow", "Выберите папку"))
        self.createfolder.setText(self._translate("MainWindow", "Создать папку"))
        self.tagline1.setText(self._translate("MainWindow", "Вставил ссылку"))
        self.tagline2.setText(self._translate("MainWindow", "Выбрал папку"))
        self.tagline3.setText(self._translate("MainWindow", "Загрузил картинки"))
        self.button.setText(self._translate("MainWindow", "Загрузить"))
        self.button_folder.setText(self._translate("MainWindow", "Выберите папку для загрузки"))

    def choice_folder(self): #Измнение текста, когда пользователь выбрал папку и сохранения пути до папки
        self.path = QFileDialog.getExistingDirectory(self.centralwidget, "Select a folder") #вызывает окно проводника и сохраняет полученный путь
        self.text_folder.setText(self._translate("MainWindow", "Изменить папку"))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.button_folder.setFont(font)
        self.button_folder.setText(self._translate("MainWindow", f"Сейчас выбрана\n{self.path}"))