'''
Crie um programa que simule o 
funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será 
o valor a ser sacado (número inteiro) e 
o programa vai informar quantas 
cédulas de cada valor serão entregues. 
OBS:
considere que o caixa possui 
cédulas de R$50, R$20, R$10 e R$1.
'''

print('----------Banco----------')
valor = int(input('Quanto dinheiro voce quer sacar? '))
cedula = 50
total_cedulas = 0
while True:
    if valor >= cedula:
        valor -= cedula
        total_cedulas += 1
    else:
        if valor < cedula:
            print('Total de {} cedulas de R${:.2f}.'.format(total_cedulas,cedula))
        if valor < 50:
            total_cedulas = 0
            cedula = 20
            if valor >= cedula:
                valor -= cedula
                total_cedulas += 1
            else:
                if valor < 20:
                    total_cedulas = 0
                    cedula = 10
                    if valor >= cedula:
                        valor -= cedula
                        total_cedulas += 1
                    else:
                        if valor < 10:
                            total_cedulas = 0
                            cedula = 1
                            if valor >= cedula:
                                valor -= cedula
                                total_cedulas += 1
                            if valor == 0:
                                break
print('-------------------------')
print('Obrigado por utilizar nosso servico. Volte sempre!')