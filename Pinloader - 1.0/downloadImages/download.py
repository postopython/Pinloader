import requests


class board():
    """Доска пользователя в pinterest"""
    def __init__(self, url, pinCount, ID):
        """
        :param url: ссылка на доску
        :param pinCount: количество пинов в доске
        :param ID: ID доски
        """
        self.url = url
        self.pinCount = pinCount
        self.ID = ID

    def pin_url_list(self):
        """
        собирает ссылки на изображения
        :return: список ссылок
        """
        #данные для запроса
        headers = {
            'accept': 'application/json, text/javascript, */*, q=0.01',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'authority': 'ru.pinterest.com',
            'referer': 'https://ru.pinterest.com/',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.71", "Google Chrome";v="120.0.6099.71"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'x-app-version': '03339f0',
            'x-pinterest-appstate': 'background',
            'x-pinterest-pws-handler': 'www/[username]/[slug].js',
            'x-pinterest-source-url': '/AllChai_/%D0%B1%D0%B0%D0%BB%D1%8C%D0%B7%D0%B0%D0%BC-%D0%BD%D0%B0-%D0%B4%D1%83%D1%88%D1%83/',
            'x-requested-with': 'XMLHttpRequest',
        }
        if self.pinCount is not None:
            if int(self.pinCount) < 250: #этот запрос не может выдавать более 250 файлов. При вводе большего значения выдаёт ошибку
                pin_count_corrected = self.pinCount
            else:
                pin_count_corrected = 250
            params = {
                'source_url': self.url,
                'data': '{"options":{"board_id":"' + self.ID + '",'
                        '"board_url":"https://ru.pinterest.com/AllChai_/dreamcore/",'
                        '"field_set_key":"react_grid_pin","filter_section_pins":true,"sort":"default","layout":"default",'
                        '"page_size":' + str(pin_count_corrected) + ',"redux_normalize_feed":true}}'
            }
            #отправка запроса
            response = requests.get('https://ru.pinterest.com/resource/BoardFeedResource/get', params=params, headers=headers).text
            response_list = response.split(",") #полученный файл по структуре является json файлом, поэтому здест он делится на параметры
            pin_list = []
            for value in response_list:
                listed = value.split(":") #полученный список является [ключ, значение]
                if '"url"' in listed and len(listed) > 2:
                    url = "https:" + listed[2][:-2]
                    listed_url = url.split("/")
                    if "originals" in listed_url:
                        pin_list.append(url[:-1])

            return pin_list
        else:
            return None


def image_download(links: list, path: str):
    """
    скачивает изображения
    :param links: список ссылок. Получается из метода pin_url_list у класса board
    :param path: путь, куда файлы скачаются
    :return: ошибки (None, если их нет)
    """
    try:
        image_count = 0
        format_list = []
        for link in links:
            image_format = link[73:] #все ссылки одной длинны. Сделано из-за формата .webp, который длинее .png .jpg
            format_list.append(image_format)
            images_bytes = requests.get(link).content
            with open(f'{path}/{image_count}.{image_format}', 'wb') as file:
                file.write(images_bytes)

            image_count += 1 #На выходе файлы именются, как 0.png, 1.jpg, 2.webp и так далее
        return None
    except Exception as ex:
        return ex
