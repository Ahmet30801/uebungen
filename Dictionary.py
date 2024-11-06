#Dictionaries (Wörterbuch) sind ein Sprachelement, welches Python gefenüber anderen Sprachen,
#wie C oder Java, hervorstellt. In einem Dictionary können mehrere Wertepaare, die logisch
#zusammen gehören abgelegt werden. Die linke Seite des Wertepaars nennt man Key, die Rechte value.

#Eine Möglichkeit Dictionaries zu deklarieren, ist wiefolgt:

coffee_maker= dict(brand = "Silver Crest", volume = 0.750, heater = True)

#Der Vorteil hier ist die eindeutige Anzeige des Datentyps mit dict.
#Nachteilig ist die lange Schreibweise in einer Zeile.

#Dagegen bietet die zweite Möglichkeit zur Deklaration genau die
#getauschten Vor- und Nachteile: nicht eindeutiger Datentyp, schreibweise über mehrere Zeilen.

coffee_maker= {"brand" : "Silver Crest",
               "volume": 0.750,
               "heater": True}

#Oft wird auch eine gemischte Schreibweise verwendet.

coffee_maker = dict()
coffee_maker["brand"] = "Silver Crest"
coffee_maker["volume"] = 0.750
coffee_maker["heater"] = True

#Hier wird der Datentyp leicht lesbar festgelegt und die Paare klar mittels key und value eingefügt.

#Über die dritte Schreibweise können Sie auch weitere key-value Paare schnell und einfach hinzufügen:
coffee_maker["decaf"] = False

#Jeder key muss in einem Dictionary eindeutig sein. Wird zwei mal der gleiche key verwendet,
#wird der Value zu dem key überschrieben.#
coffee_maker["brand"] = "WMF"

#Den value zu einem Key können Sie leicht auslesen:
value= coffee_maker["brand"]

#... oder:
value = coffee_maker.get("brand")

#Mit dem Befehl pop können leicht keys gelöscht werden

coffee_maker.pop("brand")

#Oft ist es hilfreich alle keys einen Dictionary zu kennen, dafür nutzt man folgenden Befehl:
keys_of_coffee_maker = coffee_maker.keys()

#... gleiches gilt für die values

values_of_coffee_maker = coffee_maker.values()

