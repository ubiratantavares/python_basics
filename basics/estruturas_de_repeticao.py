cont = 0
while cont <= 10:
    cont += 1
    if cont == 1:
        print(cont, 'item limpo')
    else:
        print(cont, 'itens limpos')
print('fim da repetição do bloco while')

cont = 0
while True:
    if cont < 10:
        cont += 1
        if cont == 1:
            print(cont, 'item limpo')
        else:
            print(cont, 'itens limpos')
    else:
        break
print('fim da repetição do bloco while')

texto = input('Digite a sua senha: ')
while texto != 'LetsCode':
    texto = input('Senha inválida. Digite a sua senha novamente: ')
print('Acesso permitido!')

cont = 0
while cont <= 10:
    cont += 1
    if cont == 1:
        continue
    print(cont, 'itens limpos')
print('fim da repetição do bloco while')

