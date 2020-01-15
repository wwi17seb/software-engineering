from sensoren.sensor import Sensor

class Feuermelder:
    def feuerUeberwachen(self):
        self.feuerErkannt = True
    
    def sendeStatus(self):
        if self.feuerErkannt:
            return 'Feuer wurde erkannt!!!'
        else:
            return 'Kein Feuer wurde erkannt!'