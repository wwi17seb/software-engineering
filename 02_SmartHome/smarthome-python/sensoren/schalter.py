from sensoren.sensor import Sensor

class Schalter(Sensor):

    def setState(self, value): 
        self.zustand = value
    def messen(self):
        return self.zustand