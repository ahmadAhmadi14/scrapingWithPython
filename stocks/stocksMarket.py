import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd


def real_time_stocks(stocksCode):
    link_stocks = ('https://finance.yahoo.com/quote/') + stocksCode + ('?p=') + stocksCode + ('&.tsrc=fin-srch')
    url = requests.get(link_stocks)
    soup = BeautifulSoup(url.text, 'lxml')
    stock_content = soup.find('div', {"class": 'My(6px) Pos(r) smartphone_Mt(6px) W(100%)'})
    stock_content = stock_content.find('span').text
    
    if stock_content == []:
        stock_content = '99999'

    return stock_content


Index = ['META', 'AAPL', 'NFLX', 'GOOG']

for step in range(1,101):
    price = []
    col = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%M-%D %H:%M:%S")
    for stocksCode in Index:
        price.append(real_time_stocks(stocksCode))
    col = [time_stamp]
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('real time data to csv', mode='a', header=False)
    print(col)
