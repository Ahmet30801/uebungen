
#1. Eine einfache Liste erstellen

# Eine Liste mit einigen Zahlen
zahlen = [1, 2, 3, 4, 5]
print(zahlen)

#2. Elemente zu einer Liste hinzufügen

# Eine Liste erstellen und ein Element hinzufügen
früchte = ["Apfel", "Banane", "Orange"]
früchte.append("Mango")
print(früchte)


#3. Auf Elemente zugreifen

# Auf das erste und dritte Element einer Liste zugreifen
tiere = ["Hund", "Katze", "Vogel"]
print(tiere[0])  # Erstes Element
print(tiere[2])  # Drittes Element

#4. Elemente aus einer Liste entfernen

# Ein Element mit remove entfernen
früchte = ["Apfel", "Banane", "Orange", "Mango"]
früchte.remove("Banane")
print(früchte)

früchte1 = ["Apfel", "Banane", "Orange", "Mango"]
remove=('Banane')
def delete(para1):
    erg= para1.remove()
    return erg

r=delete(früchte1,remove)
print(r)





#5. Länge der Liste abfragen

# Die Anzahl der Elemente in der Liste abfragen
zahlen = [1, 2, 3, 4, 5]
print(len(zahlen))

#6. Elemente sortieren

# Liste von Zahlen sortieren
zahlen = [3, 1, 4, 1, 5, 9, 2, 6]
zahlen.sort()
print(zahlen)
