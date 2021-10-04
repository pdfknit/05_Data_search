#1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
from pprint import pprint
import json

my_params = {
    'login': 'pdfknit',
    'per page': 10
}

url = "https://api.github.com/users/pdfknit/repos"


response = requests.get(url, params=my_params)
j_data = response.json()

with open('dz_01.txt', 'w') as f:
  json.dump(j_data, f, ensure_ascii=False, indent=4, sort_keys=True)
