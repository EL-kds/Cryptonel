import sys, os, importlib
from datetime import datetime
from csv import reader, writer
path_finder = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_finder)
#sys.path.append( '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data')
exchanges = ['Binance','Bitfinex','Bitstamp','Bittrex','CEX','Coinbase','Huobi','Kraken','Kucoin']
from Binance.Crypto_Price_V2 import Crypto_USD as binance
from Bitfinex.Crypto_Price_V2 import Crypto_USD as bitfinex
from Bitstamp.Crypto_Price_V2 import Crypto_USD as bitstamp
from Bittrex.Crypto_Price_V2 import Crypto_USD as bittrex
from CEX.Crypto_Price_V2 import Crypto_USD as cex
from Coinbase.Crypto_Price_V2 import Crypto_USD as coinbase
from Huobi.Crypto_Price_V2 import Crypto_USD as Huobi
from Kraken.Crypto_Price_V2 import Crypto_USD as Kraken
from Kucoin.Crypto_Price_V2 import Crypto_USD as Kucoin
import Price_Evaluation_V2
import Price_to_site
from apscheduler.schedulers.blocking import BlockingScheduler
from pathlib import Path

class price_1minute:
    def __init__(self):
        self.temp_Data_Output_File = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/temp Data.csv'
        self.crypto_folder_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/CryptoCurrencies/'

    def functCaller(self):
        self.date = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        
        binance().usd_Prices()
        bitfinex().usd_Prices()
        bitstamp()
        bittrex().usd_Prices()
        cex().usd_Prices()
        coinbase()
        Huobi().usd_Prices()
        Kraken()
        Kucoin().usd_Prices()
        self.price_eval_list = Price_Evaluation_V2.CrpyptoCoins().PriceAverage()
        self.crypto_Page_eval()
        Price_to_site.updateItems().Price_Evaluation()
    
    def crypto_Page_eval(self):
        
        self.crypto_list = Price_Evaluation_V2.crypto_coins
        
        for coins in self.crypto_list:
            self.coin_Price_Chart_file_path = self.crypto_folder_path+coins+'/Crypto Price Chart.csv'
            
            if Path(self.coin_Price_Chart_file_path).exists():
               pass
            else:
                open(self.coin_Price_Chart_file_path,'w')
            
            with open(self.coin_Price_Chart_file_path,'a') as file:
                csv_Writer = writer(file)
                for data in self.price_eval_list:
                    
                    if data[0] == coins:
                        Price = data[1]
                        MarketCap = data[2]
                        Volume = data[3]
                        Rank = data[4]
                        Diluted_MarketCap = data[5]
                        csv_Writer.writerow([self.date, Price, MarketCap, Volume, Rank, Diluted_MarketCap, data[0]])
        print('finish writing to files')



sched = BlockingScheduler()
# Schedule job_function to be called every two hours
sched.add_job(price_1minute().functCaller, 'interval', minutes= 1, start_date='2021-08-15 00:00:00')
sched.start()