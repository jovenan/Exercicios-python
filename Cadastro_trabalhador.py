dicionario = {}

dicionario['nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
dicionario['ctps'] = input('Carteira de trabalho: (0 se nao tem) ')
dicionario['nasc'] = nasc
dicionario['idade'] = 2020 - nasc
if dicionario['ctps'] != '0':
    dicionario['contratacao'] = int(input('Ano da contratação: '))
    dicionario['salario'] = float(input('Salario: R$'))
    dicionario['aposentadoria'] = ((dicionario['contratacao'] + 35) - 2020) + dicionario['idade']
    print('*' * 30)
    print('O nome é:{}\nO CTPS é {}\nA idade é {}\nO salario é R${}\nVai se aposentar com {}'.format(dicionario['nome'],dicionario['ctps'],dicionario['idade'],dicionario['salario'],dicionario['aposentadoria']))
    print('*' * 30)
else:
    print('*' * 30)
    print('O nome é:{}\nA idade é {}\nNao tem CTPS'.format(dicionario['nome'],dicionario['idade']))
    print('*' * 30)