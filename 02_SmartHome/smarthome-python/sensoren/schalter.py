from sensoren.sensor import Sensor

class Schalter(Sensor):
    def __init__(self, gerät, name, data = None):
        #Konstruktor
        super().__init__(gerät,gerät.standort, name, gerät.steuerzentrale, data=None)
        self.zustand = False

    # Der Schalter auch einen Zustand annehmen können soll,
    # wird hier die Klasse um eine Funktionalität erweitert.
    def setState(self, value): 
        self.zustand = value

    # Der Schalter gibt beim Aufruf dieser Funktion
    # seinen Zustand zurück, also ob dieser Ein- oder
    # Ausgeschaltet ist.
    def messen(self):
        return self.zustand