cidades = ['São Paulo', 'Londres', 'Tóquio', 'Paris']

for cidade in cidades:
    print(cidade)

print('\n')

contador = 0
while contador < len(cidades):
    print(cidades[contador])
    contador += 1

cidades = ('São Paulo', 'Londres', 'Tóquio', 'Paris')

for cidade in cidades:
    print(cidade)
print('\n')

cidades = {'nome': 'São Paulo', 'estado': 'RJ', 'populacao_milhoes': 12.2}

for chave in cidades:
    print(f'{chave}: {cidades[chave]}')

cidades = ['São Paulo', 'Londres', 'Tóquio', 'Paris']
for posicao in range(len(cidades)):
    cidades[posicao] = 'Rio de Janeiro'
print(cidades)

print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 2)))