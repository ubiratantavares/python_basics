# listas
paises = ['Brasil', 'Argentina', 'China', 'Canadá', 'Japão']
print(paises)
print('Tamanho da lista: '+str(len(paises)))
print('País:', paises[4])
print('País:', paises[-1])
paises[4] = 'Colômbia'
print('País:', paises[4])
print(paises)
#paises[5] = 'Chile'
print(paises[1:3])
print(paises[1:-1])
print(paises[3:])
print(paises[:3])
print(paises[:])
print(paises[::2])
print(paises[::-1])
print('Brasil' in paises)
print('Canadá' not in paises)

capitais = []
capitais.append('Brasília')
capitais.append('Buenos Aires')
capitais.append('Pequim')
capitais.append('Bogotá')
print(capitais)
capitais.insert(2, 'Paris')
print(capitais)
capitais.remove('Buenos Aires')
print(capitais)
capital = capitais.pop(2)
print(capital, capitais)

# tuplas
paises = ('Brasil', 'Argentina', 'China', 'Canadá', 'Japão')
print(paises, type(paises))

paises = 'Brasil', 'Argentina', 'China', 'Canadá', 'Japão'
print(paises, type(paises))

estado = 'São Paulo',
print(estado, type(estado))

print('Tamanho da tupla: '+str(len(paises)))
print('País:', paises[0])

a, b, c, d, e = paises
print(a, b, c, d, e)
print(*paises)

for pais in paises:
    print(pais)

