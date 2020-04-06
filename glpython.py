#!/usr/bin/python3

name = 'Stefanie Bedra'
alter = 32
person = name
groesse = '180'

einkaufsliste = [ 'Milch', 'Butter', 'Eier', 'Brot', 'Honig', 'KÃse', 'Wurst' ]
preise = [ 1, 1, 3, 3, 2, 2, 4 ]
anzahl = [ 2, 3, 1, 1, 2, 3, 4 ]

zaehler = 0
kosten = 0
for nahrungsmittel in einkaufsliste:
    kosten = kosten + anzahl[zaehler] * preise[zaehler]
    zaehler = zaehler + 1
    if kosten > 10:
        break
    print(zaehler)
    print(kosten)
    print(nahrungsmittel)
    a = input()


print('Ende')

