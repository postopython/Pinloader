# -*- coding: utf-8 -*-

import downloadImages
import hashingDelete
import logFile
import requstProcessing
import UI
import os
import sys
from PySide2 import QtWidgets




def show_dialog(title, text, size):
    """
    показывает диалоговое окно
    :param title: заголовок окна
    :param text: текст в окне
    :param size: размер шрифта
    :return: ничего
    """
    global Dialog #иначе окно открывается и сразу же закрывается
    Dialog = QtWidgets.QDialog()
    ui = UI.Ui_Dialog()
    ui.setupUi(Dialog, window_title=title, text=text, font_size=size)
    Dialog.show()


def inputdata_processing(ui):
    """
    извлекает из окна информацию и передаёт данные в функцию backend()
    :param ui: класс окна
    :return: ничего
    """
    link = ui.boardlink.text() #ссылка на доску из поля для вводв
    path = ui.path #чтобы было удобнее обращаться и спокойно менять
    if path == "" or link == "": #если пользователь оставил пустым одно из обязательных полей
        show_dialog("Ошибка ввода", "Не указана ссылка\nили папка", 16)
    else:
        if ui.createfolder.isChecked(): #если пользователь нажал чекбокс "Создать папку"
            os.chdir(path)
            foldername = ui.foldername.text()
            if not os.path.isdir(foldername): #если такой папки нет
                os.mkdir(foldername)
                path += f"/{foldername}"
                show_dialog("Запуск программы", "Программа\nуспешно\nзапущена", 24)
                backend(url=link, path=path) #вызов основной функции
            else:
                show_dialog("Файловая ошибка", "Такая папка уже\nсуществует. Укажите\nдругое название папки в\nстроке создания папки", 12) #окно с ошибкой
        else:
            show_dialog("Запуск программы", "Программа\nуспешно\nзапущена", 24)
            backend(url=link, path=path) #вызов основной функции


def frontend():
    """
    открывает окно
    :return: ничего
    """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.button.clicked.connect(lambda: inputdata_processing(ui=ui)) #привязывет кнопку к функции inputdata_processing()
    sys.exit(app.exec_())


def backend(url: str, path: str):
    responce, code = requstProcessing.get_request(url=url) #запрос на сервер
    if code == 200: #если ответ корректен
        errors = []
        count, error = requstProcessing.pinCount(response=responce)
        errors.append(error)
        ID, error = requstProcessing.boardID(response=responce)
        errors.append(error)
        user_board = downloadImages.board(url=url, pinCount=count, ID=ID)
        errors.append(error)
        links = user_board.pin_url_list()
        errors.append(error)
        error = downloadImages.image_download(links=links, path=path)
        errors.append(error)
        hashs, error = hashingDelete.create_hash(path=path)
        errors.append(error)
        error = hashingDelete.deleting_copy_files(hash_list=hashs, path=path)
        errors.append(error)
        logFile.write_logs(url=url, request_code=code, board_id=ID, pin_count=count, result=links, errors=errors)
        show_dialog("Успешно", "Программа\nзавершила\nработу", 24)

    else:
        logFile.write_logs(url=url, request_code=code, board_id=None, pin_count=None, result=None, errors=["server error"])
        show_dialog("Серверная ошибка", "Произошла ошибка\nпри попытке\nподключения к серверу", 12)

if __name__ == "__main__":
    frontend()