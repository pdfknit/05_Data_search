# 2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

import requests

my_params = {
    'ID': '',
    'Password': ''
}

url = "http://api.yandex.com/direct/"

response = requests.get(url, params=my_params)
print(response.status_code)
