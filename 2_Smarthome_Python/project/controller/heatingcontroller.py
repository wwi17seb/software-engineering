from .icontroller import IController
from smartdevices.heating.heater import Heater

class HeatingController(IController):
    def __init__(self):
        IController.__init__(self,"HeizungsController")
        self.heater=[]

    def addHeater(self, room):
        heater = Heater(room)
        self.heater.append(heater)
        room.smartdevices.append(heater)
        print("Heizung hinzugefügt: " + str(heater.id))

    def heatRoom(self,ventilationcontroller,room,temperature):
        if self.state==1:
            if room.hsensor != None:
                print("Der Raum: ",room.name," hat aktuell ",room.hsensor.getData(), " Grad Celsius")
                if temperature > room.hsensor.getData():
                    available=0
                    for heater in self.heater:
                        if heater.room == room:
                            heater.heat(temperature)
                            available=1
                    if available==1:
                        ventilationcontroller.stopVentilateRoom(room)
                else:
                    print("Die Zieltemperatur liegt unter der Raumtemperatur.")
                    self.stopHeatRoom(room)
            else:
                print("Keine Heizung in " + room.name + " verfügbar.")

    def stopHeatRoom(self,room):
        if self.state==1:
            available=0
            for heater in self.heater:
                if heater.room == room:
                    heater.stopHeating()
                    available=1
            if available==0:
                print("Keine Heizung in " + room.name + " verfügbar.")
