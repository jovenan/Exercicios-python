from random import randint
sorteio = []
i = 1
print('=' * 50)
print('                   Mega Sena       ')
print('=' * 50)

rodadas = int(input('Digite quantos jogos serão gerados: '))

while i <= rodadas:
    for r in range(0, 6, 1):
        sorteio.append(randint(1,60))
    print(f'A Rodada {i} resultou em: {sorteio}')
    i += 1
    sorteio.clear()
print('=' * 50)