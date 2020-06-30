print ("Digite seu nome")
nome = input()
print ("Digite sua idade")
idade = input()
if (int(idade) >= 18):
	print ("Escolha sua Bebida:")
	print ("1-skol 2-brahma 3-budweiser")
	pdt_comprado = input()
	if (int(pdt_comprado == "1")):
		pdt_comprado = "Skol"
	if (int(pdt_comprado == "2")):
		pdt_comprado = "Brahma"
	if (int(pdt_comprado == "3")):
		pdt_comprado = "Budweiser"
if (int(idade) < 18):
	print ("Escolha sua bebida:")
	print ("1-toddynho 2-leite 3-cereal")
	pdt_comprado = input()
	if (int(pdt_comprado == "1")):
		pdt_comprado = "Toddynho"
	if (int(pdt_comprado == "2")):
		pdt_comprado = "Leite"
	if (int(pdt_comprado == "3")):
		pdt_comprado = "Cereal"
print ("Quer CPF na nota? S ou N")
CPF = input()
if ((CPF == "S") or (CPF == "s")):
	print ("Digite seu CPF")
	Ncpf = input()
else:
	Ncpf = ("CPF não informado")
print ("EXTRATO")
print ("")
print (nome + " " + Ncpf + " " + pdt_comprado)
