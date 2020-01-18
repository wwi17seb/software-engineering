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

    def heatRoom(self,room,temperature):
        if self.status==1:
            for heater in self.heater:
                if heater.room == room:
                    heater.heat(temperature)
                else:
                    print("Keine Heizung in diesem Raum verfügbar")

    def stopHeatRoom(self,room):
        if self.status==1:
            for heater in self.heater:
                if heater.room == room:
                    heater.stopHeating()
                else:
                    print("Keine Heizung in diesem Raum verfügbar")
