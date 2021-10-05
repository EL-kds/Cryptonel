from typing import Collection, Dict
from webflowpy.Webflow import Webflow
import csv
from datetime import date, datetime,timedelta
from dateutil import parser
from Price_Evaluation_V2 import crypto_coins, Crypto_data

import Price_Evaluation_V2
webflow_Token = '50d90d36dde7ec35a20b58519c3c326e4ab35ce3e456afcdbbf9704fd3f7d009'
cryptonel_site_id = '604c20ea813f94deaf58b0c5'
cryptocurrency_collections_id = '6052d23ebf19d5368d0f653a'
crypto_price_id = 'f35fb20cf21fc0b778ef65d316770ee7'
api = Webflow(token = webflow_Token)
Price_Evaluation_V2.CrpyptoCoins().PriceAverage()
class updateItems():
    def __init__(self):
        self.site_Items = (api.items(collection_id = cryptocurrency_collections_id))
        self.crypto_folder_path = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/CryptoCurrencies/'
        
    def Price_Evaluation(self):  
            for coins in crypto_coins:
                file_path = self.crypto_folder_path+coins+'/Crypto Price Chart.csv'
                for items in self.site_Items.get('items'):
                    item_id = items.get('_id')
                    self.abbreviation = items.get('abbreviation')
                    name = items.get('name')
                    slug = items.get('slug')
                    if coins == self.abbreviation:
                        
                        eval_List_24hour = self._24hour_percentage(file_path)
                        eval_List_7day = self._7day_Percentage(file_path)
                        eval_List_1month = self._1month_Percentage(file_path)
                        _24Hour_Low = self.high_Low_24_hour(file_path)[0]
                        _24Hour_High = self.high_Low_24_hour(file_path)[1]
                        ranking = (self.crypto_Rank())

                        api.updateItem(collection_id = cryptocurrency_collections_id, item_id = item_id, item_data={
                            '_archived': 'false',
                            '_draft': 'false',
                            'name':name,
                            'slug':slug,
                            'price-2': eval_List_24hour[0],
                            'marketcap': eval_List_24hour[1],
                            'volume-2':eval_List_24hour[2],
                            'market-capitalisation':eval_List_24hour[3],#for sorting and ranking 
                            '24h' : eval_List_24hour[5],
                            '24h-low': _24Hour_Low,
                            '24h-high': _24Hour_High,
                            "volume-colour-change": self._24hour_colour,
                            '7d': eval_List_7day[4],
                            '7d-colour': self._7day_colour,
                            '28d': eval_List_1month[4],
                            '1-month-colour': self._1month_colour,
                            'diluted-market-cap': eval_List_24hour[4]
                        },live=True)
                        break
        
    def _24hour_percentage(self, file_path):

        Temp_Data_list = []
        with open(file_path, 'r') as file:
            csv_Reader = csv.reader(file)
            for line in csv_Reader:
                Temp_Data_list.append([line[0],line[1],line[2],line[3],line[4],line[5]])
        self.time_started = parser.parse(Temp_Data_list[len(Temp_Data_list)-1][0]) - parser.parse(Temp_Data_list[0][0])
        Temp_Data_list.reverse()
        
        for date_time_Price in Temp_Data_list:
            
            self.current_Price = float(Temp_Data_list[0][1].replace(',', ''))
            self.previous_Price = float(date_time_Price[1].replace(',', ''))
            time_iterable_equation = parser.parse(Temp_Data_list[0][0]) - parser.parse(date_time_Price[0])

            if self.time_started < timedelta(hours=24):
                self.previous_Price = float(Temp_Data_list[len(Temp_Data_list)-1][1].replace(',', ''))
                self.Price_Percentage(self.current_Price,self.previous_Price)
                break
            
            if(time_iterable_equation == timedelta(hours=24)):
                self.Price_Percentage(self.current_Price,self.previous_Price)
                break
            else:
                if(time_iterable_equation > timedelta(hours=24)):  
                    if time_iterable_equation <= timedelta(hours=24,minutes=30):
                        if time_iterable_equation >= timedelta(hours=24,minutes=24):
                            self.Price_Percentage(self.current_Price,self.previous_Price)
                            break
                        else:
                            if time_iterable_equation >= timedelta(hours=24,minutes=18):
                                self.Price_Percentage(self.current_Price,self.previous_Price)
                                break
                            else:
                                if time_iterable_equation >= timedelta(hours=24,minutes=12):
                                    self.Price_Percentage(self.current_Price,self.previous_Price)
                                    break
                                else:
                                    if time_iterable_equation >= timedelta(hours=24,minutes=6):
                                        self.Price_Percentage(self.current_Price,self.previous_Price)
                                        break
                                    else:
                                        if time_iterable_equation >= timedelta(hours=24,minutes=0):
                                            self.Price_Percentage(self.current_Price,self.previous_Price)
                                            break
        
        self._24hour_Percentage_change = self.percentage_Change
        self._24hour_Price = self.previous_Price
        self._24hour_colour = self.price_Colour_change
        return  Temp_Data_list[0][1], Temp_Data_list[0][2], Temp_Data_list[0][3],Temp_Data_list[0][4],Temp_Data_list[0][5],self._24hour_Percentage_change, self._24hour_Price



    def high_Low_24_hour(self,file_path):
        Temp_Data_list = []
        self._24_hour_sort = []
        with open(file_path, 'r') as file:
            csv_Reader = csv.reader(file)
            for line in csv_Reader:
                    Temp_Data_list.append([line[0],line[1]])

        self.time_started = parser.parse(Temp_Data_list[len(Temp_Data_list)-1][0]) - parser.parse(Temp_Data_list[0][0])

        if self.time_started < timedelta(hours=24):
            for data in Temp_Data_list:
                self._24_hour_sort.append(data[1])
            self._24_hour_sort.sort()
            
        else:
            if self.time_started >= timedelta(hours=24):
                Temp_Data_list.reverse()
                for data in Temp_Data_list:
                    time_equation = parser.parse(Temp_Data_list[0][0]) - parser.parse(data[0])
                    self._24_hour_sort.append(data[1])
                    
                    if time_equation == timedelta(hours=24):
                        break
                self._24_hour_sort.sort()
                
        return self._24_hour_sort[0], self._24_hour_sort[len(self._24_hour_sort)-1]         
            
    def crypto_Rank(self):
        self.Temp_Data_list = []
        
        count = 0
       
        for data in Crypto_data[0]:
            self.ranking_list = {}
            self.ranking_list['coin'] = data[0]
            self.ranking_list['marketCap']= int(data[2].replace(',',''))
            self.Temp_Data_list.append(self.ranking_list)


        def call(c):
            return c['marketCap']
        self.Temp_Data_list.sort(key=call,reverse=True)
        
        
        for data in self.Temp_Data_list:
            count +=1
            self.ranking_list = {}
            
            if data.get('coin') == self.abbreviation:
                self.ranking_list['coin'] = data.get('coin')
                self.ranking_list['rank'] = count
                break
        
        if self.ranking_list.get('rank') <= 5:
            top_5 = True
        else:
            top_5 = False
            
        return top_5, self.ranking_list.get('rank')



    def _7day_Percentage(self,file_path):
        
        Temp_Data_list = []
        with open(file_path, 'r') as file:
            csv_Reader = csv.reader(file)
            for line in csv_Reader:
                Temp_Data_list.append([line[0],line[1],line[2],line[3],line[4]])
        self.time_started = parser.parse(Temp_Data_list[len(Temp_Data_list)-1][0]) - parser.parse(Temp_Data_list[0][0])
        Temp_Data_list.reverse()
        
        for date_time_Price in Temp_Data_list:
            
            self.current_Price = float(Temp_Data_list[0][1].replace(',', ''))
            self.previous_Price = float(date_time_Price[1].replace(',', ''))
            time_iterable_equation = parser.parse(Temp_Data_list[0][0]) - parser.parse(date_time_Price[0])

            if self.time_started < timedelta(days=7):
                self.previous_Price = float(Temp_Data_list[len(Temp_Data_list)-1][1].replace(',', ''))
                self.Price_Percentage(self.current_Price,self.previous_Price)
                break
            
            if(time_iterable_equation == timedelta(days=7)):
                self.Price_Percentage(self.current_Price,self.previous_Price)
                break
            else:
                if (time_iterable_equation < timedelta(days=7) and time_iterable_equation > timedelta(days=6,hours=23)):
                    self.Price_Percentage(self.current_Price,self.previous_Price)
                    break
                if(time_iterable_equation > timedelta(days=7)):  
                    if time_iterable_equation <= timedelta(days=7,minutes=60):
                        if time_iterable_equation >= timedelta(days=7,minutes=48):
                            self.Price_Percentage(self.current_Price,self.previous_Price)
                            break
                        else:
                            if time_iterable_equation >= timedelta(days=7,minutes=36):
                                self.Price_Percentage(self.current_Price,self.previous_Price)
                                break
                            else:
                                if time_iterable_equation >= timedelta(days=7,minutes=24):
                                    self.Price_Percentage(self.current_Price,self.previous_Price)
                                    break
                                else:
                                    if time_iterable_equation >= timedelta(days=7,minutes=12):
                                        self.Price_Percentage(self.current_Price,self.previous_Price)
                                        break
                                    else:
                                        if time_iterable_equation >= timedelta(days=7,minutes=0):
                                            self.Price_Percentage(self.current_Price,self.previous_Price)
                                            break
        self._7day_Percentage_change = self.percentage_Change
        self._7day_Price = self.previous_Price
        self._7day_colour = self.price_Colour_change

        return  Temp_Data_list[0][1], Temp_Data_list[0][2], Temp_Data_list[0][3],Temp_Data_list[0][4],self._7day_Percentage_change, self._7day_Price



    def _1month_Percentage(self,file_path):
        
        Temp_Data_list = []
        with open(file_path, 'r') as file:
            csv_Reader = csv.reader(file)
            for line in csv_Reader:
                Temp_Data_list.append([line[0],line[1],line[2],line[3],line[4],line[5]])
        self.time_started = parser.parse(Temp_Data_list[len(Temp_Data_list)-1][0]) - parser.parse(Temp_Data_list[0][0])
        Temp_Data_list.reverse()
        
        for date_time_Price in Temp_Data_list:
            
            self.current_Price = float(Temp_Data_list[0][1].replace(',', ''))
            self.previous_Price = float(date_time_Price[1].replace(',', ''))
            time_iterable_equation = parser.parse(Temp_Data_list[0][0]) - parser.parse(date_time_Price[0])
            if self.time_started < timedelta(weeks=4):
                self.previous_Price = float(Temp_Data_list[len(Temp_Data_list)-1][1].replace(',', ''))
                self.Price_Percentage(self.current_Price,self.previous_Price)
                break
            
            if(time_iterable_equation == timedelta(weeks=4)):
                self.Price_Percentage(self.current_Price,self.previous_Price)
                break
            else:
                if (time_iterable_equation < timedelta(weeks=4) and time_iterable_equation > timedelta(weeks=3,hours=23)):
                    self.Price_Percentage(self.current_Price,self.previous_Price)
                    break
                if(time_iterable_equation > timedelta(weeks=4)):  
                    if time_iterable_equation <= timedelta(weeks=4,minutes=60):
                        
                        if time_iterable_equation >= timedelta(weeks=4,minutes=48):
                            self.Price_Percentage(self.current_Price,self.previous_Price)
                            break
                        else:
                            if time_iterable_equation >= timedelta(weeks=4,minutes=36):
                                self.Price_Percentage(self.current_Price,self.previous_Price)
                                break
                            else:
                                if time_iterable_equation >= timedelta(weeks=4,minutes=24):
                                    self.Price_Percentage(self.current_Price,self.previous_Price)
                                    break
                                else:
                                    if time_iterable_equation >= timedelta(weeks=4,minutes=12):
                                        self.Price_Percentage(self.current_Price,self.previous_Price)
                                        break
                                    else:
                                        if time_iterable_equation >= timedelta(weeks=4,minutes=1):
                                            self.Price_Percentage(self.current_Price,self.previous_Price)
                                            break
        self._1month_Percentage_change = self.percentage_Change
        self._1month_Price = self.previous_Price
        self._1month_colour = self.price_Colour_change

        return  Temp_Data_list[0][1], Temp_Data_list[0][2], Temp_Data_list[0][3],Temp_Data_list[0][4],self._1month_Percentage_change, self._1month_Price    

    def Price_Percentage(self,current_Price, previous_Price):
        if (current_Price == previous_Price):
            self.percentage_Change = 0.0
            self.price_Colour_change = 'green'
        if current_Price > previous_Price:
            self.percentage_Change = "{:,.2f}".format((abs(current_Price - previous_Price) / self.previous_Price) * 100.0)
            self.price_Colour_change = 'green'
        elif current_Price < previous_Price:
            self.percentage_Change = "{:,.2f}".format((abs(current_Price - previous_Price) / previous_Price) * 100.0)
            self.percentage_Change = -float(self.percentage_Change)
            self.price_Colour_change = 'red'

