import requests
import csv
CryptoPairs = {'BTC-USDT':'BTC','ETH-USDT':'ETH','BNB-USDT':'BNB','BUSD-USDT':'BUSD','BCH-USDT':'BCH','ADA-USDT':'ADA','LINK-USDT':'LINK', 'ATOM-USDT':'ATOM', 'CRO-USDT':'CRO',
 'DOGE-USDT':'DOGE', 'EOS-USDT':'EOS', 'FTT-USDT':'FTT','IOTA-USDT':'MIOTA', 'LTC-USDT':'LTC','XMR-USDT':'XMR', 'XEM-USDT':'XEM', 'DOT-USDT':'DOT', 'XRP-USDT':'XRP','SOL-USDT':'SOL', 
 'XLM-USDT':'XLM', 'USDT-USDC':'USDT', 'THETA-USDT':'THETA', 'TRX-USDT':'TRX', 'VET-USDT':'VET', 'FIL-USDT':'FIL', 'SHIB-USDT':'SHIB','BSV-USDT':'BSV', 'USDC-USDT':'USDC', 
 'MATIC-USDT': 'MATIC', 'ICP-USDT':'ICP', 'AVAX-USDT':'AVAX', 'ETC-USDT':'ETC', 'AXS-USDT':'AXS','NEO-USDT':'NEO','ALGO-USDT':'ALGO', 'XTZ-USDT':'XTZ', 'BTT-USDT':'BTT', 
 'WAVES-USDT':'WAVES', 'KSM-USDT':'KSM', 'NEAR-USDT':'NEAR', 'USDC-UST':'UST', 'DASH-USDT':'DASH'}

class Crypto_USD:
    def __init__(self):
        self.values = requests.get('https://openapi-v2.kucoin.com/api/v1/market/allTickers')
        
    
    def usd_Prices(self):
        self.cryptoValue = []
        for crypto in self.values.json().get('data').get('ticker'):
            for pair in CryptoPairs.keys():
                if (crypto.get('symbol') == pair):
                    self.cryptoPrice = str(crypto.get('last'))
                    """ priceCount = 0
                    for price in self.cryptoPrice: #find the price between tens hundreds and thousands
                        priceCount += 1 # to find the location of the period in the price
                        if (price == '.' and priceCount == 6):# if price equal or over ten thosand put the comma in 
                            self.cryptoPrice = self.cryptoPrice[0:2]+','+self.cryptoPrice[2:8]    
                        elif(price == '.' and priceCount == 5):# if price over a thosand and below ten thosands put the comma in 
                            self.cryptoPrice = self.cryptoPrice[0]+','+self.cryptoPrice[1:7]
                        elif(price == '.' and priceCount == 4):#if price equal to a hundred
                            self.cryptoPrice = self.cryptoPrice[0:6]
                        elif(price == '.' and priceCount == 3):#if price equal to a hundred
                            self.cryptoPrice = self.cryptoPrice[0:5] """
                    self.cryptoValue.append([CryptoPairs.get(pair),crypto.get('symbol'), self.cryptoPrice, crypto.get('vol')])  
        print(self.cryptoValue)
        file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Kucoin/Price Results.csv'
        with open(file_path, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['Coin', 'Name_Pair', 'Price','Volume'])
            for line in self.cryptoValue:
                csvWriter.writerow(line)
