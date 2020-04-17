#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Produkt():

    def __init__(self, eigenschaft):
        print('Neues Produkt')
        self.attribut = eigenschaft
        
    def set_attribut(self, key, value):
        self.attribut[key] = value

    def get_attribute(self):
        return self.attribut



kiwi = Produkt({'Name': 'Kiwi', 'Farbe': 'grün'})
orangen = Produkt({'Name': 'Orange', 'Farbe': 'orange'}) 
print(kiwi.get_attribut())
print(orange.get_attribut())




