dicionario = {}
lista = []
while True:
    dicionario['nome'] = input('Nome: ')
    dicionario['idade'] = int(input('Idade: '))
    media = float(input('Media: '))
    dicionario['media'] = media
    if media < 7:
        situacao = 'Reprovado'
    else:
        situacao = 'Aprovado'
    dicionario['situacao'] = situacao
    lista.append(dicionario.copy())
    dicionario.clear()
    dec = input('Deseja continuar: [S/N] ').upper()
    if dec == 'N':
        break
cont = 0
print( '=' * 30)
while cont < len(lista):
    print('Nome = {}\nMedia = {}\nSituacao = {}'.format(lista[cont]['nome'],lista[cont]['media'],lista[cont]['situacao']))
    cont += 1
    print( '=' * 30)