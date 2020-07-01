print('Tabuada do numero solicidado')

number = int(input('Qual tabuada você quer saber?'))
for i in range (1, 11, 1):
    mult = number * i
    print('{}x{} = {}'.format(i,number,mult))
print('Fim.')