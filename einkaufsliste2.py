#!/usr/bin/python3

name = 'Stefanie Bedra'
alter = 32
person = name
groesse = '180'

#einkaufsliste = [ 'Milch', 'Butter', 'Eier', 'Brot', 'Honig', 'Käse', 'Wurst' ]


produkt0 = {'Name': 'Butter',
            'Preis': 1,
            'Anzahl': 4}

produkt1 = {'Name': 'Butter',
            'Preis': 1,
            'Anzahl': 2}

produkt2 = {'Name': 'Eier',
            'Preis': 3,
            'Anzahl': 1}

einkaufsliste = [ produkt0, produkt1, produkt2 ]




# einlesen der Daten aus einer CSV Datei
def datei_einlesen(Datei)
    einkaufsliste = []
    firstline = True
    with open(Datei, 'r')) as fh:
          for line in fh.readlines():
              if firstline is True:
                  firstline = False
                    continue
          print(line)
          line = line.replace('\n','')
          items = line.split(',')
 #        name = items[0][1:]
 #        name = name[:-1]
  
          name    = items[0].replace ("'","")
          preis   = int(items[1])
          gewicht = int(items[2])
          anzahl  = int(items[3])
  
datei_einlesen('/home/best/python/einkaufsliste.csv', 'r')

          einkaufsliste.append({'Name': name, 'Preis':preis, 'Gewicht':gewicht, 'Anzahl':anzahl})


Geld = input('Wieviel Geld willst du heute ausgeben?[Betrag]')
Geld = int(Geld)
Gewicht = input('Wieviel kannst du tragen?[kg]')
Gewicht = int(Gewicht)

zaehler = 0
kosten = 0
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
      print(f'Sie kauften {nahrungsmittel["Anzahl"]} * {nahrungsmittel["Name"]} a {nahrungsmittel["    Preis"]}€, fuer {produktkosten}€, Gesamtpreis: {kosten}€ {produktgewicht}')
     zaehler = zaehler + 1 
      print(zaehler)
      print(kosten)
      print(einkaufsgewicht)
      print(nahrungsmittel)
      a = input()                   
