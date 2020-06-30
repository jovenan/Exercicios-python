import random
import os
from time import sleep

xpc = str(random.randint(1, 3))
ypc = str(random.randint(1, 3))
print('randomico ' + str(xpc) + ',' + str(ypc))

c11 = False
c12 = False
c13 = False
c21 = False
c22 = False
c23 = False
c31 = False
c32 = False
c33 = False

x = 1
while x <= 3:
    y = 1
    while y <= 3:
        print('\033[' + str(x+1) + ';' + str(y * 8) + 'H'+ str(x)+','+ str(y))
        sleep(0.2)
        y+=1
    x += 1

xus = input('digite seu valor x:')
yus = input('digite seu valor y:')
os.system('clear')



if xus == 1 and yus == 1:
    c11 = True
elif xus == 1 and yus == 2:
    c12 = True
elif xus == 1 and yus == 3:
    c13 = True
elif xus == 2 and yus == 1:
    c21 = True
elif xus == 2 and yus == 2:
    c22 = True
elif xus == 2 and yus == 3:
    c23 = True
elif xus == 3 and yus == 1:
    c31 = True
elif xus == 3 and yus == 2:
    c32 = True
elif xus == 3 and yus == 3:
    c33 = True
    

while str(xpc) != str(xus) or str(ypc) != str(yus):
    x = 1
    while x <= 3:
        y = 1
        while y <= 3:
            if c11 == True and x == 1 and y == 1:
                print('\033[' + str(x+1) + ';' + str(y * 8) + 'HX,X')
            elif c12 == True and x == 1 and y == 2:
                print('\033[' + str(x+1) + ';' + str(y * 8) + 'HX,X')
            elif c13 == True and x == 1 and y == 3:
                print('\033[' + str(x+1) + ';' + str(y * 8) + 'HX,X')
            elif c21 == True and x == 2 and y == 1:
                print('\033[' + str(x+1) + ';' + str(y * 8) + 'HX,X')
            elif c22 == True and x == 2 and y == 2:
                print('\033[' + str(x+1) + ';' + str(y * 8) + 'HX,X')
            elif c23 == True and x == 2 and y == 3:
                print('\033[' + str(x+1) + ';' + str(y * 8) + 'HX,X')
            elif c31 == True and x == 3 and y == 1:
                print('\033[' + str(x+1) + ';' + str(y * 8) + 'HX,X')
            elif c32 == True and x == 3 and y == 2:
                print('\033[' + str(x+1) + ';' + str(y * 8) + 'HX,X')
            elif c33 == True and x == 3 and y == 3:
                print('\033[' + str(x+1) + ';' + str(y * 8) + 'HX,X')
            else:
                print('\033[' + str(x+1) + ';' + str(y * 8) + 'H' + str(x) + ',' + str(y))
            y += 1
        x += 1
        sleep(0.1)
    xus = input('digite seu valor x:')
    yus = input('digite seu valor y:')
    os.system('clear')
    
    if xus == 1 and yus == 1:
        c11 = True
    elif xus == 1 and yus == 2:
        c12 = True
    elif xus == 1 and yus == 3:
        c13 = True
    elif xus == 2 and yus == 1:
        c21 = True
    elif xus == 2 and yus == 2:
        c22 = True
    elif xus == 2 and yus == 3:
        c23 = True
    elif xus == 3 and yus == 1:
        c31 = True
    elif xus == 3 and yus == 2:
        c32 = True
    elif xus == 3 and yus == 3:
        c33 = True
        
x=1
while x <= 3:
    y = 1
    while y <= 3:
        if xpc == str(x) and ypc == str(y):
            print('\033['+ str(x+1)+';'+str(y*8)+'H@,@')
        else:
            print('\033['+ str(x+1)+ ';'+ str(y*8)+'HX,X')
        y+=1
    x+=1

