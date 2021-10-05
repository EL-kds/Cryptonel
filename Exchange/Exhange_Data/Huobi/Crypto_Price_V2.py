import requests
import csv
cryptoPairs = {'BTCUSDT':'BTC','ETHUSDT':'ETH','BNBUSDT':'BNB','BUSDUSDT':'BUSD','BCHUSDT':'BCH','ADAUSDT':'ADA', 'LINKUSDT':'LINK', 'ATOMUSDT':'ATOM', 'CROUSDT':'CRO', 'DOGEUSDT':'DOGE',
'EOSUSDT':'EOS','FTTUSDT':'FTT', 'IOTAUSDT':'MIOTA', 'LTCUSDT':'LTC', 'XMRUSDT':'XMR', 'XEMUSDT':'XEM', 'DOTUSDT':'DOT', 'XRPUSDT':'XRP', 'SOLUSDT':'SOL', 'XLMUSDT':'XLM', 'USDTHUSD':'USDT',
'THETAUSDT':'THETA', 'TRXUSDT':'TRX','VETUSDT':'VET', 'FILUSDT':'FIL', 'SHIBUSDT':'SHIB','BSVUSDT':'BSV', 'USDCUSDT':'USDC', 'MATICUSDT':'MATIC', 'ICPUSDT':'ICP', 'AVAXUSDT':'AVAX',
'ETCUSDT':'ETC', 'AXSUSDT':'AXS', 'NEOUSDT':'NEO', 'ALGOUSDT':'ALGO', 'XTZUSDT':'XTZ', 'BTTUSDT':'BTT', 'WAVESUSDT':'WAVES', 'KSMUSDT':'KSM', 'NEARUSDT':'NEAR', 'HBARUSDT':'HBAR',
'HTUSDT':'HT', 'DCRUSDT':'DCR', 'DASHUSDT':'DASH'}

class Crypto_USD:
    def __init__(self):
        self.values = requests.get('https://api.huobi.pro/market/tickers')
        
    
    def usd_Prices(self):
        self.cryptoValue = []
        for crypto in self.values.json().get('data'):
            for pair in cryptoPairs.keys():
                if (crypto.get('symbol') == pair.lower()):
                    self.cryptoPrice = str(crypto.get('close'))
                    if crypto.get('symbol') == 'SHIBUSDT'.lower():
                        self.cryptoPrice = "{:,.8f}".format(float(self.cryptoPrice))
                    self.cryptoValue.append([cryptoPairs.get(pair),crypto.get('symbol'), self.cryptoPrice, 0])  
        print(self.cryptoValue)
        file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Huobi/Price Results.csv'
        with open(file_path, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['Coin', 'Name_Pair', 'Price','Volume'])
            for line in self.cryptoValue:
                csvWriter.writerow(line)
