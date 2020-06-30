

N = "Samuel"
i = 25
print ("nome: {} idade: {}".format(N,i))
#indice: preencher / alinhar / largura / .precisão/
print ("nome {0:*^18.8} , idade {1}" .format(N,i))

#para strings
#indice : preencher/ alinhar/ largura/ .precisao
			#			<>^		10		.2

#para Numeros
#indice : preencher/ alinhar/ sinal/ largura/ .precisao/          tipo
			#			<>^		+     10		casas decimais		decimal, etc

#d = decimal  		f = float			s = string 		b = binario		o = octa    h = hexa


sol = 1500.555

print ("{:^+10.4f}".format(sol))

print ("{0:#^18.2f}" .format(sol))
