from geräte import gerät

class Heizung(gerät.Gerät):
    
    def aendern(self, value):
        if zustand == None:
            zustand = 0
        self.zustand += value
    
    def heizungAufdrehen(self):
        self.aendern(5)
        print ("Hmmm...Heizung wurde auf {0} gedreht".format(self.zustand) )

    def heizungZudrehen(self):
        self.aendern(-5)
        print ("Brrr...Heizung wurde auf {0} gedreht".format(self.zustand) )