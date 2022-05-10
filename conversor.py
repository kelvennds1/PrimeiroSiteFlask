import requests
class cotacao:
    def bid(self):
        dolar = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
        require = requests.get(dolar)
        require = require.json()
        USDBRL = float(require['USDBRL']['bid'])
        return f'O dolar está custando: R$ {USDBRL:.2f}' 
