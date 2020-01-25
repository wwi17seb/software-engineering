from abc import ABC

class IController(ABC):
    def __init__(self,name):
        self.state=0
        self.name=name

    def turnOn(self):
        if self.state==0:
            self.state=1
            print("Das System: ",self.name, "wurde gestartet")
        else:
            print("Das System: ",self.name, " läuft bereits")

    def turnOff(self):
        if self.state==1:
            self.state=0
            print("Das System: ",self.name, " wurde abgeschaltet")
        else:
            print("Das System: ",self.name, " ist bereits abgeschaltet")
