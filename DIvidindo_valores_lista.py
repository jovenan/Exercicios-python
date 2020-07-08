lista = []
pares = []
impar = []
while True:
    continuar = input('Deseja adicionar um numero? [Sim ou Não] ').upper()
    if continuar[:1] == 'N':
        break
    num = int(input('Digite um numero: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impar.append(num)
print(f'lista Geral {lista}, lista de pares {pares}, lista de impares {impar}.')