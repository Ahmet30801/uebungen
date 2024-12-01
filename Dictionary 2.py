# Erstellen Sie ein Wörterbuch mit der Zuordnung von
# Vor- auf Nachnamen. So ist beispielweise "Hans"
# der Key und "Müller" der Value.
from distutils.command.install import value

from Dictionary import keys_of_coffee_maker

# 1) Erstellen Sie ein entsprechendes Wörterbuch mit mindestens fünf Einträgen.

dict_names = dict()
dict_names ['Ahmet'] = 'Toplar'
dict_names ['Harun'] = 'Kayaci'
dict_names ['Musti'] = 'Demiral'
dict_names ['Batu'] = 'Aktürk'
dict_names ['Hans'] = 'Müller'

print(dict_names)

# 2) Schreiben Sie eine Funktion, welche den Benutzer nach den Vornamen fragt und den Nachnamen ausgibt.
'''
pername_to_lastname = input('Geben Sie einen Vornamen ein ')

if pername_to_lastname in dict_names:
    value = dict_names[pername_to_lastname]
    print(value)'''


def pername_to_lastname(names):
    key = input("Geben Sie den Vornamen ein: ")

    line = dict_names[key] + ', ' + key

    print(line)

pername_to_lastname(dict_names)

#3) Erweitern Sie die Funktion aus 2) um eine Fehlerbahndlung. Wird ein Vorname, der nicht in dem
# Wörterbuch ist eingegeben, erscheint der Text: 'Prename not found in dict'


def pername_to_lastname(names):
    pername_to_lastname = input("Geben Sie den Vornamen ein: ")
    if pername_to_lastname in dict_names:
        value = dict_names[pername_to_lastname]
        print(value)

    else:
        print('Prename not found')

pername_to_lastname(dict_names)


#4) Erweitern Sie die Funktion aus 3) um eine Abfrage bei fehlenden Vornamen.
# Wird ein Vorname nicht gefunden, wird der Benutzer nach dem Nachnamen gefragt und
# das neue Namenspaar in das dict eingefügt.

def prename_to_lastname(names):
    key = input("Geben Sie den Vornamen ein: ")

    if not key in dict_names:
        print('Prename not found')

        value = input ('Geben sie den Nachnamen ein ')

        names[key] = value

    line= dict_names[key] + ', ' + key

    print(line)

# 5) Implementieren Sie eine weitere Funktion, welche alle
# Nachnamen (und nur die Nachnamen) ausgibt.

def print_lastnames (names):
    for value in names.values():
        print(value)

print_lastnames(dict_names)

# 6) Erweitern Sie 5) indem die Nachnamen alphabetisch sortiert wird.

