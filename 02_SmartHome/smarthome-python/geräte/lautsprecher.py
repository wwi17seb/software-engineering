from geräte.gerät import Gerät

class Lautsprecher(Gerät):
    
    def aendern(self):
        pass

    def lautstaerkeErhoehen(self):
        x = 5
        self.zustand= self.data + x
        print(self.zustand)

    def laustaerkeSenken(self):
        y = -5
        self.zustand = self.data + y