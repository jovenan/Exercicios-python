'''
A Confederação Nacional de Natação precisa de um
programa que leia o ano de nascimento de um atleta 
e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''

import datetime

print('Digite seu ano de nascimento para saber sua categoria\n')

data = datetime.datetime.today()
year_birth = int(input('ano de nascimento: '))

years = int(data.year) - int(year_birth)
if years < 10:
    category = "MIRIM"
elif years < 15:
    category = "INFANTIL"
elif years < 20:
    category = "JUNIOR"
elif years < 26:
    category = "SENIOR"
else:
    category = "MASTER"    

print('Sua categoria na natação é {}'.format(category))