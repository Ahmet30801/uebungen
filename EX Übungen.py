#Schreiben Sie eine Funktion greetWorld() ohne Rückgabewert, die "Guten Tag, Welt!"
#auf dem Bildschirm ausgibt. Rufen Sie die Funktion auf.

'''
def greetWorld():
    print("Guten Tag, Welt")
greetWorld()
'''

#Schreiben Sie eine Funktion greetPerson1(name) ohne Rückgabewert, die einen Namen als Parameter
#übergibt und dann "Guten Tag, [Name]!" auf dem Bildschirm ausgibt.
#Verwenden Sie die Funktion mit dem Namen "Anna"

'''
def greetPerson1(param1):
    print(f"Guten Tag, {param1}!")

greetPerson1("Anna")
'''

#Schreiben Sie eine Funktion greetPerson2(name) mit Rückgabewert, die einen Namen als Parameter übergibt
#und dann "Guten Tag, [Name]!" auf dem Bildschrim ausgibt.
#Verwenden Sie die Funktion mit dem Namen "Anna"

'''
def greetPerson2(name):
    ret= (f"Guten Tag, {name}!")
    return ret

r= greetPerson2("Anna")
print(r)
'''

#Schreiben Sie einen Funktion printPerson(vorname, nachname, alter) die den Vor- und Nachnamen sowie
#das alter einer Person ausgibt.

'''
def printPerson(vorname,nachname,alter):
    print(f" {vorname}, {nachname}, {alter}")

printPerson ("Ahmet", "Toplar", "23")
'''

#Schreiben Sie eine Funktion, die alle Elemente in einer Liste verdoppelt. Verwenden Sie
#die Liste zahlen = [2, 5, 8, 1, 6].

'''
zahlen= [2, 5, 8, 1, 6]
for zahl in zahlen:
    erg= zahl * 2
    print(erg)  
'''

#Schreiben Sie eine Funktion, die alle Elemente einer Liste rückwärts ausgibt. Verwenden Sie
#die Liste früchte = ["Apfel", "Banane", "Orange", "Mango"].

'''
früchte =["Apfel","Banane", "Orange", "Mango"]
früchte.reverse()
print(früchte)
'''

#Schreiben Sie eine Funktion, die das größte Element in einer Liste von Zahlen zurückgibt.
#Verwenden Sie die Liste zahlen= [15,22,3,47,9,5].

