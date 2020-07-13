def area(largura,comprimento):
    area = largura * comprimento
    return area

def escreva(mensagem):
    tamanho = len(mensagem)
    print('~' * (tamanho + 4))
    print('  {}'.format(mensagem))
    print('~' * (tamanho + 4))

def contagem(inicio,fim,passo):
    print('-' * 20)    
    for i in range (1,11,1):
        print(i, end=' ')
    print('')
    print('-' * 20)
    for i in range(10,0,-2):
        print(i, end=' ')
    print('0 FIM')
    print('-' * 20)
    for i in range(inicio,fim+1,passo):
        print(i, end=' ')
    print('FIM')
    print('-' * 20)

def maior(*valor):
    return max(valor)


from random import randint
numeros = []

def sorteia():
    for i in range(0,5,1):
        numeros.append(randint(0,100))

def somaPar(lista):
    resultado = 0
    for i in lista:
        if i % 2 == 0:
            resultado += i
    return resultado
sorteia()
print(numeros)
print(somaPar(numeros))

import datetime
def voto(ano_nascimento):
    tipo = ''
    data = datetime.date.today()
    idade = data.year - ano_nascimento
    if idade < 16:
        tipo = 'Nao Vota'
    if idade > 15 and idade < 19:
        tipo = 'Nao obrigatorio'
    if idade > 18 and idade < 60:
        tipo = 'Obrigadorio'
    if idade > 59:
        tipo = 'Nao obrigatorio'
    return tipo

#print(voto(int(input('Digite seu ano de nascimento'))))

def fatorial(num):
    i = num
    while i > 1:
        i -= 1
        num = num * i
    return num


def ficha(nome='desconhecido',gols=0):
    try:
        int(gols)
    except:
        gols = 0
    if nome == '':
        nome = 'Desconhecido'
    print(f'O jogador {nome} fez {gols} gols.')

#ficha(input('Digite o nome:'),input('Digite quantos gols:'))


def leiaInt(num):
    while True:
        try:
            int(num)
            break
        except:
            print('Digite um numero valido!')
            num = (input('numero: '))
    print('Voce digitou {}'.format(num))    

#leiaInt(input('Numero: '))

def notas(*nota, sit=False):
    lista = nota
    turma = {}
    turma['total'] = len(lista)
    turma['maior'] = max(lista)
    turma['menor'] = min(lista)
    turma['media'] = sum(lista) / len(lista)
    if sit == True:
        if turma['media'] <= 5:
            turma['situacao'] = 'Ruim'
        elif turma['media'] > 5 and turma['media'] < 8:
            turma['situacao'] = 'Intermediario'
        else:
            turma['situacao'] = 'Bom'
    return turma

n = notas(4,5,8,2,3)
print(n)

