lista = []

while True:
    continuar = input('Deseja adicionar um numero? [Sim ou Não] ').upper()
    if continuar[:1] == 'N':
        break
    num = int(input('Digite um numero: '))
    if num in lista:
        print('Numero ja esta na lista')
    else: 
        lista.append(num)
lista.sort()
print(lista)