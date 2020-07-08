lista = []
lista_geral = []
cont = 0
mais_peso = menos_peso = 0

while True:
    pessoa = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    lista.append(pessoa)
    lista.append(peso)
    if len(lista_geral) == 0:
        mais_peso = menos_peso = peso
    elif mais_peso < peso:
        mais_peso = peso
    elif menos_peso > peso:
        menos_peso = peso
    cont += 1
    lista_geral.append(lista[:])
    lista.clear()
    resp = input('Deseja continuar: [s/n] ').upper()
    if resp[:1] == 'N':
        break
#print(lista_geral)
print(f'{cont} pessoas foram cadastradas, o maior peso foi {mais_peso} que é o peso de: ', end='')
for p in lista_geral:
    if p[1] == mais_peso:
        print(f'{p[0]}', end='')
print(f' , menor peso foi de {menos_peso} de ', end='')
for p in lista_geral:
    if p[1] == menos_peso:
        print(f'{p[0]}',end='')