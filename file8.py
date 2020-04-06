#!/usr/bin/python3


teilnehmer = [
     {"first": "Erna", "last": "Mayer"},
     {"first": "Fred", "last": "Tischler"},
     {"first": "Karsten", "last": "Schmidt"}]


zaehler = 0
for dings in teilnehmer:
    zaehler = zaehler + 1
    print(zaehler)
    print(dings["first"])
    print("-"*10)



