print('Jogo do par ou impar com o PC...')
from random import randint

vencidas = 0
while True:
    jogador = input('Par ou impar?\n').upper()
    maquina = randint(1,2)
    if maquina == 1:
        maquina = 'PAR'
    else:
        maquina = 'IMPAR'
    n_jogador = int(input('Digite um numero de 1 a 10: '))
    n_maquina = randint(0,10)
    print('A maquina jogou {}'.format(n_maquina))
    soma = n_jogador + n_maquina
    print('A soma deu {}'.format(soma))
    if soma % 2 == 0:
        i = 'PAR'
    else:
        i = 'IMPAR'
    if jogador == i:
        print('Parabens você venceu a rodada!')
        vencidas +=1
    else:
        break
print('Voce perde!\nTeve um total de vitorias de {}'.format(vencidas))