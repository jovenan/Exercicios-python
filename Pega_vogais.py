tupla = ('Aprender','Palavra', 'Som', 'Sair')

for p in tupla:
    print(f'Na palavra {p} temos ', end = ' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = '')
    print('\n')
    