import requests
import csv
import time
CryptoPairs = {'BTC-USD':'BTC','ETH-USD':'ETH','BNB-USD':'BNB','BUSD-USD':'BUSD','BCH-USD':'BCH','ADA-USD':'ADA','LINK-USD':'LINK', 'ATOM-USD':'ATOM', 'CRO-USD':'CRO',
 'DOGE-USD':'DOGE', 'EOS-USD':'EOS', 'FTT-USD':'FTT','IOTA-USD':'MIOTA', 'LTC-USD':'LTC','XMR-USD':'XMR', 'XEM-USD':'XEM', 'DOT-USD':'DOT', 'XRP-USD':'XRP','SOL-USD':'SOL', 
 'XLM-USD':'XLM', 'USDT-USD':'USDT', 'THETA-USD':'THETA', 'TRX-USD':'TRX', 'VET-USD':'VET', 'FIL-USD':'FIL', 'SHIB-USD':'SHIB', 'USDT-USDC':'USDC','MATIC-USD':'MATIC',
 'ICP-USD':'ICP','ETC-USD':'ETC','AXS-USD':'AXS', 'ALGO-USD':'ALGO', 'XTZ-USD':'XTZ', 'AMP-USD':'AMP', 'UST-USD':'UST', 'DASH-USD':'DASH'}


class Crypto_USD:
    def __init__(self):
        self.cryptoValue = []
        for crypto in CryptoPairs.keys():
            
            self.values = requests.get('https://api.pro.coinbase.com/products/'+crypto+"/ticker")
            try:
                if self.values.json().get('message') == 'NotFound':
                    continue
                print(self.values.json(), crypto.lower())
                
                self.cryptoPrice = str(self.values.json().get('price'))
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
                self.cryptoValue.append([CryptoPairs.get(crypto),crypto.upper(), self.cryptoPrice, self.values.json().get('volume')])  
            except:
                print('404')
        print(self.cryptoValue)
        file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Coinbase/Price Results.csv'
        with open(file_path, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['Coin', 'Name_Pair', 'Price','Volume'])
            for line in self.cryptoValue:
                csvWriter.writerow(line)
