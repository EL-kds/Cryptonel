import sys, os, importlib
import time
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
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
while True:
    binance().usd_Prices()
    bitfinex().usd_Prices()
    bitstamp()
    bittrex().usd_Prices()
    cex().usd_Prices()
    coinbase()
    Huobi().usd_Prices()
    Kraken()
    Kucoin().usd_Prices() 
    countdown(60)