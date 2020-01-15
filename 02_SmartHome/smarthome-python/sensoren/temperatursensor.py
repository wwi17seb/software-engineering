from sensoren.sensor import Sensor

class Temperatursensor(Sensor):
    def aenderungenUeberwachen(self):
        self.temperatur = 23.1
    
    def sendeStatus(self):
        return self.temperatur