num1 = int(input("num1:"))
num2 = int(input("num2:"))
num3 = int(input("num3:"))

if num1 < num2:
    if num2 < num3:
        print("crescente")
    else:
        print("não está em ordem crescente")
else:
    print("não está em ordem crescente")