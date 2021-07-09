import requests as r
import datetime as dt
import csv

url = 'https://api.covid19api.com/dayone/country/brazil'
resposta = r.get(url)
codigo = resposta.status_code
raw_data = resposta.json()
print(raw_data[0])
final_data = []

for obs in raw_data:
    final_data.append([obs['Date'], obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active']])

final_data.insert(0, ['data', 'confirmados', 'obitos', 'recuperados', 'ativo'])

print(len(final_data))
print(final_data)

DATA = 0
CONFIRMADOS = 1
OBITOS = 2
RECUPERADOS = 3
ATIVOS = 4

for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]
print(final_data)

with open('brasil_covid_novo.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

with open('brasil_covid_novo.csv', 'r', encoding='utf-8') as arq:
    leitor = csv.reader(arq, delimiter=',')
    for linha in leitor:
        print(linha)

for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')

for i in range(0, len(final_data)):
    print(final_data[i])
