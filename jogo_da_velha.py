import os
jogo = (["00","01","02"],["10","11","12"],["20","21","22"])
lista = []
jogada = 0
fim_de_jogo = 1		

def imprime_jogo(lista):
	linha = 0
	coluna = 0
	while(linha <= 2):
		while(coluna <= 2 ):
			print (lista[linha][coluna], end=" ")
			coluna += 1
		linha += 1
		print()
		coluna = 0

def jogada_repetida(x,y,jogo1):
	if (jogo[x][y] == " x") or (jogo[x][y] == " O"):
		return True

def qual_jogador(x,y):
	os.system ("clear")
	if (jogada%2 == 0):
		jogo[x][y] = " x"
		imprime_jogo(jogo)
	else:
		jogo[x][y] = " O"
		imprime_jogo(jogo)

imprime_jogo(jogo)

while (fim_de_jogo != 0):
	x1 = int(input("\ndigite o valor da linha"))
	y1 = int(input("digite o valor da coluna"))
	if jogada_repetida(x1,y1,jogo) == True:
		print("\nnao é possivel fazer essa jogada")
	else:	
		qual_jogador(x1,y1)
		jogada +=1
