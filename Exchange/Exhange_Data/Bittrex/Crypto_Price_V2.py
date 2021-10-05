import requests
import csv
CryptoPairs = {'USD-BTC':'BTC','USD-ETH':'ETH','BNBUSDT':'BNB','BUSDUSDT':'BUSD','USD-BCH':'BCH','USD-ADA':'ADA', 'USD-LINK':'LINK', 'USD-ATOM':'ATOM', 'USD-CRO':'CRO',
 'USD-DOGE':'DOGE', 'USD-EOS':'EOS', 'FTTUSDT':'FTT', 'USD-IOTA':'MIOTA', 'USD-LTC':'LTC', 'XMRUSDT':'XMR', 'USD-XEM':'XEM', 'USD-DOT':'DOT', 'USD-XRP':'XRP', 'SOLUSDT':'SOL',
 'USD-XLM':'XLM', 'THETAUSDT':'THETA', 'USD-TRX':'TRX', 'VETUSDT':'VET', 'USD-FIL':'FIL','USD-USDT':'USDT', 'SHIBUSDT':'SHIB', 'USD-USDC':'USDC', 'USD-MATIC':'MATIC',
 'USDT-AVAX':'AVAX', 'USDT-ETC':'ETC', 'USDT-KLAY':'KLAY', 'USDT-NEO':'NEO', 'USD-ALGO':'ALGO', 'USDT-XTZ':'XTZ', 'USDT-BTT':'BTT', 'USDT-WAVES':'WAVES', 'USDT-KSM':'KSM',
 'USDT-AMP':'APM', 'USDT-HBAR':'HBAR', 'USD-DCR':'DCR', 'USDT-UST':'UST',}

class Crypto_USD:
    def __init__(self):
        self.values = requests.get('https://api.bittrex.com/api/v1.1/public/getmarketsummaries')
       
    
    def usd_Prices(self):
        self.cryptoValue = []
        for crypto in self.values.json().get('result'):
            for pair in CryptoPairs.keys():
                if (crypto.get('MarketName') == pair):
                    self.cryptoPrice = str(crypto.get('Last'))
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
                    self.cryptoValue.append([CryptoPairs.get(pair),crypto.get('MarketName'), self.cryptoPrice, crypto.get('Volume')])  
        print(self.cryptoValue)
        file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Bittrex/Price Results.csv'
        with open(file_path, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['Coin', 'Name_Pair', 'Price','Volume'])
            for line in self.cryptoValue:
                csvWriter.writerow(line)
