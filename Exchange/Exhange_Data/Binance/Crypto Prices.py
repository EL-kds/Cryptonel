import requests

new = {'pass':'google'}

print(new.get('pass'))

class BitcoinToFiat_prices: 

    def __init__(self,):
        print(self.BTCUSDT())

    def BTCGBP(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BTCGBP')
        return self.value.json().get('price')
        
    def BTCUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
        return self.value.json().get('price')
    
    def BTCEUR(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BTCEUR')
        return self.value.json().get('price')
        
    def BTCRUB(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BTCRUB')
        return self.value.json().get('price')     

    def BTCAUD(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BTCRUB')
        return self.value.json().get('price')
        
class EthereumToFiat_prices:
    def ETHGBP(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ETHGBP')
        return self.value.json().get('price')
        
    def ETHUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ETHUSDT')
        return self.value.json().get('price')
    
    def ETHEUR(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ETHEUR')
        return self.value.json().get('price')
        
    def ETHRUB(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ETHRUB')
        return self.value.json().get('price')     

    def ETHAUD(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ETHAUD')
        return self.value.json().get('price')

class BinanceCoinToFiat_prices:
    def BNBGBP(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BNBGBP')
        return self.value.json().get('price')
        
    def BNBUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BNBUSDT')
        return self.value.json().get('price')
    
    def BNBEUR(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BNBEUR')
        return self.value.json().get('price')
        
    def BNBRUB(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BNBRUB')
        return self.value.json().get('price')     

    def BNBAUD(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BNBAUD')
        return self.value.json().get('price')
    
class BinanceUSD_ToFiat_prices:
    def BUSDUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BUSDUSDT')
        return self.value.json().get('price')
        
    def BUSDRUB(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BNBUSDT')
        return self.value.json().get('price')

   
class BitcoinCash_ToFiat_prices:
    def BCHUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BCHUSDT')
        return self.value.json().get('price')
        
    def BCHEUR(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BCHEUR')
        return self.value.json().get('price')
    
class Cardano_ToFiat_prices:
    def ADAUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ADAUSDT')
        return self.value.json().get('price')
        
    def ADAEUR(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ADAEUR')
        return self.value.json().get('price')

    def ADAGBP(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ADAGBP')
        return self.value.json().get('price')
    
    def ADAAUD(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ADAAUD')
        return self.value.json().get('price')

    def ADARUB(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ADARUB')
        return self.value.json().get('price')
    
class ChainLink_ToFiat_prices:
    def LINKUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ADAUSDT')
        return self.value.json().get('price')
        
    def LINKEUR(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ADAEUR')
        return self.value.json().get('price')

    def LINKGBP(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ADAGBP')
        return self.value.json().get('price')
    
    def LINKAUD(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ADAAUD')
        return self.value.json().get('price')

    def LINKRUB(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ADARUB')
        return self.value.json().get('price')
class Cosmos_ToFiat_prices:
    def ATOMUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ATOMUSDT')
        return self.value.json().get('price')
class DogeCoin_ToFiat_prices:
    def DOGEUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ADAUSDT')
        return self.value.json().get('price')
class Eos_ToFiat_prices:
    def EOSUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=EOSUSDT')
        return self.value.json().get('price')    

class FTX_ToFiat_prices:
    def FTTUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=FTTUSDT')
        return self.value.json().get('price')

class IOTA_ToFiat_prices:
    def IOTAUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=IOTAUSDT')
        return self.value.json().get('price') 

class LiteCoin_ToFiat_prices:
    def LTCUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=LTCUSDT')
        return self.value.json().get('price')

class Monero_ToFiat_prices:
    def XMRUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=XMRUSDT')
        return self.value.json().get('price')   

class NEM_ToFiat_prices:
    def XEMUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=XEMUSDT')
        return self.value.json().get('price') 

class Plokadot_ToFiat_prices:
    def DOTUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=DOTUSDT')
        return self.value.json().get('price')

class Ripple_ToFiat_prices:
    def XRPUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=EOSUSDT')
        return self.value.json().get('price')

class solonaToFiat_prices:
    def SOLUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=SOLUSDT')
        return self.value.json().get('price')

class stellar_ToFiat_prices:
    def XLMUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=XLMUSDT')
        return self.value.json().get('price')  

class Tether_ToFiat_prices:
    def BTCUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
        return self.value.json().get('price')

class theta_ToFiat_prices:
    def THETAUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=THETAUSDT')
        return self.value.json().get('price')

class Tron_ToFiat_prices:
    def TRXUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=TRXUSDT')
        return self.value.json().get('price')

class Vechain_ToFiat_prices:
    def VETUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=VETUSDT')
        return self.value.json().get('price')

class filecoin_ToFiat_prices:
    def FILUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=FILUSDT')
        return self.value.json().get('price')

class EosCoin_ToFiat_prices:
    def EOSUSDT(self):
        self.value = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=EOSUSDT')
        return self.value.json().get('price')                                                                                                        

cryptoPairs = {'BTCUSDT':'BTC','ETHUSDT':'ETH','BNBUSDT':'BNB','BUSDUSDT':'BUSD','BCHUSDT':'BCH','ADAUSDT':'ADA', 'LINKUSDT':'LINK', 'ATOMUSDT':'ATOM', 'CROUSDT':'CRO', 'DOGEUSDT':'DOGE', 'EOSUSDT':'EOS',
 'FTTUSDT':'FTT', 'IOTAUSDT':'IOTA', 'LTCUSDT':'LTC', 'XMRUSDT':'XMR', 'XEMUSDT':'XEM', 'DOTUSDT':'DOT', 'XRPUSDT':'XRP', 'SOLUSDT':'SOL', 'XLMUSDT':'XLM', 'USDTUSD':'USDT', 'THETAUSDT':'THETA', 'TRXUSDT':'TRX',
 'VETUSDT':'VET', 'FILUSDT':'FIL', 'SHIBUSDT':'SHIB'}

print(len(cryptoPairs.keys()))