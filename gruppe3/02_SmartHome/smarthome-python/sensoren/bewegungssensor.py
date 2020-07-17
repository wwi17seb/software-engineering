from sensoren.sensor import Sensor

class Bewegungssensor(Sensor):

    def __init__(self, gerät, raum, name, steuerzentrale, data=None):
        #Konstruktor
        super().__init__(gerät, raum, name, steuerzentrale, data=None)
        self.bewegungErkannt = False

    def messen (self):
        #bewegungUeberwachen
        bewegung = 47.11
        return bewegung

    def sendeStatus(self):
        self.bewegungErkannt = True if self.messen() != 0 else False
        return self.bewegungErkannt