
Person_1=["Ahmet, Toplar, 23"]
print (Person_1)

def printPerson(vorname, nachname, alter):
    print(f"mein Name ist {vorname}, {nachname}, {alter}")

printPerson("Ahmet", "Toplar", 23)
printPerson("Harun", "Kayaci", 21)

person_1=["Ahmet", "Toplar", "23"]
def getPersonAsString(person_1):
    ret = (f"vorname:{person_1 [0]} nachname:{person_1 [1]} alter:{person_1 [2]}")
    return ret

r=getPersonAsString(person_1)
print(r)
