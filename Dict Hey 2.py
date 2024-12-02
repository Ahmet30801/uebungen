# Übung 2:
# Erstellen Sie ein Wörterbuch mit der Zuordnung von
# Vor- auf Nachnamen. So ist beispielsweiße "Hans"
# der Key und "Müller" der Value.
from cgi import print_arguments

# 1) Erstellen Sie ein entsprechendes Wörterbuch mit
#    mindestens fünf Einträgen.
dict_of_names = dict()
dict_of_names["Hans"] = "Müller"
dict_of_names["Anna"] = "Schmidt"
dict_of_names["Peter"] = "Meier"
dict_of_names["Lisa"] = "Bauer"
dict_of_names["Max"] = "Koch"
print(dict_of_names)
# 2) Schreiben Sie eine Funktion, welche den Benutzer
#    nach den Vornamen fragt und den Nachnamen ausgibt.
def pername_to_lastname_2(names):
    key = input("Geben Sie den Vornamen ein: ")

    line = dict_of_names[key] + ", " + key

    print(line)
pername_to_lastname_2(dict_of_names)
# 3) Erweitern Sie die Funktion aus 2) um eine Fehler-
#    behandlung. Wird ein Vorname, der nicht in dem
#    Wörterbuch ist eingegeben, erscheint der Text:
#    "Prename not found in dict."
def pername_to_lastname_3(names):
    key = input("Geben Sie den Vornamen ein: ")

    if not key in dict_of_names:
        print("Prename not found in dict.")

        return

    line = dict_of_names[key] + ", " + key

    print(line)
pername_to_lastname_3(dict_of_names)
# 4) Erweitern Sie die Funktion aus 3) um eine Abfrage-
#    bei fehlenden Vornamen. Wird ein Vorname nicht ge-
#    gefunden, wird der Benutzer nach dem Nachnamen ge-
#    fragt und das neue Namespaar in das dict eingefügt.
def pername_to_lastname(names):
    key = input("Geben Sie den Vornamen ein: ")

    if not key in dict_of_names:
        print("Prename not found in dict.")

        value = input("Geben Sie den Nachnamen ein: ")

        names[key]  = value

    line = dict_of_names[key] + ", " + key

    print(line)
pername_to_lastname(dict_of_names)
# 5) Implementieren Sie eine weitere Funktion, welche alle
#    Nachnamen (und nur die Nachnamen) ausgibt.
def print_lastnames(names):
    for value in names.values():
        print(value)

# 6) Erweitern Sie 5) indem die Nachnamen alphabetisch
#    sortiert sind.
def print_lastnames(names):
    sorted_names=sorted(dict_of_names.values())

    for value in sorted_names:
        print(value)

# 7) Erweitern Sie 6) so, dass zu den Nachnamen, die zu-
#    gehörigen Vornamen ausgegeben werden.
    sortiertes_dict = dict(sorted(dict_of_names.items(), key=lambda values: values[1]))
    print(sortiertes_dict)

print_lastnames(dict_of_names)
#or
def print_pre_and_lastnames(names):
    sorted_names = sorted(names.values())
    for value in sorted_names:
        for key in names.keys():
            if names[key] == value:
                print(value + ", " + key)
                break

print_pre_and_lastnames(dict_of_names)