import requests
import csv
import time
CryptoPairs = {'BTCUSD':'BTC','ETHUSD':'ETH','BNBUSD':'BNB','BUSDUSD':'BUSD','BCHUSD':'BCH','ADAUSD':'ADA','LINKUSD':'LINK', 'ATOMUSD':'ATOM', 'CROUSD':'CRO',
 'DOGEUSD':'DOGE', 'EOSUSD':'EOS', 'FTTUSD':'FTT','IOTUSD':'MIOTA', 'LTCUSD':'LTC','XMRUSD':'XMR', 'XEMUSD':'XEM', 'DOTUSD':'DOT', 'XRPUSD':'XRP','SOLUSD':'SOL', 
 'XLMUSD':'XLM', 'USDTUSD':'USDT', 'THETAUSD':'THETA', 'TRXUSD':'TRX', 'VETUSD':'VET', 'FILUSD':'FIL', 'SHIBUSD':'SHIB','USDCUSD':'USDC', 'MATICUSD':'MATIC',
 'ALGOUSD':'ALGO',}

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

class Crypto_USD:
    def __init__(self):
        self.cryptoValue = []
        for crypto in CryptoPairs.keys():
            
            self.values = requests.get('https://www.bitstamp.net/api/v2/ticker/'+crypto.lower())
            try:
                print(self.values.json(), crypto.lower())
                
                self.cryptoPrice = (self.values.json().get('last'))
                priceCount = 0
                """ for price in self.cryptoPrice: #find the price between tens hundreds and thousands
                    priceCount += 1 # to find the location of the period in the price
                    if (price == '.' and priceCount == 6):# if price equal or over ten thosand put the comma in 
                        self.cryptoPrice = self.cryptoPrice[0:2]+','+self.cryptoPrice[2:8]   
                    elif(price == '.' and priceCount == 5):# if price over a thosand and below ten thosands put the comma in 
                        self.cryptoPrice = self.cryptoPrice[0]+','+self.cryptoPrice[1:7]
                    elif(price == '.' and priceCount == 4):#if price equal to a hundred
                        self.cryptoPrice = self.cryptoPrice[0:6]
                    elif(price == '.' and priceCount == 3):#if price equal to a hundred
                        self.cryptoPrice = self.cryptoPrice[0:5] """
                self.cryptoValue.append([CryptoPairs.get(crypto),crypto.upper(), self.cryptoPrice, self.values.json().get('volume')])  
            except:
                print('404')
        print(self.cryptoValue)
        file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Bitstamp/Price Results.csv'
        with open(file_path, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['Coin', 'Name_Pair', 'Price', 'volume'])
            for line in self.cryptoValue:
                csvWriter.writerow(line)
