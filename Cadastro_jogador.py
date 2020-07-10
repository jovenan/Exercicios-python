dicionario = {}
lista_gols = []
total = 0

dicionario['nome'] = input('Nome do jogador: ')
dicionario['partidas'] = int(input('Quantas partidas {} jogou: '.format(dicionario['nome'])))

for i in range(0, dicionario['partidas']):
    lista_gols.append(int(input(f'Quantos gols na partida {i + 1}: ')))
    total += lista_gols[i]
dicionario['gols'] = lista_gols[:]
print('-' * 30)
print('O campo nome tem {}\nO campo gols tem o valor {}\nO campo total tem {}'.format(dicionario['nome'],dicionario['gols'],total))
print('-' * 30)

print('O jogador {}, jogou {} partidas.'.format(dicionario['nome'],dicionario['partidas']))
i = 0
while i < dicionario['partidas']:
    print('--> Na partida {}, fez {} gols'.format(i + 1,dicionario['gols'][i]))
    i += 1
print('Foi um total de {} Gols'.format(total))
print('-' * 30)
