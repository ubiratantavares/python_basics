def hello():
    print('Olá, mundo!')

hello()

def media(valor1, valor2, valor3):
    return (valor1 + valor2 + valor3)/3

print(media(10, 10, 10))
print(media(9, 10, 11))

resultado = media(valor1=9, valor2=10, valor3=9)
print(resultado)

print('Olá,', end=' ')
print('Pietro')

def media(valor1=0, valor2=0, valor3=0):
    return (valor1 + valor2 + valor3)/3

resultado = media()
print(resultado)
