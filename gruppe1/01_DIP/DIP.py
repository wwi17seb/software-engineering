

class SchalterClient:
    def anschalten(self):
        raise NotImplementedError
    def ausschalten(self):
        raise NotImplementedError


class Lampe(SchalterClient):
    leuchtet = False

    def anschalten(self):
        leuchtet = True
        print("Angeschaltet! Leuchtet = ", leuchtet)

    def ausschalten(self):
        leuchtet = False
        print("Ausgeschaltet! Leuchtet = ", leuchtet)


class Schalter:

    def __init__(self, SchalterClient):
        self.lampe = Lampe
        self.gedrueckt = False

    def drueckeSchalter(self):
        self.gedrueckt = not self.gedrueckt
        if(self.gedrueckt):
            self.lampe.anschalten()
        else:
            self.lampe.ausschalten()

#Objekte Erstellen
lampe1 = Lampe()
schalter1 = Schalter(lampe1)

#Schalter An/Aus
schalter1.drueckeSchalter()
schalter1.drueckeSchalter()
