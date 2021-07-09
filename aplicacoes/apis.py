'''
Exchange Rate API
Referência: https://www.exchangerate-api.com/docs/python-currency-api

API Access: Your API Key: 247eda6115d994c36e9c659e
Example Request: https://v6.exchangerate-api.com/v6/247eda6115d994c36e9c659e/latest/USD
'''

import requests

# Where USD is the base currency you want to use
url = 'https://api.exchangerate-api.com/v6/latest'

# Making our request
response = requests.get(url)

code = response.status_code

if code == 200:
    data = response.json()
    #print(data)
    reais = float(input('Digite o valor em R$ a ser convertido para U$: '))
    cotacao = data['rates']['BRL']
    print('R$ {:.2f} equivale a U$ {:.2f}'.format(reais, reais/cotacao))

url = 'https://v6.exchangerate-api.com/v6/247eda6115d994c36e9c659e/latest/USD'
response = requests.get(url)
code = response.status_code
if code == 200:
    data = response.json()
    print(data['conversion_rates'])
