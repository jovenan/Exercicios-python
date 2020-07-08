from random import randint
from operator import itemgetter

dicionario = {'Jogador1': randint(1,6),
                 'Jogador2': randint(1,6),
                 'Jogador3': randint(1,6),
                 'Jogador4': randint(1,6)}

print('=' * 30)
for p, i in dicionario.items():
    print(f'A {p} tirou {i}')
print('=' * 30)

rank = sorted(dicionario.items(), key=itemgetter(1), reverse= True)
print('RANKING')
print('=' * 30)
colocacao = 1
for i,k in rank:
    print(f'{colocacao}º {i} tirou {k}')
    colocacao += 1
print('=' * 30)
