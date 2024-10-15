#Schreiben Sie eine Funktion greetWorld() ohne Rückgabewert, die "Guten Tag, Welt!"
#auf dem Bildschirm ausgibt. Rufen Sie die Funktion auf.


def greetWorld():
    print("Guten Tag, Welt")
greetWorld()


#Schreiben Sie eine Funktion greetPerson1(name) ohne Rückgabewert, die einen Namen als Parameter
#übergibt und dann "Guten Tag, [Name]!" auf dem Bildschirm ausgibt.
#Verwenden Sie die Funktion mit dem Namen "Anna"


def greetPerson1(param1):
    print(f"Guten Tag, {param1}!")

greetPerson1("Anna")


#Schreiben Sie eine Funktion greetPerson2(name) mit Rückgabewert, die einen Namen als Parameter übergibt
#und dann "Guten Tag, [Name]!" auf dem Bildschrim ausgibt.
#Verwenden Sie die Funktion mit dem Namen "Anna"


def greetPerson2(name):
    ret= (f"Guten Tag, {name}!")
    return ret

r= greetPerson2("Anna")
print(r)


#Schreiben Sie einen Funktion printPerson(vorname, nachname, alter) die den Vor- und Nachnamen sowie
#das alter einer Person ausgibt.


def printPerson(vorname,nachname,alter):
    print(f" {vorname}, {nachname}, {alter}")

printPerson ("Ahmet", "Toplar", "23")


#Schreiben Sie eine Funktion, die alle Elemente in einer Liste verdoppelt. Verwenden Sie
#die Liste zahlen = [2, 5, 8, 1, 6].


zahlen= [2, 5, 8, 1, 6]

def verdoppeln(zahlen):
    for zahl in zahlen:
        erg= zahl * 2
        print(erg)

verdoppeln(zahlen)

#Schreiben Sie eine Funktion, die alle Elemente einer Liste rückwärts ausgibt. Verwenden Sie
#die Liste früchte = ["Apfel", "Banane", "Orange", "Mango"].


fruechte =["Apfel","Banane", "Orange", "Mango"]
def backwards(fruechte):
    fruechte.reverse()
    print(fruechte)

backwards(fruechte)

#Schreiben Sie eine Funktion, die das größte Element in einer Liste von Zahlen zurückgibt.
#Verwenden Sie die Liste zahlen= [15,22,3,47,9,5].

zahlen =[15, 22, 3, 47, 9, 5]

def groesste(zahlen):
    print(max(zahlen))

groesste(zahlen)

#Schreiben Sie eine Funktion, die alle geraden Zahlen aus einer Liste zurückgibt.
#Verwenden Sie die Liste zahlen = [12,7,9,16,18,21,30]

zahlen= [12, 7, 9, 16, 18, 21, 30]
def gerade(zahlen):
    for x in zahlen:
         if x % 2 == 0:
             print(x)

gerade(zahlen)