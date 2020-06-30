import random
cash_user = int(20)
cash_comp = int(20)
aposta_user = int(0)
aposta_comp = int(0)
ponto_carta_user = int(0)
ponto_carta_comp = int(0)
N_tirado = int(0)
resp_user = str
pote = int(0)
estourou = str
print("BLACK JACK\n")
while (cash_comp != 0) and (cash_user != 0):
	print("\nVocê tem: R$",cash_user,"e o computador tem R$",cash_comp,"\n")
	aposta_user = int(input("Digite sua aposta:\n\n"))
	if (aposta_user <= cash_comp) and (aposta_user <= cash_user):
		aposta_comp = aposta_user
		pote = aposta_comp + aposta_user
		print("\nSuas apostas são", aposta_user,"\n")
		ponto_carta_user = (random.randint(1,9))
		print("Você tirou um ",ponto_carta_user,"\n")
		resp_user = "s"
		while (resp_user == "s"):
			resp_user = input("Deseja tirar mais uma carta? S ou N\n")
			if (resp_user == "s"):
				N_tirado = random.randint(1,9)
				print("voce tirou um ",N_tirado,"\n")
				ponto_carta_user += N_tirado
				print("voce tem um numero de pontos igual a ",ponto_carta_user,"\n")
				if (ponto_carta_user > 21):
					print("estourou\n")
					estourou = "s"
					resp_user = "n"
		if (resp_user == "n") or (estourou == "s"):
			ponto_carta_comp += random.randint(1,9)
			ponto_carta_comp += random.randint(1,9)
			ponto_carta_comp += random.randint(1,9)
			print("Voce fez um numero de pontos igual a ",ponto_carta_user,"\n""O computador fez um numero de pontos igual a ",ponto_carta_comp,"\n")
		if (estourou == "s") and (ponto_carta_comp > 21):
			print("os dois estouraram\n")
		elif (estourou == "s") and (ponto_carta_comp < 22):
			print("voce perdeu\n")
			cash_comp += aposta_comp
			cash_user -= aposta_user
		elif (ponto_carta_user <= 21) and (ponto_carta_comp < ponto_carta_user):
			print ("voce ganhou\n")
			cash_user += aposta_comp
			cash_comp -= aposta_comp
		elif (ponto_carta_comp <= 21) and (ponto_carta_user < ponto_carta_comp):
			print("voce perdeu\n")
			cash_comp += aposta_comp
			cash_user -= aposta_user
		elif (ponto_carta_comp == ponto_carta_user):
			print("empate\n")
		aposta_comp = 0
		aposta_user = 0
		ponto_carta_comp = 0
		ponto_carta_user = 0
	else:
		print("Digite uma aposta compativel com o seu valor e/ou a do computador\n")
