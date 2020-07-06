tupla = (int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')))
print('Os numeros pares sao: ', end =' ')
for c in range(0, 4, 1):
    if tupla[c] % 2 == 0:
        print(tupla[c],', ', end = '' )

print(f'e o 9 apareceu {tupla.count(9)} vezes, o 3 foi digitado na posicao {tupla.index(3)}')