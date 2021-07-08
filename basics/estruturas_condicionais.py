valor_passagem = 4.30

valor_corrida = input('Qual é o valor de corrida? ')
valor_corrida = float(valor_corrida)

if valor_corrida <= valor_passagem * 5:
    print('Pague a corrida')
elif valor_corrida <= valor_passagem * 6:
    print('Aguarde um momento, o valor da corrida pode abaixar')
else:
    print('Pegue o ônibus')



