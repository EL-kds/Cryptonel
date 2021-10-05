import requests
import csv
cryptoPairs = {'BTCUSDT':'BTC','ETHUSDT':'ETH','BNBUSDT':'BNB','BUSDUSDT':'BUSD','BCHUSDT':'BCH','ADAUSDT':'ADA', 'LINKUSDT':'LINK', 'ATOMUSDT':'ATOM', 'CROUSDT':'CRO', 'DOGEUSDT':'DOGE',
 'EOSUSDT':'EOS','FTTUSDT':'FTT', 'IOTAUSDT':'MIOTA', 'LTCUSDT':'LTC', 'XMRUSDT':'XMR', 'XEMUSDT':'XEM', 'DOTUSDT':'DOT', 'XRPUSDT':'XRP', 'SOLUSDT':'SOL', 'XLMUSDT':'XLM', 'USDTUSD':'USDT', 
 'THETAUSDT':'THETA', 'TRXUSDT':'TRX', 'VETUSDT':'VET', 'FILUSDT':'FIL', 'SHIBUSDT':'SHIB', 'USDCUSDT':'USDC', 'MATICUSDT':'MATIC', 'ICPUSDT':'ICP', 'AVAXUSDT': 'AVAX', 'ETCUSDT':'ETC',
 'AXSUSDT':'AXS', 'KLAYUSDT':'KLAY', 'NEOUSDT':'NEO', 'ALGOUSDT':'ALGO','XTZUSDT':'XTZ', 'BTTUSDT':'BTT', 'EGLDUSDT':'EGLD', 'WAVESUSDT':'WAVES', 'KSMUSDT':'KSM', 'NEARUSDT':'NEAR',
 'HBARUSDT':'HBAR', 'DCRUSDT':'DCR', 'DASHUSDT':'DASH'}

class Crypto_USD:
    def __init__(self):
        self.values = requests.get ('https://api1.binance.com/api/v3/ticker/24hr')
    
    def usd_Prices(self):
        self.cryptoValue = []
        for crypto in self.values.json():
            for pair in cryptoPairs.keys():
                if (crypto.get('symbol') == pair):
                    self.cryptoPrice = str(crypto.get('lastPrice'))
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
                    self.cryptoValue.append([cryptoPairs.get(pair),crypto.get('symbol'), self.cryptoPrice, crypto.get('volume')])  
        print(self.cryptoValue)
        file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Binance/Price Results.csv'
        with open(file_path, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['Coin', 'Name_Pair', 'Price','Volume'])
            for line in self.cryptoValue:
                csvWriter.writerow(line)
        print('finish')
