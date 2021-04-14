import bs4
from bs4 import BeautifulSoup
import requests
from alpha_vantage.timeseries import TimeSeries
import yfinance as yf
import lxml
from urllib.request import urlopen
import re
import pandas as pd
import numpy as np
import time



def main():
    key="H7DNZEX9GXEBBFER"
    ts = TimeSeries(key)
    aapl,meta = ts.get_daily(symbol="MSFT")
    data_=aapl["2021-04-13"]
    print(data_)
    url="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
    response=requests.get(url)
    data=pd.DataFrame(response.json())
    print(data)
    data.to_csv('pars.csv')
#----------------------------------------------------

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
    r = requests.get('https://finance.yahoo.com/quote/MSFT/profile?p=MSFT', headers=headers)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    print()
    name=str(soup.find_all("h3","Fz(m) Mb(10px)"))
    addrres=str(soup.find_all("p","D(ib) W(47.727%) Pend(40px)"))
    workers=str(soup.find_all("span", "Fw(600)"))

    sumbol_1 = addrres.find("13 -->")
    sumbol_2 = "<!-- /react-text"
    sumbol_3 = workers.find('"30">')
    sumbol_4 = "<!-- /react-text"

    addrres = addrres[sumbol_1 + 6:]
    addrres = addrres.split(sumbol_2,1)[0]

    workers= workers[sumbol_3 +5 :-15]

    print("Name:",name[45:-6])
    print("Address:", addrres)
    print("Amount of workers:", workers)



if __name__ == '__main__':
    while True:
        main()
        time.sleep(300)#Запуск каждые 5 мин