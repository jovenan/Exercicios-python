dicionario = {}
lista = []
pessoas = 0
soma_idades = 0

while True:
    dicionario['nome'] = input('Nome: ')
    sexo = input('Sexo: ').upper()
    if sexo[:1] in 'MmfF':
        dicionario['sexo'] = sexo
    else:
        print('Digite um  sexo valido!')
        sexo = input('Sexo: ').upper()        
    idade = int(input('Idade: '))
    dicionario['idade'] = idade
    pessoas += 1
    soma_idades += idade
    lista.append(dicionario.copy())
    dicionario.clear()
    resp = input('Quer continuar: [S/N]').upper()
    if resp[:1] in 'Nn':
        break
    elif resp[:1] in 'Ss':
        pass
    else:
        print('ERRO! Digite S ou N!')
        resp = input('Quer continuar: [S/N]').upper()
    
        

media = soma_idades / pessoas
lista_mulheres = []
cont = 0
lista_acima_media = []
while cont < len(lista):
    if lista[cont]['sexo'] == 'F':
        lista_mulheres.append(lista[cont]['nome'])
    if lista[cont]['idade'] > media:
        lista_acima_media.append(lista[cont]['nome'])
    cont += 1

print('=' * 30)
print('Ao todo temos {} pessoas cadastradas.'.format(pessoas))
print('A media de idade é de: {:.2f} anos'.format(media))
print('As mulheres cadastradas foram: {}'.format(lista_mulheres))
print('As pessoas que estao acima da media sao: {}'.format(lista_acima_media))
print('=' * 30)
