from bs4 import BeautifulSoup


def boardID(response: str):
    """
    извлекает ID доски пользователя из ответа сервера
    :param response: ответ от сервера
    :return: ID доски пользователя, ошибки (None, если их нет)
    """
    try:
        soup = BeautifulSoup(response, "html.parser")
        board_source = soup.find("script", id="__PWS_DATA__").text
        board_source_list = board_source.split(",") #структура этой части ответа похожа на json, поэтому мы делаем список с параметрами
        board_id = None
        for value in board_source_list:
            value_list = value.split(":") #так как структура-это json, то мы получаем список [ключ, значение]
            if value_list[0] == '"boards"':
                board_id = value_list[1][2:][:-1] #очищает от лишнего, так как там не только id

        return board_id, None
    except Exception as ex:
        return None, ex

def pinCount(response: str):
    """
       извлекает количество пинов в доске пользователя из ответа сервера
       :param response: ответ от сервера
       :return: ID доски пользователя, ошибки (None, если их нет)
       """
    try:
        soup = BeautifulSoup(response, "html.parser")
        response_source = soup.find("div", class_="FNs zI7 iyn Hsu")
        if response_source is not None:
            pin_count = response_source.text[:-8]
            return pin_count, None
        else:
            return None, "No such class name"
    except Exception as ex:
        return None, ex