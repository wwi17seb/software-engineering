from gegenstand import Gegenstand

class gegenstandTest(Gegenstand):
    def __init__(self, raum, name, steuerzentrale, data = None):
        super().__init__(raum, name, steuerzentrale, data)
    
    def anschalten(self):
        super().anschalten()

    def ausschalten(self):
        super().ausschalten()

    def verbinden(self):
        super().verbinden()