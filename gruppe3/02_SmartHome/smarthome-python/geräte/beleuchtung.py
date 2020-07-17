from geräte.gerät import Gerät

class Beleuchtung(Gerät):
    
    def __init__(self,raum, name, steuerzentrale, data = None):
        super().__init__(raum, name, steuerzentrale, data = None)
        
    def setState(self, value):
        self.helligkeit = value
    
    def setHelligkeit(self, value):
        if value <= 100 and value >= 0:
            self.setState(value)
        else:
            print('Der Wert ist ungültig!')

    def helligkeitErhöhen(self):
        if self.helligkeit < 100:
            self.helligkeit = self.helligkeit + 10
        else:
            print('Lampe bereits maximal hell!')

    def helligkeitVerringern(self):
        if self.helligkeit > 0:
            self.helligkeit = self.helligkeit + 10
        else:
            print('Lampe bereits maximal dunkel!')
    
    def anschalten(self):
        super().anschalten()
        print("Licht ist an")

    def ausschalten(self):
        super().ausschalten()
        print("Licht ist aus")
