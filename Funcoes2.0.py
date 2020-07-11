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

