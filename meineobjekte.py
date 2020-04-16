#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Person():
    name = ''

    def laufen (self, geschwindigkeit, richtung):
        print(f'Ich kann {geschwindigkeit} {richtung} laufen')

    def gehen (self, geschwindigkeit, richtung):
        print(f'Ich kann {geschwindigkeit} {richtung} gehen')

    def springen (self, höhe):
        print(f'Ich kann {höhe} hoch springen')

Peter = Person()


Peter.name = 'Peter'
print(Peter.name)
Peter.laufen(' langsam', 'vorwaerts')

Claudia = Person()
Claudia.name = 'Claudia'
print(Claudia.name)
Claudia.gehen('schnell', 'rueckwaerts')

Udo = Person()
Udo.name = 'Udo'
print(Udo.name)
Udo.springen('3 Meter')

