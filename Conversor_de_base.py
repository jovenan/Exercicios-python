'''
Escreva um programa em Python que leia um número inteiro 
qualquer e peça para o usuário escolher qual será a base 
de conversão: 1 para binário, 2 para octal e 3 para
hexadecimal.
'''

print("Conversor de Bases numericas:\n")

number = int(input('Digite um numero: '))
option = int(input('Digite para converter: 1 para Binario, 2 para Octal, 3 para Hexadecimal:\n'))

if option == 1:
    print('{} convertido para Binario fica {}'.format(number, bin(number)[2:]))
elif option == 2:
    print('{} convertido para Octal fica {}'.format(number, oct(number)[2:]))
elif option == 3:
    print('{} convertido para Hexadecimal fica {}'.format(number, hex(number)[2:]))
else:
    print('Opção invalida, tente novamente')    