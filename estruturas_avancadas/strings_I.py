empresa = 'Google'
print(empresa)
empresa = "Google"
print(empresa)
print(empresa[0])
print(empresa[:3])

empresa = "Let's code"
print(empresa)
frase = "O professor Pietro da Let's code disse: \"Hoje a pizza é por minha conta\""
print(frase)

cidades = "São Paulo,Belo Horizonte,Rio de Janeiro,Brasília"
cidades = cidades.split(',')
print(cidades)

cidades = "São Paulo Belo Horizonte Rio de Janeiro Brasília"
cidades = cidades.split()
print(cidades)
cabecalho = '                         MENU PRINCIPAL                                '
print(cabecalho.strip())

cidade = 'rio DE jaNeiro'
print(cidade.title())
print(cidade.capitalize())
print(cidade.lower())
print(cidade.upper())
print(cidade.replace(cidade, 'RJ'))

msg = 'Que cidade do Brasil é conhecida como cidade maravilhosa? '
cidade = input(msg)
cidade = cidade.strip()
while cidade.lower() != 'rio de janeiro':
    print('Resposta errada. Tente novamente...')
    cidade = input(msg)
print('Resposta correta.')

msg = 'Você viu o que o Pietro disse na sala ontem?'
citado = 'Pietro' in msg
print(citado)

