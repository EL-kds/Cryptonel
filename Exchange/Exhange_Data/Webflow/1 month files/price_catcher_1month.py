import sys, os, importlib
import time
path_finder = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_finder)
#sys.path.append( '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data')
exchanges = ['Binance','Bitfinex','Bitstamp','Bittrex','CEX','Coinbase','Huobi','Kraken','Kucoin']

import Price_Evaluation
import Price_to_site
from apscheduler.schedulers.blocking import BlockingScheduler

def functCaller():
    Price_Evaluation.CrpyptoCoins().Price_7day()
    

sched = BlockingScheduler()
# Schedule job_function to be called every two hours
sched.add_job(functCaller, 'interval', weeks = 4, start_date='2021-07-20 00:00:00')
sched.start()