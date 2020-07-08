lista = []

while True:
    continuar = input('Deseja adicionar um numero? [Sim ou Não] ').upper()
    if continuar[:1] == 'N':
        break
    num = int(input('Digite um numero: '))
    lista.append(num)
lista.sort(reverse=True)
print(f'Foi digitado um total de {len(lista)} numeros. a lista é: {lista}')
if 5 in lista:
    print('O numero 5 consta na lista!')
else:
    print('O numero 5 nao consta na lista.')