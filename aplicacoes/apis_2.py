'''
ALPHA VANTAGE
Referência: https://www.alphavantage.co/

URL:
https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&dataformat=csv&apikey=demo

API key: HZSN057REIW03M7Y

'''

import requests
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&dataformat=csv&apikey=HZSN057REIW03M7Y'
response = requests.get(url)
code = response.status_code
if code == 200:
    data = response.json()
    print(data)
    print(len(data['Time Series (5min)'].keys()))
    print(data['Time Series (5min)'].keys())
print('\n')


