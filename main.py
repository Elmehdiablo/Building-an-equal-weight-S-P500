#Importing libraries

import numpy as np
import pandas as pd
import math 
import requests 
import xlsxwriter
from secrets import IEX_CLOUD_API_TOKEN




# Let's get the informations from the Cust



# Let's import our stocks from the csv file

stocks = pd.read_csv("S&P500.csv")

#Let's creat the Datframe]
my_columns = ['Symbol','Stockprice','MarketCap','Numbers of Shares to buy']
final_dataframe = pd.DataFrame(columns=my_columns)

#Let's make a full string of stocks for our bunch call
def chunk(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]
lst_of_stocks = [stock for stock in stocks['Symbol']]
devide_list_of_stocks = list(chunk(lst_of_stocks, 100))   
devide_list_of_stocks.pop()
strings_list = []
for i in range(0,len(devide_list_of_stocks)):
    strings_list.append(','.join(devide_list_of_stocks[i]))
for string_list in strings_list[:1]:
    bach_url_api = f'https://cloud.iexapis.com/stable/stock/market/batch?symbols={string_list}&types=quote&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(bach_url_api).json()
    for symbol in lst_of_stocks:
        try:
           final_dataframe = final_dataframe.append(
             pd.Series(
                  [
                     symbol,
                     data[symbol]['quote']['latestPrice'],
                     data[symbol]['quote']['marketCap'],
                     'N/A'
                  ],index=my_columns
             ),ignore_index=True
            )
        except KeyError:
            pass  
amount_money = input("Hello ! Please enter your porfolio Size :  ")

try:
    val = float(amount_money)
except ValueError:
    print("Please enter an integer number ! ")
    amount_money = input("Hello ! Please enter your porfolio Size :  ")
    val = float(amount_money)          
porfolio_size = val/int(len(final_dataframe))
for i in range(len(final_dataframe.index)):
    final_dataframe.loc[i,'Numbers of Shares to buy']= math.floor(porfolio_size/final_dataframe.loc[i,'Stockprice'])
print(final_dataframe)

#Let's make a bunch requests 


#Let's add the stocks to our Dataframe

#for stock in stocks['Symbol']:


