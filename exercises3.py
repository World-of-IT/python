#!/usr/bin/python3

def datei_einlesen(Datei):
    Liste = []
    firstline = True

    with open(Datei, 'r') as fh:
        for line in fh.readlines():
            if firstline is True
                firstline = False
                continue

            items = line.split(';')
            name = items
            name = name

            Liste.append(items[0])
            print(name[0])
            print(Liste)

datei_einlesen('/home/tn02/repos/python/network_stuff.csv')









