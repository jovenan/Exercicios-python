num = int(input('Digite o valor de n: '))
i = num

if num == 0 or num == 1:
    print("1")
else:
    while i > 1:
        i -= 1
        num = num * i
    print(num)


#from math import factorial

#num = int(input('Digite um numero para saber a fatorial: '))
#num = factorial(num)
#print('o fatorial é {}'.format(num))
