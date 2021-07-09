import csv

with open('brasil_covid.csv', 'r', encoding='utf-8') as arq:
    leitor = csv.reader(arq)
    header = next(leitor)
    for linha in leitor:
        if int(linha[2]) > 1:
            print(linha)


with open('brasil_covid.csv', 'r', encoding='utf-8') as arq:
    linhas = arq.read()
    linhas = linhas.split('\n')
    for linha in linhas:
        linha = linha.split(',')
        print(linha)

with open('users.csv', 'w', encoding='utf-8', newline='') as arq:
    escritor = csv.writer(arq)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Pietro', 'Ribeiro', 'pietro@gmail.com', 'Masculino'])
    escritor.writerow(['João', 'Ferreira', 'joao@gmail.com', 'Masculino'])

with open('users.csv', 'r', encoding='utf-8') as arq:
    leitor = csv.reader(arq)
    for linha in leitor:
        print(linha)

header = ['nome', 'sobrenome']

dados = []

opcao = int(input('O que deseja fazer?\n1-Cadastrar\n0-Sair\n'))
while opcao != 0:
    nome = input('Digite o nome: ')
    sobrenome = input('Digite o sobrenome: ')
    dados.append([nome, sobrenome])
    opcao = int(input('O que deseja fazer?\n1-Cadastrar\n0-Sair\n'))

with open('users.csv', 'w', encoding='utf-8', newline='') as arq:
    escritor = csv.writer(arq)
    escritor.writerow(header)
    escritor.writerows(dados)

with open('users.csv', 'r', encoding='utf-8') as arq:
    leitor = csv.reader(arq, delimiter=',')
    for linha in leitor:
        print(linha)
