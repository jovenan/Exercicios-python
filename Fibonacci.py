print('Sequencia de Fibonacci!')

n = int(input("Digite o numero de elementos a serem mostrados: "))
t1 = 0
t2 = 1
cont = 3
print(t1)
print(t2)
while cont <= n:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    cont += 1
    