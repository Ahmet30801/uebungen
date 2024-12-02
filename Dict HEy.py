#Dictionaries (Wörterbuch) sind ein Sprachelement, welches
#Python gegenüber anderen Sprachen, wie C oder Java, hervorstellt.
#In einem Dictionary können mehrere Wertepaare, die logisch zusammengehören abgelegt werden
#Die linke Seite des Wertepaars nennt man key, die Rechte value.

#Eine Möglichkeit Dictionarys zu deklarieren, ist wiefolgt:
coffe_maker=dict(brand='Silver Chest',Volume=0.750,heater=True)
print(coffe_maker)
print(coffe_maker['brand'])
print(coffe_maker['Volume'])
print(coffe_maker['heater'])
#Der Vorteil hier ist die eindeutige Anzeige des Datentyps mit dict.
#Nachteilig ist die lange Schreibweise in deiner Zeile.

#Dagegen bietet die zweite Möglichkeit zur Deklaration genau die getauschten Vor- und Nachteile:
#nicht eindeutiger Datentyp, schreibweise über mehrere Zeilen.
thisdict = {
    'brand':'Ford',
    'model':'Mustang',
    'year':1964
}
print(thisdict)
print(thisdict['brand'])
print(thisdict['model'])
print(thisdict['year'])


#Oft wied auch eine gemischte Schreibweise verwendet:
coffe_maker=dict()
coffe_maker['brand']='Silver Chest'
coffe_maker['Volume']=0.750
coffe_maker['heater']=True
#Hier wird der Datentyp leicht lesbar festgelegt und die Paare klar mittels key und value eingefügt.
#klar mittels key und value

#Über die dritte Schreibweise können Sie auch weitere key-value schnell und einfach hinzufügen
coffe_maker['decaf']=False

#Jeder key muss in einem Dictionary eindeutig sein. Word zwei Mal der gleiche key verwendet, wird
#der value zu dem key überschrieben
coffe_maker['brand']='WMF'


#Mit dem Befehl pop können leicht keys gelöscht werden.
coffe_maker.pop('brand')

#Oft ist es hilfreich alle keys eines Dictionaries zu kennen, dafür nutzt man folgenden Befehl:
keys_of_coffe_maker=coffe_maker.keys()

#... gleiches gilt natürlich auch für die values:
values_of_coffe_maker=coffe_maker.values()

#Den value zu einem key können Sie leicht auslesen:
value=coffe_maker['brand']

#... oder:
value=coffe_maker.get('brand')