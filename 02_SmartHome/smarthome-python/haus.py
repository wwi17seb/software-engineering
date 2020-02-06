# Gemäß dem Single-Responsibility-Prinzip hat diese Klasse nur die 
# Verantwortung ein Haus oder eine Wohnung abzubilden

class Haus:
    def __init__(self, name, flaeche):
        #Konstruktor
        self.name = name
        self.flaeche = flaeche
        self.raeume = list()
    
    def raumZuweisen (self, raum):
        self.raeume.append(raum)