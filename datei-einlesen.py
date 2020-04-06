#!/usr/bin/python3


with open('/home/best/python/einkaufsliste.csv', 'r') as fh:
    content = fh.read()


print(content)

print('---')
firstline = True
with open('/home/best/python/einkaufsliste.csv', 'r') as fh:
    for line in fh.readlines():
        if firstline is True:
            firstline = False
            continue
        print(line)
#       name = ..
#       preis = ..
        items = line.split(',')
        name = items[0][1:]
        name = name[:-1]
        preis = int(items[1])
        gewicht = int(items[2])
        gewicht = items[2]
        anzahl = items[3]
        anzahl = int(anzahl[:-1])
        print(items)
        print(f'Produkt Name: -{name}-')
        print(f'Preis: -{preis}-')
        print(f'Gewicht: -{gewicht}-')
        print(f'Anzahl: -{anzahl}-')
        print(int(gewicht) * 3)

        #nahrungsmittel = {'name': name, 'preis':preis, 'gewicht':gewicht, 'anzahl':anzahl}
        #'Milch',1,1000,4
print(einkaufsliste) Hausaufgabe einkaufsliste implimentieren dictionary liste 

print(line)
