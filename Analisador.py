'''
Desenvolva um programa que leia 
o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: 
a média de idade do grupo, qual 
é o nome do homem mais velho e 
quantas mulheres têm menos de 20 anos.
'''

homem_mais_velho = ''
idade_mais_velho = 0
n_mulheres_menos_20 = 0
media = 0

for i in range(0, 4, 1):
    nome = input('Digite seu nome: ')
    sexo = input('Digite seu sexo: M ou F ')
    idade = int(input('Digite sua idade: '))
    sexo = sexo.upper()
    media += idade
    if idade_mais_velho == 0 and sexo == 'M':
        idade_mais_velho = idade
    if sexo == 'M' and idade_mais_velho < idade:
        idade_mais_velho = idade
        homem_mais_velho = nome
    if sexo == 'F' and idade < 21:
        n_mulheres_menos_20 += 1
media /= 4
print('A media de idade é {}, o homem mais velho é o {}, e {} mulhere(s) tem menos de 20 anos.'.format(media,homem_mais_velho,n_mulheres_menos_20))
