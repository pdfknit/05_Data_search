import requests
from bs4 import BeautifulSoup as bs

url = 'http://www.google.ru'

response = requests.get(url)
soup = bs(response.text, 'html.parser')

tag_a = soup.find('a')
div_d = soup.find('div', attrs={'id': 'd'}) #кладем аттрибуты внутри, id, class, href...
all_p = div_d.findChildren(recursive=False)
select_p = soup.find_all('p', attrs={'class': 'red'})
print(response)