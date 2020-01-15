from sensoren.sensor import Sensor

class Bewegungssensor(Sensor):

    def __init__(self, data = None):
        #Konstruktor
        self.data = data
        self.bewegungErkannt = False

    def messen (self):
        #bewegungUeberwachen
        bewegung = 47.11
        return bewegung

    def sendeStatus(self):
        self.bewegungErkannt = True if self.messen() != 0 else False
        return self.bewegungErkannt