print("Calculo da equação do 2ºgrau")
print("ax^2 + bx + c")
print("Digite o valor de a")
a = int(input())
print("Digite o valor de b")
b = int(input())
print("Digite o valor de c")
c = int(input())
vldelta = ((b*b)-(4*a*c))
if (vldelta < 0):
	print("o valor de delta nao é real")
else:
	rx1 = ((-b + (vldelta **(1/2)))/(2*a))
	rx2 = ((-b - (vldelta **(1/2)))/(2*a))
	print("o resultado de X1 é", rx1)
	print("o resultado de x2 é", rx2)
