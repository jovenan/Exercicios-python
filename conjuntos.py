#Conjuntos

#listas são delimitadas por []

lista = [2, 4, 5, 3]
#lista.append(int(input("digite 1 numero: ")))
print(lista)
lista.sort()
print(lista)

#tuplas sao delimitadas por parenteses () elas sao imutaveis e uma alteracao ira gerar outra tupla

tupla = (10, 22, 44, 1)
print(type(tupla))

#mapas sao listas separadas por virgula do entanto cada elemento tem um valor.

mapa = {"jan":100 , "mar" :200}
print(type(mapa))

#para acessar os itens do mapa
for chave in mapa:
    print(chave)

#para acessar os valores do mapa
for chave in mapa.values():
    print(chave)

#para acessar o item e o valor
for chave, valor in mapa.items():
    print(f'Nome:{chave} valor: {valor}')

#sets sao conjuntos matematicos sao diferentes de mapas pois so tem os valores

S = {1, 4, 6}
print(S)
print(type(S))
