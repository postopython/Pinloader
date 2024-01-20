#!/usr/bin/python
# -*- coding: utf8 -*-


import os


def deleting_copy_files(hash_list: list, path: str):
    """
    удаление повторяющихся файлов
    :param hash_list: список хэшей всех файлов в папке
    :param path: путь до файлов
    :return: ошибки (None, если их нет)
    """
    try:
        os.chdir(path=path) #переход в директорию с картинками
        files = os.listdir() #получение списка с названиями всех файлов в папке
        for main_index, main_hash in enumerate(hash_list): #берёт хеш
            for second_index, second_hash in enumerate(hash_list): #проходится по всему списку
                if main_hash == second_hash and main_index != second_index: #Сравнивает первый хеш со вторым и их индексы, чтобы не сравнивать хеш с самим собой
                    os.remove(files[second_index]) #удаление файлов с одинаковым хешем
                    hash_list.pop(second_index) #удаление хеша из списка, иначе удалятся оба файла

        return None
    except Exception as ex:
        return ex
