# funcoes
""""""
def calcula_volume_esfera(raio):
    v = ((4 / 3) * 3.14 * raio ** 2)
    return v


print("Calculadora de volume de uma esfera")
R = calcula_volume_esfera(int(input("digite o valor do : ")))
print(R)


def conversao_celcius_Fahrenheit(C):
    f = (C * (9 / 5) + 32)
    return f


print("conversor de grau celcius para Fahrenheit")
R = conversao_celcius_Fahrenheit(int(input("Digite o grau celcius a ser convertido: ")))
print(R, "Fº")


# *args é um parametro de funcao que quando utilizado pode receber varios numeros no parametro

def soma_numeros(nome, *args):
    return sum(args)


print(soma_numeros('jonatas', 2, 4))


def maior_valor():
    vet_int = [0]
    s = False
    while (s == False):
        R = int(input("Digite um Nº"))
        vet_int.append(R)
        s = (input("Deseja sair? {S ou N}"))
        if s == "s":
            s = True
        else:
            s = False
    vet_int.sort()
    vet_int.reverse()
    return vet_int[0]

R = maior_valor()
print("O maior valor desta lista é ", R)
