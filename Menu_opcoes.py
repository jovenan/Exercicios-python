from time import sleep
print('Calculadora com menu.')
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
op = ""
while op is not 4:
    op = int(input('Digite uma das opções:\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] sair do programa\n'))
    if op == 1:
        result = num1 + num2
    if op == 2:
        result = num1 * num2
    if op == 3:
        if num1 > num2:
            result = num1
        else: 
            result = num2
    if op < 4:
        print('A sua solicitação resultou em: {}'.format(result))
        sleep(3)
    if op > 4:
        print('Digite um valor valido!')
        sleep(3)
print('Você saiu do programa.')