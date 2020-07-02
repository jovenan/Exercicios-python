'''
Crie um programa que leia o ano de 
nascimento de sete pessoas. 
No final, mostre quantas pessoas 
ainda não atingiram a maioridade e
quantas já são maiores.
'''

maioridade = 0
n_maioridade = 0

for i in range(0, 7, 1):
    idade = int(input('Digite sua idade: '))
    if idade > 17:
        maioridade += 1
    else:
        n_maioridade += 1
print('De 7 pessoas entrevistadas apenas {} atingiram a maioridade, {} sâo menores de idade.'.format(maioridade,n_maioridade))