# Gemäß dem Single-Responsibility-Prinzip hat diese Klasse nur die 
# Verantwortung die Netzwerkfunktionalität zu realisieren.

class Netzwerk:

    def __init__(self, name, zugangsdaten, netzwerkSettings):
        #Konstruktor
        self.name = name
        self.zugangsdaten = zugangsdaten
        self.netzwerkSettings = netzwerkSettings
        self.sichtbar = False
        self.steuerzentralen = list()

    def oeffentlichStellen(self):
        self.sichtbar = True
    
    def privatStellen(self):
        self.sichtbar = False
    
    def verbindeSteuerzentrale(self, steuerzentrale):
        self.steuerzentralen.append(steuerzentrale)