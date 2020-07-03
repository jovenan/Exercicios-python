print('Tabuada do numero solicidado.')

while True:
    print('Digite um numero negativo para sair.')
    number = int(input('Qual tabuada você quer saber?'))
    if number < 0:
        break
    for i in range (1, 11, 1):
        mult = number * i
        print('{}x{} = {}'.format(i,number,mult))

print('Fim.')
