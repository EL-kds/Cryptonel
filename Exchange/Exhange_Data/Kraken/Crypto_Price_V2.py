import requests
import csv
import time
CryptoPairs = {'XXBTZUSD':'BTC','XETHZUSD':'ETH','BNBUSD':"BNB",'BUSDUSD':'BUSD','BCHUSD':'BCH','ADAUSD':'ADA', 'LINKUSD':'LINK', 'ATOMUSD':'ATOM', 'CROUSD':'CRO',
 'XDGUSD':'DOGE', 'EOSUSD':'EOS','FTTUSD':'FTT', 'IOTUSD':'MIOTA', 'XLTCZUSD':'LTC', 'XXMRZUSD':'XMR', 'XEMUSD':'XEM', 'DOTUSD':'DOT', 'XXRPZUSD':'XRP', 'SOLUSD':'SOL', 'XXLMZUSD':'XML', 
 'USDTZUSD':'USDT', 'THETAUSD':'THETA', 'TRXUSD':'TRX','VETUSD':'VET', 'FILUSD':'FIL', 'SHIBUSD':'SHIB', 'USDCUSD':'USDC', 'MATICUSD':'MATIC', 'ETCUSD':'ETC', 'AXSUSD':'AXS',
 'ALGOUSD':'ALGO', 'XTZUSD':'XTZ', 'WAVESUSD':'WAVES', 'KSMUSD':'KSM', 'DASHUSD':'DASH'}


class Crypto_USD:
    def __init__(self):
        self.cryptoValue = []
        for crypto in CryptoPairs.keys():
            
            self.values = requests.get('https://api.kraken.com/0/public/Ticker?pair='+crypto)
            #print(self.values.json().get('result').get(crypto).get('a')[0])
            try:            
                self.cryptoPrice = str(self.values.json().get('result').get(crypto).get('a')[0])
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
                volume = str(self.values.json().get('result').get(crypto).get('v')[0])
                self.cryptoValue.append([CryptoPairs.get(crypto),crypto.upper(), str(self.cryptoPrice),volume])     
            except:
                print('404')
        print(self.cryptoValue)
        file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Kraken/Price Results.csv'
        with open(file_path, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['Coin', 'Name_Pair', 'Price', 'Volume'])
            for line in self.cryptoValue:
                csvWriter.writerow(line) 
                
