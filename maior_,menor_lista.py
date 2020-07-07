lista = []
while len(lista) != 5:
    lista.append(int(input('Digite um valor')))
print(f'O maior valor foi {max(lista)} na posicao {lista.index(max(lista))}, o menor valor foi {min(lista)}, na posicao {lista.index(min(lista))}')