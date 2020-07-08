matriz = [[],[],[]]
i = 1
soma_pares = 0

while True:
    if i <= 3:
        matriz[0].append(int(input('Digite um numero: ')))
        i += 1
    if i > 3 and i <= 6:
        matriz[1].append(int(input('Digite um numero: ')))
        i += 1
    if i > 6 and i <= 9:
        matriz[2].append(int(input('Digite um numero: ')))
        i += 1
    if i > 9:
        break
print(matriz[0])
print(matriz[1])
print(matriz[2])

for v in matriz:
    for i in v:
        if i % 2 == 0:
            soma_pares += i 

print(f'A soma dos valores pares é {soma_pares}, a soma da terceira coluna é {sum(matriz[1])}, e o maior valor na segunda linha é {max(matriz[1])}')