def media(*args):
    print(args, type(args))

resultado = media(10, 8, 9)
print(resultado)

def media(*args):
    return sum(args)/len(args)

resultado = media(10, 8, 9)
print(resultado)

def media(*args, margem):
    return sum(args)/len(args) + margem

resultado = media(10, 8, 9, margem=0.5)
print(resultado)

def  print_info(**kwargs):
    print(kwargs, type(kwargs))

print_info(nome='Felipe', sobrenome='Pietro')
