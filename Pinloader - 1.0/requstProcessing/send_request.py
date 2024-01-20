import requests


def get_request(url: str):
    """
    отправляет запрос на сервер
    :param url: url доски
    :return: ответ от сайта, код соединения
    """
    payload = ""
    headers = {
        "User-Agent": "insomnia/8.4.5"
    }
    responce = requests.request("GET", url, data=payload, headers=headers)
    code = responce.status_code

    return responce.text, code

