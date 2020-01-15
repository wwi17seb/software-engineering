from geräte.gerät import Gerät

class Beleuchtung(Gerät):
    
    def aendern(self):
        pass

    def anschalten(self):
        self.zustand = "ON"
        print("Licht ist an")

    def ausschalten(self):
        self.zustand = "OFF"
        print("Licht ist aus")
