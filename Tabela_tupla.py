Prod_precos = ('lapis', 1.99,
                'cadernos', 7.5,
                'Mochila', 59,
                'Martelo', 39.9,
                'prego', 3,
                'Rejunte', 6)
print('Tabela')
print('-' * 40)
i = 0
while i <= len(Prod_precos[i]):
    print(f'{Prod_precos[i]:.<25} R$', "", end = "")
    print(f'{Prod_precos[i + 1]:>.2f}')
    i += 2
print('-' * 40)