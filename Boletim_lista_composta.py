aluno = []
sala = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)
    sala.append(aluno[:])
    aluno.clear()
    resp = input('Deseja continuar? [s/n] ').upper()
    if resp[:1] == 'N':
        break    
print('-' * 40)
print('No.          NOME           MÉDIA')
print('-' * 40)
c = 0
while c < len(sala):
    print(f'{c:<5} -> {sala[c][0]:^10} ->{sala[c][3]:>10.2f}')
    c += 1
print('-' * 40)
decisao = 0
while decisao != 999:
    decisao = int(input('mostrar nota de qual aluno? 999 interrompe): '))
    if decisao == 999:
        break
    print(f'Notas de {sala[decisao][0]} são {sala[decisao][1]} e {sala[decisao][2]}')
    print('-' * 40)     
print('-' * 40)
print('Ate mais!')
print('-' * 40)