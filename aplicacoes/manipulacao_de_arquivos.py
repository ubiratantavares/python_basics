arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8')
texto = arquivo.read()
print(texto)
arquivo.close()
print('FIM DA LEITURA DO ARQUIVO\n')


arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8')
linha = arquivo.readline()
print(linha)
while linha != '':
    print(linha, end='')
    linha=arquivo.readline()
arquivo.close()
print('FIM DA LEITURA DO ARQUIVO\n')


arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8')
for linha in arquivo:
    print(linha, end='')
arquivo.close()
print('FIM DA LEITURA DO ARQUIVO\n')


with open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto)
print('FIM DA LEITURA DO ARQUIVO\n')


with open('arquivo_teste.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Esta é a primeira linha que escrevi usando Python.\n')
    arquivo.write('Esta é a segunda linha que escrevi usando Python.\n')


with open('arquivo_teste.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto, end='')
print('FIM DA LEITURA DO ARQUIVO\n')


with open('arquivo_teste.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Esta é a terceira linha que escrevi usando Python.\n')


with open('arquivo_teste.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto, end='')
print('FIM DA LEITURA DO ARQUIVO\n')


