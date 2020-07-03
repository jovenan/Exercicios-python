from random import randint

print('Ola sou seu computador...\npensei em um numero...\nvamos ver se voce consegue adivinhar qual é, de 0 a 10')
numero = randint(0, 10)
user = int(input('Digite seu palpite: '))
tentativas = 1
if user == numero:
    print('parabens voce acertou de primeira!!!')        
while user != numero:
    if numero > user:
        print('Mais... Tente de novo!')
        tentativas += 1
    else:
        print('Menos... Tente de novo!')
        tentativas += 1
    user = int(input('Digite seu palpite: '))
print('Parabens voce acertou com {} tentativas.'.format(tentativas))