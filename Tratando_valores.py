cont = 0
n = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero ou 999 para sair: '))
    if n == 999:
        pass
    if n != 999:
        cont += 1
        soma += n
print('Você digitou {}, a soma deles é {}'.format(cont,soma))
