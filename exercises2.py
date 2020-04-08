#!/usr/bin/python3

Datei = '/home/tn02/repos/python/network_stuff.csv'
Liste = []
firstline = True
def datei_einlesen(Datei):
    Liste2 = []
with open(Datei, 'r') as fh:
    for line in fh.readlines():
        if firstline is True:
            firstline = False
            continue

        items = line.split(';')
        adress = (item[0])
        private = [1]
        network = [2]
        broadcast = [3]
        netmask = [4]
        hosts = [5]
        ipv6 = [6]
        bin = [7]
        adresstype = {'adress': adress, 'private': private, 'network': network, 'broadcast': broadcast, 'netmask': netmask, 'hosts': hosts, 'ipv6': ipv6, 'bin': bin}
print(Liste)

        Liste2.append(adresstype)
return  Liste2


Liste = datei_einlesen('/home/tn02/repos/python/network_stuff.csv')

