num = int(input('Digite um numero para saber a fatorial: '))
i = num

while i > 1:
    i -= 1
    num = num * i
print('o fatorial é {}'.format(num))

"OU"
from math import factorial

num = int(input('Digite um numero para saber a fatorial: '))
num = factorial(num)
print('o fatorial é {}'.format(num))
