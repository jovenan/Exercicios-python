'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou 
então o empréstimo será negado.
'''
print("Teste de emprestimo para Imovel\n")

value_loan = float(input("Digite o valor do imovel: R$"))
salary = float(input("Digite o seu salario: R$"))
years = int(input("Digite em quantos anos você pagara: "))
min = salary * 30 / 100
installment = value_loan / (years * 12)

print('Para pagar essa casa a prestação ficará R${:.2f}'.format(installment))
if installment <= min:
    print("Emprestimo consedido")
else:
    print("Emprestimo negado")
