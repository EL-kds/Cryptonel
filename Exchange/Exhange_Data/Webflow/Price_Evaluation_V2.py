import csv
import requests
exchanges = ['Binance','Bitfinex','Bitstamp','Bittrex','CEX','Coinbase','Huobi','Kraken','Kucoin']
crypto_coins = ['BTC', 'ETH','BNB','BSV','BUSD','BCH','ADA','LINK','ATOM','CRO','DOGE','EOS','FTT','MIOTA',
'LTC','XMR','XEM','DOT','XRP','SOL','XLM','USDT','THETA','TRX','VET','FIL','SHIB','USDC','MATIC','ICP','AVAX',
'ETC','AXS','KLAY', 'NEO','ALGO', 'XTZ', 'LEO', 'BTT', 'EGLD', 'WAVES', 'KSM', 'NEAR', 'AMP', 'HBAR', 'HT', 'DCR',
'UST', 'DASH', 'QNT'] 
print(len(crypto_coins))
Crypto_data = []
class CrpyptoCoins:
    def __init__(self):
        self.value = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    
    def PriceAverage(self):
        self.cryptoValue = []
        self.exchange_Data = {}
        for coin in crypto_coins:
            self.average_Price = 0
            self.volume = 0
            self.price_Addition = 0
            self.volume_Addition = 0
            self.count = 0
            self.marketCap = 0
            self.tempData = []
            for exchange in exchanges:
                self.file_Path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/'+exchange+'/Price Results.csv'
                with open(self.file_Path, 'r') as file:
                    self.csvReader = csv.reader(file)
                    next(self.csvReader)
                    
                    for line in self.csvReader:
                        
                        if line[0] == coin:
                            self.tempData.append( {exchange:[line[2],line[3]]})
                            self.count += 1
                            self.price_Addition = self.price_Addition+float(line[2])
                            self.volume_Addition = self.volume_Addition + float(line[3])
            self.exchange_Data[coin] = self.tempData
            if self.price_Addition == 0: 
                continue      
            elif  self.price_Addition > 0:    
                self.average_Price = self.price_Addition / self.count
                self.volume =  "{:,.0f}".format(self.volume_Addition * self.average_Price)
                if coin == 'SHIB':
                    self.average_Price = "{:,.8f}".format(self.average_Price)
                priceCount = 0
                self.string_price = str(self.average_Price)
                for price in self.string_price: #find the price between tens hundreds and thousands
                    priceCount += 1 # to find the location of the period in the price
                    if (price == '.' and priceCount == 6):# if price equal or over ten thosand put the comma in 
                        self.average_Price = self.string_price[0:2]+','+self.string_price[2:8]    
                    elif(price == '.' and priceCount == 5):# if price over a thosand and below ten thosands put the comma in 
                        self.average_Price = self.string_price[0]+','+self.string_price[1:7]
                    elif(price == '.' and priceCount == 4):#if price equal to a hundred
                        self.average_Price = self.string_price[0:6]
                    elif(price == '.' and priceCount == 3):#if price equal to a tens
                        self.average_Price = self.string_price[0:5]
                    elif(price =='.' and priceCount ==2 and int(self.string_price[0])>0):#if price less than north
                        self.average_Price = self.string_price[0:4]
                    elif(price =='.' and priceCount ==2 and len(self.string_price)>7):#if price less than north
                        if coin == 'SHIB':
                            self.average_Price = self.string_price[0:10]
                        else:
                            self.average_Price = self.string_price[0:7]
                    elif(price == '.' and priceCount > 6):
                        self.average_Price = "{:,.2f}".format(self.string_price)

                for crypto in self.value.json():
                    
                    if crypto.get('symbol') == coin.lower():  
                        self.marketCap = "{:,.0f}".format(self.price_Addition /self.count * crypto.get('circulating_supply'))
                        self.rank_Marketcap = self.price_Addition /self.count * crypto.get('circulating_supply')
                        if crypto.get('total_supply') == None:
                            self.diluted_MarketCap = self.marketCap
                        else:
                            self.diluted_MarketCap = "{:,.0f}".format(self.price_Addition /self.count * float(crypto.get('total_supply')))
                            
                self.cryptoValue.append([coin, self.average_Price,self.marketCap, self.volume, self.rank_Marketcap,self.diluted_MarketCap])
                
            self.file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/Crypto Price.csv'
            with open(self.file_path, 'w') as newFile:
                csvWriter = csv.writer(newFile)
                csvWriter.writerow(['Coin','Average Price','MarketCap','Volume','Rank'])
                for line in self.cryptoValue:
                    csvWriter.writerow(line)   
        print('finish writing to file')
        Crypto_data.append(self.cryptoValue)
        return self.cryptoValue


#CrpyptoCoins().Price_24hour_checker()
#CrpyptoCoins().Price_1month()


