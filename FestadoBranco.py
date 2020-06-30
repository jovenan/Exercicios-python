print ("Festa do branco, vermelho e rosa")
cor_camisa = input("Qual a cor da sua camisa?")
idade = int(input ("Qual a sua idade?"))
sexo = input ("Digite seu sexo: {M/F}")

if (idade < 18):
	print("Você não pode entrar!")
elif ((sexo == "M") or (sexo == "m") and (cor_camisa == "rosa") or (cor_camisa == "Rosa") and (idade < 21)):
	print("Entra!")
elif ((sexo == "F") or (sexo == "f")) and ((cor_camisa == "vermelho") or (cor_camisa == "Vermelho")):
	print("Entra!")
elif ((sexo == "F") or (sexo == "f") and ((cor_camisa == "branco") or (cor_camisa == "Branco")) and (idade > 30)):
	print("Você não pode entrar!")
elif ((sexo == "M") or (sexo == "m") and (cor_camisa == "rosa") or (cor_camisa == "Rosa") and (idade > 40)):
	print("Entra!")
elif ((sexo == "F") or (sexo == "f") and (cor_camisa == "vermelho") or (cor_camisa == "Vermelho") and (idade == 32)):
	print("Entra! Você é Vip!")
else:
	print("Você não pode entrar!")
