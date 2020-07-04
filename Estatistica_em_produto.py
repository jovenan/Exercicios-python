print('Mercadinho!')
gasto = 0
produtos_mais_mil = 0
mais_barato = ''
prod_mais_barato = 0
n = 1
while n != 99999:
    continuar = input('Deseja adicionar um produto? [Sim ou Nao]\n').upper()
    if continuar[:1] == 'N':
        break
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$'))
    gasto += preco
    if n == 1:
        mais_barato = preco
        prod_mais_barato = nome
        n += 1
    if preco >= 1000:
        produtos_mais_mil += 1
    if preco < mais_barato:
        prod_mais_barato = nome
        mais_barato = preco
print('Seu gasto total deu R${:.2f}, \n{} Produtos custam mais de R$1000.00,\nO produto mais barato é o {} que custou R${:.2f}.'.format(gasto,produtos_mais_mil,prod_mais_barato,mais_barato))
