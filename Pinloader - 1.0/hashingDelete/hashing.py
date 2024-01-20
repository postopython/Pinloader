#!/usr/bin/python
# -*- coding: utf8 -*-

import hashlib
import os


def create_hash(path: str):
    """
    создаёт список с хеш-кодами всех файлов в указанной папке
    :param path: путь до папки
    :return: список хеш-кодов, ошибки (None, если их нет)
    """
    try:
        hash_list = []
        os.chdir(path=path)
        files = os.listdir() #код из интернета
        for filename in files:
            with open(filename, 'rb') as file:
                meta = hashlib.md5()
                while True:
                    data = file.read(8192)
                    if not data:
                        break
                    meta.update(data)
                hash_list.append(meta.hexdigest())
        return hash_list, None

    except Exception as ex:
        return None, ex
