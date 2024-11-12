'''inp=int(input('Please enter a number between 1 and 100: '))
while inp<0 or inp>100:
    print('Please enter a number between 1 and 100 and not anything else')
    break

while True:
    inp = input('Please enter a new number between 1 and 100: ')
    inp = int(inp)

    if inp==0:
        print('System error')
        break

    elif inp<1 or inp>100:
        print('Please enter a number between 1 and 100 and not anything else')
        continue'''

import random
num1= random.randint(0,100)
i=1

num2=int(input("Geben Sie eine Zahl zwischen 0 und 100 ein:  "))

if num2 < 1 or num2 > 100:
    print("Programmabruch, Zahl ist kleiner 0 oder größer 100")
else:
    while num2 != num1:
        i=i+1
        if num2 < 1 or num2 > 100:
            print("Programmabruch, Zahl ist kleiner 0 oder größer 100")
            break
        elif num2 >num1+10 or num2 <num1-10:
            print("Sie liegen weit daneben!")
            num2=int(input("Geben Sie eine neue Zahl ein:  "))
        elif num2 > num1-10 or num2 <num1+10:
            print("Sie liegen leicht daneben")
            num2=int(input("Geben Sie eine neue Zahl ein:  "))
    else:
        print(f"Sie haben {i} Schritte gebraucht um die Zahl zu erraten.")