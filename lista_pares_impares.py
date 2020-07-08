lista = [[],[]]

for i in range (0, 7, 1):
    valor = (int(input('Digite um numero: ')))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista.sort()
print(f'Os numeros pares sao {lista[0]}, e os numeros impares sao {lista[1]}')