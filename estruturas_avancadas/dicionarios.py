cidades = {'nome': 'São Paulo',
           'estado': 'SP',
           'area_km2': 1521,
           'populacao_milhoes': 12.18
}
print(cidades, type(cidades))

cidades['pais'] = 'Brasil'
print(cidades)
print(cidades['nome'])
cidades['area_km2'] = 1500
print(cidades)

cidades2 = cidades.copy()
cidades2['estado'] = 'RJ'
print(cidades2)

novos = {'populacao_milhoes': 15, 'fundacao': '25/01/1554'}
cidades.update(novos)
print(cidades)

print(cidades.get('prefeito'))
print(cidades.keys())
print(cidades.values())
print(cidades.items())


