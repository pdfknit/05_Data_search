import requests
from bs4 import BeautifulSoup as bs

url = 'http://www.google.ru'

response = requests.get(url)
soup = bs(response.text, 'html.parser')

print(response)