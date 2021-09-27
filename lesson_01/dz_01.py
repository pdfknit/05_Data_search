#1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.

import requests
from pprint import pprint
city = 'moscow'
my_params = {
    'login': 'pdfknit',

}

url = "https://api.github.com/users/defunkt"

for i in range(500):
    response = requests.get(url, params=my_params)
    j_data = response.json()
    pprint(f'Р’ РіРѕСЂРѕРґРµ {j_data.get("name")} + {i} С‚РµРјРїРµСЂР°С‚СѓСЂР° {j_data.get("main").get("temp") - 273.15} РіСЂР°РґСѓСЃРѕРІ')



