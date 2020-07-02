print('Soma dos numeros pares')

sum = 0
for i in range(0, 6, 1):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        sum += num
print('a soma dos numeros pares é igual a {}'.format(sum))