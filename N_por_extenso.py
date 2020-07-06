contagem = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
num = int(input('Digite um numero de 0 a 20 '))
while True:
    if num < 0 or num > 20:
        num = int(input('Digite um numero de 0 a 20! '))
    if num > -1 and num < 21:
        break
print(f'O numero que você digitou foi o {contagem[num]}')