from abc import ABC, abstractmethod 

# Diese Klasse ist abstract und wird durch die Klassen gegenstandTest getestet

# Diese Klasse dient als Grundlage für alle Gegenstände, die im Smarthome
# vorhanden sind. Sie stellt dabei Grundlegende Funktionalität zur verfügung.
class Gegenstand(ABC):

    @abstractmethod
    def __init__(self, raum, name, steuerzentrale, data = None):
        #Konstruktor
        self.standort = raum
        self.haus = self.standort.haus
        self.name = name
        self.zustand = ""
        self.steuerzentrale = steuerzentrale
        self.data = data
    
    # Diese folgenden Methoden sollen für alle weiteren Geräte und 
    # Sensoren zur Verfügung stehen. Lediglich in einigen wenigen 
    # fällen ist eine Spezifizierung der Funktionalität notwendig.
    # Auch kann so eine hohe Realisierung des Open-Closed-Prinzip 
    # realisiert werden.

    def anschalten(self):
        self.zustand = "ON"
        print("{0} ist an".format(self.name))

    def ausschalten(self):
        self.zustand = "OFF"
        print("{0} ist aus".format(self.name))
    
    def verbinden(self):
        self.steuerzentrale.gegenstandHinzu(self)
        print("{0} wurde zum System {1} hinzugefügt.".format(self.name, self.steuerzentrale.name))
      
    def smartAssistant(self):
        pass