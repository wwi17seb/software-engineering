# Verwendung des design pattern Decorator

from abc import ABC, abstractmethod 
from gegenstand import Gegenstand

class Dekorierer (Gegenstand):
    def __init__(self, gegenstand):
        self.gegenstand = gegenstand
        
        self.standort = gegenstand.standort
        self.haus = self.standort.haus
        self.name = gegenstand.name
        self.zustand = ""
        self.steuerzentrale = gegenstand.steuerzentrale
        self.data = gegenstand.data

    def smartAssistant(self):
        self.gegenstand.smartAssistant()

class AlexaDekorierer (Dekorierer):
    def __init__ (self, gegenstand):
        super().__init__(gegenstand)

    def smartAssistant(self):
        print(self.name + " ist kompatibel mit Amazon Alexa")
        super().smartAssistant()

class SiriDekorierer (Dekorierer):
    def __init__ (self, gegenstand):
        super().__init__(gegenstand)

    def smartAssistant(self):
        print(self.name + " ist kompatibel mit Siri und HomeKit")
        super().smartAssistant()

class GoogleDekorierer (Dekorierer):
    def __init__ (self, gegenstand):
        super().__init__(gegenstand)

    def smartAssistant(self):
        print(self.name + " ist kompatibel mit Google Home")
        super().smartAssistant()