dicionario = {}
lista_gols = []
total = 0
time = []

while True:
    dicionario['nome'] = input('Nome do jogador: ')
    dicionario['partidas'] = int(input('Quantas partidas {} jogou: '.format(dicionario['nome'])))

    for i in range(0, dicionario['partidas']):
        lista_gols.append(int(input(f'Quantos gols na partida {i + 1}: ')))
        total += lista_gols[i]
    dicionario['gols'] = lista_gols[:]
    time.append(dicionario.copy())
    dicionario.clear()
    lista_gols.clear()
    resp = input('Quer continuar? [S/N] ').upper()
    if resp[:1] == 'N':
        break

c = 0
print('-' * 40)
print('Cod   nome            gols            total')
while c < len(time):
    print('{:<3} -> {:<7} ->{:<15} -> {:>6} '.format(c + 1,time[c]['nome'],str(time[c]['gols']),sum(time[c]['gols'])))
    c += 1
print('-' * 40)

while True:
    c = int(input('Quer informacoes de qual jogador? [999 para parar] '))
    if c == 999:
        break
    elif c > len(time):
        print('indice fora das informacoes dadas! Digite um indice valido!')
    else:
        print('-' * 30)
        print('O jogador {}, jogou {} partidas.'.format(time[c - 1]['nome'],time[c -1 ]['partidas']))
        i = 0
        while i < time[c - 1]['partidas']:
            print('--> Na partida {}, fez {} gols'.format(i + 1,time[c - 1]['gols'][i]))
            i += 1
        print('Foi um total de {} Gols'.format(sum(time[c - 1]['gols'])))
        print('-' * 30)

print('-' * 30)
print('Ate mais')
print('-' * 30)