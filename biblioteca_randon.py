import random

num = (random.randint(1,10))
print("A soma do seu numero mais o da maquina \n")
print("Digite um numero")
num_user = int(input())
print ("par ou impar? {P ou I}")
esc = input()
soma = num + num_user
rest = (soma%2)
if (rest == 0):
	p_i = "par"
	rst = "ganhou"
else:
	p_i = "impar"
	rst = "perdeu"
print("{0:-^21}".format("Resultado"))
#forma com 1 print
print("Seu Nº {:>14.2f}\nNº do comp {:>10.2f}\nSoma {:>16.2f}\nVocê {:>1.8} Deu {:>1.8}".format(num_user,num,soma,rst,p_i))
#forma com varios print
#print("Seu Nº","{:>14.2f}" .format(num_user))
#print("Nº do comp","{:>10.2f}".format(num))
#print("Soma","{:>16.2f}\n".format(soma))
#print("Você {0:>1.8} Deu {1:>1.8}".format(rst,p_i))

print("{0:-^21}".format(""))
