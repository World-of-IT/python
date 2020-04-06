#!/usr/bin/python3

produkt0 = {'Name': 'Milch',
                'Preis': 1,
                'Anzahl': 2}

produkt1 = {'Name': 'Butter',
            'Preis': 1,
            'Anzahl': 2}

produkt2 = {'Name': 'Eier',
            'Preis': 3,
            'Anzahl': 1}

produkt3 = {'Name': 'Brot',
            'Preis': 3,
            'Anzahl': 1}

produkt4 = {'Name': 'Honig',
            'Preis': 2,
            'Anzahl': 2}

produkt5 = {'Name': 'Kaese',
            'Preis': 2,
            'Anzahl': 3}

produkt6 = {'Name': 'Wurst',
            'Preis': 4,
            'Anzahl': 4}


einkaufsliste = [ produkt0, produkt1, produkt2, produkt3, produkt4, produkt5, produkt6 ]


Geld = input('Wieviel Geld willst du heute ausgeben?[Betrag]'
Geld = int(Geld)
zaehler = 0
kosten = 0
for nahrungsmittel in einkaufsliste:
    produktkosten = nahrungsmittel['Anzahl'] * nahrungsmittel['Preis']
    kosten = kosten + produktkosten
    if kosten > Geld:
        break
        print(f'Sie kauften {nahrungsmittel["Anzahl"]} * {nahrungsmittel["Name"]} a {nahrungsmittel["Preis"]}, fuer  {produktkosten}Euro, Gesamtpreis: {kosten}Euro' )
    print(zaehler)
    print(kosten)
    print(nahrungsmittel)
    a = input()
