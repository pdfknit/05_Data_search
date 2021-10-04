# Необходимо собрать информацию по продуктам питания с сайта:
# Список протестированных продуктов на сайте Росконтроль.рф
# Приложение должно анализировать несколько страниц сайта (вводим через input или аргументы).
# Получившийся список должен содержать:
#
# Наимеонвание продукта.
# Все параметры (Безопасность, Натуральность, Пищевая ценность, Качество) Не забываем преобразовать к цифрам
# Общую оценку
# Сайт, откуда получена информация.

import json
import requests
from bs4 import BeautifulSoup as bs

url = 'https://roscontrol.com/category/produkti/'
pages = ['molochnie_produkti/kefir/', 'myasnie_produkti/kolbasa/', 'riba_i_moreprodukti/solenaya_riba/']
params = {'page': 1}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
product_data = {}
for product_type in range(0, len(pages)):
    response = requests.get(url + pages[product_type], params=params, headers=headers)
    soup = bs(response.text, 'html.parser')
    pagination = soup.find('div', attrs={'class': 'page-pagination'})

    # print(soup)

    product_name_list = soup.find_all('div', attrs={'class': 'product__item-link'})
    # print(product_name_list[0].text)

    product_list = soup.find_all('div', attrs={'class': 'wrap-product-catalog__item'})
    # print(product_list[0])

    for product in product_list:
        parameters_list = {}
        product_name = product.find('div', attrs={'class': 'product__item-link'})
        # print(product_name.text)
        parameters_list['Название'] = product_name.text
        black_list = product.find('div', attrs={'class': 'blacklist-value'})

        if not black_list:

            parameters = product.find_all('div', attrs={'class': 'text'})
            param_count = product.find_all('div', attrs={'class': 'right'})

            for name, count in zip(parameters, param_count):
                name.find('div', attrs={'class': 'text'})
                # print(name.text)

                count.find('div', attrs={'class': 'text'})
                # print(count.text)
                try:
                    int_count = int(count.text)
                except:
                    int_count = 0
                parameters_list[name.text] = int_count

            rating = product.find('div', attrs={'class': 'rate'})
            try:
                print('rate =', rating.text)
                parameters_list['Общая оценка'] = rating.text
            except:
                print('rate = 0')
        else:
            parameters_list['black list'] = True

        link = url + product.find_all('a')[0].attrs['href']
        # print('link =', link)
        parameters_list['link'] = link
        print(parameters_list)


        # for name, result in zip (safety, safety_count):

        # print(dict(zip(safety, safety_count)))

