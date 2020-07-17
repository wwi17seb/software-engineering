from sensoren.sensor import Sensor

class Temperatursensor(Sensor):
    def aenderungenUeberwachen(self):
        self.temperatur = 23.1
    
    def messen(self):
        self.aenderungenUeberwachen()
        return self.temperatur