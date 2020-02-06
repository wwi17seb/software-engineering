class Steuerzentrale:
    def __init__(self, name = "Hauszentrale", data = None):
        #Konstruktor
        self.data = data
        self.name = name
        self.gegenstaende = list()
        
    def steuernRaum(self, raum, aktion):
        pass

    def steuernGerät(self, gerät, aktion):
        pass

    def gegenstandHinzu(self, gegenstand):
        self.gegenstaende.append(gegenstand)

    def gegenstandEntfernen(self, gegenstand):
        self.gegenstaende.remove(gegenstand)
