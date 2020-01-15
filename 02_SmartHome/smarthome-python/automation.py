class Automation:
    def __init__(self, _input, _output, typ):
        #Konstruktor
        self.id = 1
        self.input = _input #ein Gegenstand
        self.output = _output #ein Gegenstand
        self.typ = typ
        self.gegenstand_liste = list()
    
    def ausführen(self):
        print("Automation ausgelöst von {0}: ".format(self.input))
        self.output.anschalten()

    def bearbeiten(self,automation):
        input_string = input("Füge Gegenstände getrennt mit Kommazeichen hinzu : ")
        self.gegenstand_liste += input_string.split(",")
        print (self.gegenstand_liste)

        
