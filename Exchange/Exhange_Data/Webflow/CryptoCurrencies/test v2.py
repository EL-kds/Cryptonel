from datetime import datetime, timedelta
import dateutil.parser
from dateutil import parser
import pandas as pd
import csv


file = '/home/ubuntu/Cryptonel/Exchange/Exhange_Data/CryptoCurrencies/BTC/Crypto Price Chart.csv'

date = datetime.now()
data_time = dateutil.parser.parse('2021-08-19-16:10:30')
data_time2 = dateutil.parser.parse('2021-08-19-16:09:30')
then = timedelta(days=19)
test_date = data_time - data_time2

if test_date == timedelta(minutes=1):
    print(test_date)

with open(file,'r') as f:
    read = csv.reader(f)
    print(next(read))
    
