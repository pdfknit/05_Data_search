# https://www.kinopoisk.ru/popular/films/?quick_filters=serials&tab=all
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = 'https://www.kinopoisk.ru'
params = {'quick_filters': 'serials',
          'tab': 'all',
          'page': 1}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

while True:
    response = requests.get(url + '/popular/films/', params=params, headers=headers)
    soup = bs(response.text, 'html.parser')

    serials_list = soup.find_all('div', attrs={'class': 'desktop-rating-selection-film-item'})
    # print(serials_list[0])
#     if not serials_list or not response.ok:
#         break
#     # print(serials_list[0])
#     serials = []
#
#     for serial in serials_list:
#         serial_data = {}
#         serial_info = serial.find('p', attrs={'class': 'selection-film-item-meta__name'})
#
#         serial_name = serial_info.text
#         serial_link = url + serial_info.parent['href']
#
#         serial_genre = serial.find('span', attrs={'class': 'selection-film-item-meta__meta-additional-item'}).next_sibling.text
#         serial_rating = serial.find('span', attrs={'class': 'rating__value'}).text
#         try:
#             serial_rating = float(serial_rating)
#         except:
#             serial_rating = None
#
#         serial_data['name'] = serial_name
#         serial_data['link'] = serial_link
#         serial_data['genre'] = serial_genre
#         serial_data['rating'] = serial_rating
#
#         serials.append(serial_data)
#     params['page'] += 1
#
# pprint(serials)