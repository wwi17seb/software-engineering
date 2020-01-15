from abc import ABC, abstractmethod 

class Gegenstand(ABC):

    def __init__(self, raum, name, steuerzentrale, data = None):
        #Konstruktor
        self.standort = raum
        self.haus = self.standort.haus
        self.name = name
        self.zustand = ""
        self.steuerzentrale = steuerzentrale
    
    def anschalten(self):
        self.zustand = "ON"
        print("{0} ist an".format(self))

    def ausschalten(self):
        self.zustand = "OFF"
        print("{0} ist aus".format(self))
    
    def verbinden(self):
        self.steuerzentrale.gegenstandHinzu(self)
        print("{0} wurde zum System hinzugefügt.".format(self))