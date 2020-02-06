# Gemäß dem Single-Responsibility-Prinzip hat diese Klasse nur die 
# Verantwortung die Raumfunktionalität zu realisieren.

class Raum:
    def __init__(self, name, hoehe, haus):
        #Konstruktor
        self.name = name
        self.hoehe = hoehe
        self.haus = haus
