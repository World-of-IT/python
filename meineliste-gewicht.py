#!/usr/bin/python3

produkt0 = {'Name': 'Milch',
                'Preis': 1,
                'Anzahl': 2,
                'Gewicht': 0.5}

produkt1 = {'Name': 'Butter',
            'Preis': 1,
            'Anzahl': 2,
            'Gewicht': 0.2}

produkt2 = {'Name': 'Eier',
            'Preis': 3,
            'Anzahl': 1,
            'Gewicht': 0.7}

produkt3 = {'Name': 'Brot',
            'Preis': 3,
            'Anzahl': 1,
            'Gewicht': 0.5}

produkt4 = {'Name': 'Honig',
            'Preis': 2,
            'Anzahl': 2,
            'Gewicht': 0.4}

produkt5 = {'Name': 'Kaese',
            'Preis': 2,
            'Anzahl': 3,
            'Gewicht': 0.5}

produkt6 = {'Name': 'Wurst',
            'Preis': 4,
            'Anzahl': 4,
            'Gewicht': 0.5}


einkaufsliste = [ produkt0, produkt1, produkt2, produkt3, produkt4, produkt5, produkt6 ]


Geld = input('Wieviel Geld willst du heute ausgeben?[Betrag]')
Geld = int(Geld)
Gewicht = input('Wieviel kannst du tragen?[kg]')
Gewicht = int(Gewicht)

zaehler = 0
kosten = 0
einkaufsgewicht = 0
for nahrungsmittel in einkaufsliste:
    if kosten > Geld or einkaufsgewicht > Gewicht:
        break
    produktkosten = nahrungsmittel['Anzahl'] * nahrungsmittel['Preis']
    kosten = kosten + produktkosten
    produktgewicht = nahrungsmittel['Anzahl'] * nahrungsmittel['Gewicht']
    einkaufsgewicht = einkaufsgewicht + produktgewicht
    if einkaufsgewicht > Gewicht:
        break
    if kosten > Geld:
        break
    print(f'Sie kauften {nahrungsmittel["Anzahl"]} * {nahrungsmittel["Name"]} a {nahrungsmittel["Preis"]}€, fuer {produktkosten}€, Gesamtpreis: {kosten}€ {produktgewicht}')
    zaehler = zaehler + 1

    print(zaehler)
    print(kosten)
    print(einkaufsgewicht)
    print(nahrungsmittel)
    a = input()
