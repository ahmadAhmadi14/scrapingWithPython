from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://shopee.co.id/search?keyword=hp').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'row shopee-search-item-result__items', dataclass_='item')
print(jobs)