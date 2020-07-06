times = ('Flamengo','Santos','Palmeiras','Gremio','Atletico-PR','Sao Paulo','Internacional','Corinthians','Fortaleza','Goias','Bahia','Vasco','Fluminense','Botafogo','Ceara','Cruzeiro','CSA','Chapecoense','Avai')

print(f'Os 5 primeiros times são: {times[0:5]}')
print(f'Os 4 ultimos colocados são: {times[-4:]}')
print(f'Os times em ordem alfabetica sao: {sorted(times)}')
posicao = times.index('Chapecoense')
print(f'O chapecoense esta em: {posicao + 1}')
