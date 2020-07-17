class Automation:
    def __init__(self, _input, _output, typ):
        #Konstruktor
        self.id = 1
        self.input = _input #ein Gegenstand
        self.output = _output #ein Gegenstand
        self.typ = typ
        self.gegenstand_liste = list([_output.name])
    
    def ausführen(self):
        print("Automation ausgelöst von {0}: ".format(self.input.name))
        self.output.anschalten()

    def bearbeiten(self,input = None, output = None):
        self.gegenstand_liste += [output.name]
        self.input = input
        print (self.gegenstand_liste)