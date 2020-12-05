import math

n1 = int(input("ponto1 "))
n2 = int(input("ponto2 "))
n3 = int(input("ponto3 "))
n4 = int(input("ponto4 "))

distancia = math.sqrt(((n1-n2)**2)+((n3-n4)**2))
if distancia >= 10:
    print("longe")
else:
    print("perto")