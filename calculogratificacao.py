print ("Qual é o valor do seu salario bruto")
salbrut = float(input())
grat = ((salbrut * 5)/100)
desc = ((salbrut * 7)/100)
liq = (salbrut + grat - desc)
print("\n")
print("{:-^29}" .format("Holerite"))

#forma com varios print
#print("Salario Bruto {0:>15.2f}" .format(salbrut))
#print("gratificação {0:>14.2f}" .format(grat))
#print("Total de desconto {0:>10.2f}" .format(desc))
#print("Salario liquido é {0:>11.2f}" .format(liq))

#forma com 1 print
print("Salario Bruto {:15.2f}\nGratificação {:>14.2f}\nTotal de desconto {:>10.2f}\nSalario liquido é {:>11.2f}".format(salbrut,grat,desc,liq))
print("{:-^29}" .format(""))
