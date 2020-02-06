from sensoren.sensor import Sensor

# der Feuermelder wird von der Klasse Sensor abgeleitet
class Feuermelder(Sensor):
    # Hier wurde die Funktion "messen" definiert und funktional
    # an die Anforderungen an den Feuermelder angepasst.
    def messen(self):
        return True
    
    # Es soll durch den Feuermelder Dauerhaft geprüft werden, ob
    # es brennt oder nicht, daher müsste hier eine Endlosschleife eingesetzt werden.
    def feuerÜberwachen(self):
        if(True): #while(True):
            if self.messen():
                self.sendeStatus(True)


    # So bald ein Feuer erkannt wurde, soll dies an die Außenwelt
    # weitergegeben werden.
    def sendeStatus(self, value):
        if value:
            print('Feuer wurde erkannt!!!')
        else:
            print('Kein Feuer wurde erkannt!')