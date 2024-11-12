klasse =input('Geben Sie Ihre Klasse ein')
vorname=input('Geben Sie ihren Vornamen ein')
nachname=input('Geben Sie ihren Nachnamen ein')

import csv
file1 = open('class.csv','w')
writer = csv.writer(file1, delimiter = ';')
writer.writerow(['Class', 'Forename', 'Lastname'])
writer.writerow([klasse, nachname, vorname])
file1.close()

print('Done')
inp = input('Wollen Sie weitere Daten eingeben? ')

while inp=='ja' or inp=='JA' or inp=='Ja':
    klasse = input('Geben Sie Ihre Klasse ein')
    vorname = input('Geben Sie ihren Vornamen ein')
    nachname = input('Geben Sie ihren Nachnamen ein')
    inp = input('Wollen Sie weitere Daten eingeben? ')

    import csv
    file1 = open('class.csv', 'a')
    writer = csv.writer(file1, delimiter=';')
    writer.writerow([klasse, nachname, vorname])
    file1.close()