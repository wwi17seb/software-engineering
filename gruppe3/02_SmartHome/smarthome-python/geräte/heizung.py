from geräte.gerät import Gerät

class Heizung(Gerät):
    def __init__(self, raum, name, steuerzentrale, data = None):
        super().__init__(raum, name, steuerzentrale, data = None)
        self.zustand = 0
    
    def setState(self, value):
#        if zustand == None:
#            zustand = 0
        self.zustand += value
        
    def heizungAufdrehen(self):
        self.setState(5)
        print ("Hmmm...Heizung wurde auf {0} gedreht".format(self.zustand) )

    def heizungZudrehen(self):
        self.setState(-5)
        print ("Brrr...Heizung wurde auf {0} gedreht".format(self.zustand) )