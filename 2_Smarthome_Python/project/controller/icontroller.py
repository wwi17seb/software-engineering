class IController:
    def __init__(self,name):
        self.status=0
        self.name=name

    def turnOn(self):
        if self.status==0:
            self.status=1
            print("Das System: ",self.name, "wurde gestartet")
        else:
            print("Das System: ",self.name, " läuft bereits")

    def turnOff(self):
        if self.status==1:
            self.status=0
            print("Das System: ",self.name, " wurde abgeschaltet")
        else:
            print("Das System: ",self.name, " ist bereits abgeschaltet")
