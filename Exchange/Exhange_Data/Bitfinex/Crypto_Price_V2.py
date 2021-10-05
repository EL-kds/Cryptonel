import requests
import csv
CryptoPairs = {'tBTCUSD':'BTC','tETHUSD':'ETH','BNBUSDT':'BNB','tBUSDUSD':'BUSD','tBCHN:USD':'BCH','tADAUSD':'ADA', 'tLINK:USD':'LINK', 'tATOMUSD':'ATOM',
 'CROUSDT':'CRO', 'tDOGE:USD':'DOGE', 'tEOSUSD':'EOS','tFTTUSD':'FTT', 'tIOTUSD':'MIOTA', 'tLTCUSD':'LTC', 'tXMRUSD':'XMR', 'tXEMUSD':'XEM', 'tDOTUSD':'DOT', 
 'tXRPUSD':'XRP', 'tSOLUSD':'SOL', 'tXLMUSD':'XLM', 'tTHETAUSD':'THETA','tTRXUSD':'TRX','tVETUSD':'VET', 'tFILUSD':'FIL','tUSTUSD':'USDT', 'tSHIBUSD':'SHIB',
 'tBSVUSD':'BSV', 'tUDCUSD':'USDC', 'tICPUSD':'ICP', 'tAVAX:USD':'AVAX', 'tETCUSD':'ETC', 'tNEOUSD':'NEO', 'tALGUSD':'ALGO', 'tXTZUSD':'XTZ', 'tLEOUSD':'LEO',
 'tBTTUSD':'BTT', 'tEGLD:USD':'EGLD', 'tWAVES:USD':'WAVES', 'tKSMUSD':'KSM', 'tNEAR:USD':'NEAR', 'tDCRUSD':'DCR', 'tTERRAUST:USD':'UST', 'tDSHUSD':'DASH'}

class Crypto_USD:
    def __init__(self):
        self.values = requests.get('https://api-pub.bitfinex.com/v2/tickers?symbols=ALL')
        
    def usd_Prices(self):
        self.cryptoValue = []
        for crypto in self.values.json():
            for pair in CryptoPairs.keys():
                if (crypto[0] == pair):
                    self.cryptoPrice = str(crypto[1])
                    """ priceCount = 0
                    for price in self.cryptoPrice: #find the price between tens hundreds and thousands
                        priceCount += 1 # to find the location of the period in the price
                        
                        if (price == '.' and priceCount == 6):# if price equal or over ten thosand put the comma in 
                            self.cryptoPrice = self.cryptoPrice[0:2]+','+self.cryptoPrice[2:8]
                            print(self.cryptoPrice)
                        elif(price == '.' and priceCount == 5):# if price over a thosand and below ten thosands put the comma in 
                            self.cryptoPrice = self.cryptoPrice[0]+','+self.cryptoPrice[1:7]
                            print(self.cryptoPrice)
                        elif(price == '.' and priceCount == 4):#if price equal to a hundred
                            self.cryptoPrice = self.cryptoPrice[0:6]
                            print(self.cryptoPrice)
                        elif(price == '.' and priceCount == 3):#if price equal to a hundred
                            self.cryptoPrice = self.cryptoPrice[0:5]
                            print(self.cryptoPrice) """
                    self.cryptoValue.append([CryptoPairs.get(pair),crypto[0], self.cryptoPrice, crypto[8]])  
        print(self.cryptoValue)
        file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Bitfinex/Price Results.csv'
        with open(file_path, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['Coin', 'Name_Pair', 'Price','volume'])
            for line in self.cryptoValue:
                csvWriter.writerow(line)
