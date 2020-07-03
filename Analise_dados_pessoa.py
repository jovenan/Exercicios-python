print('Cadastro')
mais_de_18 = 0
mulheres_menos_20 = 0
homens = 0
while True:
    parar = input('Se voce deseja parar de cadastrar escreva parar, ou escreva qualquer coisa para continuar.\n').upper()
    if parar[:1] == 'P':
        break
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo.[M ou F] ').upper()
    if idade > 18:
        mais_de_18 += 1
    if sexo == 'F' and idade < 21:
        mulheres_menos_20 += 1
    if sexo == 'M':
        homens += 1
print('Cadastro parado...\nVocê cadastrou {} pessoa(s) com mais de 18 anos, {} homem(ns), {} mulher(s) com mais de 20 anos.'.format(mais_de_18,homens,mulheres_menos_20))
