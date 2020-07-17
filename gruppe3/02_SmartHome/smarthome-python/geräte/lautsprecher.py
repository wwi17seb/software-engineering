from geräte.gerät import Gerät

class Lautsprecher(Gerät):
    
    def __init__(self, raum, name, steuerzentrale, data = None):
        super().__init__(raum, name, steuerzentrale, data = None)
        self.zustand = 0
        
    def setState(self, value):
        self.zustand = value

    def lautstaerkeErhoehen(self):
        x = 5
        self.zustand = self.zustand + x
        print('Lautstärke bei {0}'.format(self.zustand))

    def lautstaerkeSenken(self):
        y = -5
        self.zustand = self.zustand + y
        print('Lautstärke bei {0}'.format(self.zustand))