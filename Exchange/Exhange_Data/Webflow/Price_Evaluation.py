import csv
import requests
exchanges = ['Binance','Bitfinex','Bitstamp','bittrex','CEX','Coinbase','Huobi','Kraken','Kucoin']
crpyto_coins = ['BTC', 'ETH','BNB','BUSD','BCH','ADA','LINK','ATOM','CRO','DOGE','EOS','FTT','MIOTA','LTC','XMR','XEM','DOT','XRP','SOL','XLM','USDT','THETA','TRX','VET','FIL','SHIB']
class CrpyptoCoins:
    def __init__(self):
        self.value = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')
        self.currentPrice_file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/Crypto Price.csv'
        self.PriceAverage()
    
    def PriceAverage(self):
        self.cryptoValue = []
        for coin in crpyto_coins:
            self.average_Price = 0
            self.volume = 0
            self.price_Addition = 0
            self.volume_Addition = 0
            self.count = 0
            self.marketCap = 0
            
            for exchange in exchanges:
                self.file_Path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/'+exchange+'/Price Results.csv'
                #print(self.file_Path)
                with open(self.file_Path, 'r') as file:
                    self.csvReader = csv.reader(file)
                    next(self.csvReader)
                    for line in self.csvReader:
                        if line[0] == coin:
                            self.count += 1
                            self.price_Addition = self.price_Addition +float(line[2])
                            self.volume_Addition = self.volume_Addition + float(line[3])

            self.average_Price = self.price_Addition / self.count
            self.volume =  "{:,.0f}".format(self.volume_Addition * self.average_Price)

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
                    self.average_Price = self.string_price[0:7]
                elif(price == '.' and priceCount > 6):
                    self.average_Price = "{:,.2f}".format(self.string_price)

            self.string_volume = self.volume

            for crypto in self.value.json():
                
                if crypto.get('symbol') == coin.lower():  
                    self.marketCap = "{:,.0f}".format(self.price_Addition /self.count * crypto.get('circulating_supply'))
                    self.rank_Marketcap = self.price_Addition /self.count * crypto.get('circulating_supply')
            
            self.cryptoValue.append([coin, self.average_Price,self.marketCap, self.volume, self.rank_Marketcap])

            
            self.file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/Crypto Price.csv'
            with open(self.file_path, 'w') as newFile:
                csvWriter = csv.writer(newFile)
                csvWriter.writerow(['Coin','Average Price','MarketCap','Volume','Rank'])
                for line in self.cryptoValue:
                    csvWriter.writerow(line)    
        print('starting to write to files')


    #chack for price every 24 hour
    def Price_24hour(self):
        self.lastPrices = []
        self.file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/Crypto Price.csv'
        with open (self.file_path, 'r') as newFile:
            csvReader = csv.reader(newFile)
            next(csvReader)
            for line in csvReader:
                self.lastPrice = line[1].replace(',','')
                self.lastPrices.append([line[0], self.lastPrice])

        print(self.lastPrices)
        self.file_path_2 = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/24 hour files/Crypto Price 24h.csv'
        with open(self.file_path_2, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['coin','24hour Price'])
            for coins in self.lastPrices:
                csvWriter.writerow(coins)
    
    
    #check for price percentage every 24 hour
    def Price_24hour_checker(self):
        self._24hour_file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/24 hour files/Crypto Price 24h.csv'
        self.currentPrice_file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/Crypto Price.csv'
        self._24hour_percentage_File_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/24 hour files/Crypto 24h Price Percentage.csv'
        self._24hour_percentage_Price = []
        with open (self._24hour_file_path, 'r') as _24hour_file:
            csvReader = csv.reader(_24hour_file)
            next(csvReader)
            for Previous_Crypto_Price in csvReader:
                 with open (self.currentPrice_file_path, 'r') as _1min_file:
                    csvReader2 = csv.reader(_1min_file)
                    next(csvReader2)
                    for coins in csvReader2:
                        if Previous_Crypto_Price[0] == coins[0]:
                            self.current_Price = float(coins[1].replace(',',''))
                            self.previous_Price = float(Previous_Crypto_Price[1])
                            
                            if self.current_Price == self.previous_Price:
                                self._24hour_percentage_Change = 0.0
                                self._24hour_price_change = 'neutral'
                            try:
                                self._24hour_percentage_Change = "{:,.2f}".format((abs(self.current_Price - self.previous_Price) / self.previous_Price) * 100.0)
                                if self.current_Price > self.previous_Price:
                                    self._24hour_price_change = 'bull'
                                elif self.current_Price < self.previous_Price:
                                    self._24hour_price_change = 'bear'
                                    self._24hour_percentage_Change = -float(self._24hour_percentage_Change)
                                self._24hour_percentage_Price.append([coins[0],coins[1],coins[2],coins[3],coins[4], self._24hour_percentage_Change, self._24hour_price_change])
                            except ZeroDivisionError:
                                return 0 
        
        with open(self._24hour_percentage_File_path, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['coin','Average Price','MarketCap','Volume','Rank','Percentage','Price Change'])
            for coins in self._24hour_percentage_Price:
                csvWriter.writerow(coins)  
        print('finish writing to file','\n')


    #check for price every 7 day
    def Price_7day(self):
        self.lastPrices = []
        self.file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/Crypto Price.csv'
        with open (self.file_path, 'r') as newFile:
            csvReader = csv.reader(newFile)
            next(csvReader)
            for line in csvReader:
                self.lastPrice = line[1].replace(',','')
                self.lastPrices.append([line[0], self.lastPrice])

        print(self.lastPrices)
        self.file_path_2 = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/7 day files/Crypto Price 7day.csv'
        with open(self.file_path_2, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['coin','7day Price'])
            for coins in self.lastPrices:
                csvWriter.writerow(coins)
    
    #check for price percentage every 7 days
    def Price_7day_checker(self):
        self._7day_file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/7 day files/Crypto Price 7day.csv'
        self.currentPrice_file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/Crypto Price.csv'
        self._7day_percentage_File_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/7 day files/Crypto 7day Price Percentage.csv'
        self._7day_percentage_Price = []
        with open (self._7day_file_path, 'r') as _7day_file:
            csvReader = csv.reader(_7day_file)
            next(csvReader)
            for Previous_Crypto_Price in csvReader:

                 with open (self.currentPrice_file_path, 'r') as _current_Price_file:
                    csvReader2 = csv.reader(_current_Price_file)
                    next(csvReader2)
                    for coins in csvReader2:
                        if Previous_Crypto_Price[0] == coins[0]:
                            self.current_Price = float(coins[1].replace(',',''))
                            self.previous_Price = float(Previous_Crypto_Price[1])
                            
                            if self.current_Price == self.previous_Price:
                                self._7day_percentage_Change = 0.0
                                self._7day_price_change = 'neutral'
                            try:
                                self._7day_percentage_Change = "{:,.2f}".format((abs(self.current_Price - self.previous_Price) / self.previous_Price) * 100.0)
                                if self.current_Price > self.previous_Price:
                                    self._7day_price_change = 'bull'
                                elif self.current_Price < self.previous_Price:
                                    self._7day_price_change = 'bear'
                                    self._7day_percentage_Change = -float(self._7day_percentage_Change)
                                self._7day_percentage_Price.append([coins[0],coins[1],coins[2],coins[3],coins[4],self._7day_percentage_Change,self._7day_price_change])
                            except ZeroDivisionError:
                                return 0 
        
        with open(self._7day_percentage_File_path, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['coin','Average Price','MarketCap','Volume','Rank','Percentage','Price Change'])
            for coins in self._7day_percentage_Price:
                csvWriter.writerow(coins)  
        print('finish writing to file','\n')

    
    #check for price every 1 month day
    def Price_1month(self):
        self.lastPrices = []
        self.file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/Crypto Price.csv'
        with open (self.file_path, 'r') as newFile:
            csvReader = csv.reader(newFile)
            next(csvReader)
            for line in csvReader:
                self.lastPrice = line[1].replace(',','')
                self.lastPrices.append([line[0], self.lastPrice])

        print(self.lastPrices)
        self.file_path_2 = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/1 month files/Crypto Price 1month.csv'
        with open(self.file_path_2, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['coin', '1month Price'])
            for coins in self.lastPrices:
                csvWriter.writerow(coins)

    
    #check for price percentage every 1 month days
    def Price_1month_checker(self):
        self._1month_file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/1 month files/Crypto Price 1month.csv'
        self.currentPrice_file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/Crypto Price.csv'
        self._1month_percentage_File_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/1 month files/Crypto 1month Price Percentage.csv'
        self._1month_percentage_Price = []
        with open (self._1month_file_path, 'r') as _1month_file:
            csvReader = csv.reader(_1month_file)
            next(csvReader)
            for Previous_Crypto_Price in csvReader:
                 with open (self.currentPrice_file_path, 'r') as _current_Price_file:
                    csvReader2 = csv.reader(_current_Price_file)
                    next(csvReader2)
                    for coins in csvReader2:
                        if Previous_Crypto_Price[0] == coins[0]:
                            self.current_Price = float(coins[1].replace(',',''))
                            self.previous_Price = float(Previous_Crypto_Price[1])
                            
                            if self.current_Price == self.previous_Price:
                                self._1month_percentage_Change = 0.0
                                self._1month_price_change = 'neutral'
                            try:
                                self._1month_percentage_Change = "{:,.2f}".format((abs(self.current_Price - self.previous_Price) / self.previous_Price) * 100.0)
                                if self.current_Price > self.previous_Price:
                                    self._1month_price_change = 'bull'
                                elif self.current_Price < self.previous_Price:
                                    self._1month_price_change = 'bear'
                                    self._1month_percentage_Change = -float(self._1month_percentage_Change)
                                self._1month_percentage_Price.append([coins[0],coins[1],coins[2],coins[3],coins[4],self._1month_percentage_Change,self._1month_price_change])
                            except ZeroDivisionError:
                                return 0 
        
        with open(self._1month_percentage_File_path, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['coin','Average Price','MarketCap','Volume','Rank','Percentage','Price Change'])
            for coins in self._1month_percentage_Price:
                csvWriter.writerow(coins)  
        print('finish writing to file','\n')
    

    #check for percentages every minute
    def Crypto_page_eval(self):
        self.Price_24hour_checker()
        self.Price_7day_checker()
        self.Price_1month_checker()
        self._24hour_percentage_File_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/24 hour files/Crypto 24h Price Percentage.csv'
        self._7day_percentage_File_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/7 day files/Crypto 7day Price Percentage.csv'
        self._1month_percentage_File_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/1 month files/Crypto 1month Price Percentage.csv'
        crypto_Percentage_Files = [self._24hour_percentage_File_path, self._7day_percentage_File_path, self._1month_percentage_File_path]
        self._24hour_percentage_Data = []
        self._7day_percentage_Data = []
        self._1month_percentage_Data = []
        crypto_Percentage_Data = [self._24hour_percentage_Data, self._7day_percentage_Data, self._1month_percentage_Data]
        
        for file in crypto_Percentage_Files:
            with open (file, 'r') as newFile:
                csvReader = csv.reader(newFile)
                next(csvReader)
                for line in csvReader:
                    if file == self._24hour_percentage_File_path:
                        self._24hour_percentage_Data.append(line)
                    elif file == self._7day_percentage_File_path:
                        self._7day_percentage_Data.append(line)
                    elif file == self._1month_percentage_File_path:
                        self._1month_percentage_Data.append(line)
        print(crypto_Percentage_Data[0])

                
                    
                    
        with open (self.currentPrice_file_path, 'r') as newFile:
            csvReader = csv.reader(newFile)
            next(csvReader)
            for line in csvReader:
                #self.lastPrice = line[1].replace(',','')
                #self.lastPrices.append([line[0], self.lastPrice])
                pass
        
        self.eval_file_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/Crypto Page Price eval.csv'
        
        with open(self.eval_file_path, 'w') as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(['coin','Average Price','MarketCap','Volume','Rank','24 hour Percentage','24hour Price Change',
            '7day Percentage','7day Price Change','1 month Percentage','1 month Price Change'])
            self.count = 0
            for coins in crypto_Percentage_Data[0]:
                _24hour_data = coins
                _7day_data = crypto_Percentage_Data[1]
                _1month_data = crypto_Percentage_Data[2]
                Temp_data = []
                
                csvWriter.writerow([coins[0],coins[1],coins[2],coins[3],coins[4],coins[5],coins[6],
                _7day_data[self.count][5],_7day_data[self.count][6],_1month_data[self.count][5],_1month_data[self.count][6]])
                self.count += 1
        print('finish writing to file','\n')


#CrpyptoCoins().Crypto_page_eval()
#CrpyptoCoins().Price_24hour_checker()
#CrpyptoCoins().Price_1month()


