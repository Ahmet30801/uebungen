'''
#Aufgabe1
zahlen=[5,3,8,2,10]
summe = 0
for zahl in zahlen:
    summe += zahl
print(summe)

#Aufgabe2

zahlen2= [15, 22, 3, 47, 9, 5]
temp=0
for zahl in zahlen2:
    if temp <= zahl:
        temp=zahl
print(temp)

#Aufgabe3

zahlen3=[4,2,4,6,4,7,8,4,1]
for i in range(9):
    res= zahlen3.count(i)
    if res >= 0:
      print (f"Die Zahl {i} kommt {res} mal vor")

#Aufgabe4

zahlen4=[2, 5, 8, 1, 6]
for zahl in zahlen4:
    erg= zahl *2
    print(f"Die Zahl {zahl} ist verdoppelt {erg}")


#Aufgabe5

fruechte=["Apfel", "Banane", "Organe", "Mango"]
fruechte.reverse()
print(fruechte)


#Aufgabe6

zahlen5=[12, 7, 9, 16, 18, 21, 30]
for zahl in zahlen5:
    if zahl % 2 == 0:
        print(zahl,end=";")

print('\n')
#Aufgabe7

zahlen6=[1, 4, 7, 10]
for zahl in zahlen6:
    summe = zahl*3
    print(summe)

'''
#ExtraAufgabe
'''
zahlen7=[1, 4, 7, 10]
zahlen8=[3, 5, 2, 6]

for zahl1 in zahlen7:
    for zahl2 in zahlen8:
        summe = zahl1*zahl2
    print(summe)
'''

lst_1= list(range(1,101))
print(lst_1)
lst_2= [x*x+x for x in lst_1]
print(lst_2)


def quadrat(list3):
    return list3*list3+list3

lst4 = range(1,101)
ergebnis = list(map(quadrat, lst4))
print(ergebnis)











