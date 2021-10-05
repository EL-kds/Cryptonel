import requests
import csv
CryptoPairs = {'BTC:USD':'BTC','ETH:USD':'ETH','BNB:USD':'BNB','BUSD:USD':'BUSD','BCH:USD':'BCH','ADA:USD':'ADA', 'LINK:USD':'LINK', 'ATOM:USD':'ATOM',
 'CRO:USD':'CRO','DOGE:USD':'DOGE', 'EOS:USD':'EOS','FTT:USD':'FTT', 'IOTA:USD':'MIOTA', 'LTC:USD':'LTC', 'XMR:USD':'XMR', 'XEM:USD':'XEM', 'DOT:USD':'DOT', 
 'XRP:USD':'XRP', 'SOL:USD':'SOL', 'XLM:USD':'XLM', 'USDT:USD':'USDT', 'THETA:USD':'THETA', 'TRX:USD':'TRX','VET:USD':'VET', 'FIL:USD':'FIL', 'SHIB:USD':'SHIB',
 'USDC:USD':'USDC', 'MATIC:USD': 'MATIC', 'ICP:USD':'ICP', 'NEO:USD':'NEO', 'XTZ:USD':'XTZ', 'BTT:USD':'BTT', 'KSM:USD':'KSM', 'DASH:USD':'DASH'}

class Crypto_USD:
    def __init__(self):
        self.values = requests.get('https://cex.io/api/tickers/USD')
        
    
    def usd_Prices(self):
        self.cryptoValue = []
        for crypto in self.values.json().get('data'):
            for pair in CryptoPairs.keys():
                if (crypto.get('pair') == pair):
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
                    self.cryptoValue.append([CryptoPairs.get(pair),crypto.get('pair'), self.cryptoPrice, crypto.get('volume')])
        print(self.cryptoValue)
        file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/CEX/Price Results.csv'
        with open(file_path, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['Coin', 'Name_Pair', 'Price','Volume'])
            for line in self.cryptoValue:
                csvWriter.writerow(line)
