import csv
file1 = open('class.csv','r')
reader = csv.reader(file1, delimiter = ';')
for row in reader:
    print (row)
file1.close()

inp = input('geben Sie 1 für eingeben ein und 2 für aktualisierung ein ' )

while inp == '1':
    klasse = input('Geben Sie Ihre Klasse ein ')
    vorname = input('Geben Sie ihren Vornamen ein ')
    nachname = input('Geben Sie ihren Nachnamen ein ')
    inp = input('Wollen Sie weitere Daten eingeben? ')

    file1 = open('class.csv', 'a')
    writer = csv.writer(file1, delimiter=';')
    writer.writerow([klasse, vorname, nachname])
    file1.close()


