'''
Faça um programa que leia o peso 
de cinco pessoas. 
No final, mostre qual foi o maior 
e o menor peso lidos.
'''
print('Este programa mostra qual menor peso e o maior peso dentre as entradas')

maiorpeso = 0
menorpeso = 0

for i in range(0, 5, 1):
    peso = float(input('Digite seu peso: '))
    if i == 0:
        maiorpeso = peso
        menorpeso = peso
    elif peso > maiorpeso:
        maiorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso
print('O menor peso foi {}, e o maior peso foi {}.'.format(menorpeso,maiorpeso))