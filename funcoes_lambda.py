#Lambdas sao funcoes sem nome, referenciadas pela palavra lambda

#A estrutura das funcoes lambdas sao:
# Lambda variaveis : retorno


exponencial_dos_numeros = lambda num, expo : num ** expo

print(exponencial_dos_numeros(3,2))

calc_area = lambda altura, largura : altura * largura

print(calc_area(5,3),"m2")
