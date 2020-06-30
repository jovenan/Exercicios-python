"""
Uma funcao geradora retorna um gerador

-----------------------------------------------------------------------------------
| Funções                                 | Generator Functions                   |
-----------------------------------------------------------------------------------
| utilizam return                         | utilizam yield                        |
-----------------------------------------------------------------------------------
| retorna uma vez                         | podem utilizar yield múltiplas vezes  |
-----------------------------------------------------------------------------------
| quando executada, retorna um valor      | quanto executada, retorna um generator|
-----------------------------------------------------------------------------------
"""

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# essa funcao geradora retorna um gerador que ira gerando 1 valor por vez, e para isso utilizamos o next()

gen = conta_ate(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#outra forma de mostrar todos os valores é utilizando:

gen = conta_ate(4)
for num in gen:
    print(num)

#podemos tambem transformar um gerador em uma lista:

gen = conta_ate(10)
print(list(gen))

#utilizando geradores o consumo de memoria diminui drasticamente