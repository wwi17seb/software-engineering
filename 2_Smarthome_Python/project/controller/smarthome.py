from .icontroller import IController
from .heatingcontroller import HeatingController
from room import Room
from .lightingcontroller import LightingController
from .ventilationcontroller import VentilationController

class Smarthome(IController):

    def __init__(self,name,rooms=[]):
        IController.__init__(self,name)
        self.rooms=rooms
        self.heatingcontroller = HeatingController()
        self.lightingcontroller = LightingController()
        self.ventilationcontroller = VentilationController()

    def systemStart(self):
        print("Systemstart:")
        self.turnOn()
        self.heatingcontroller.turnOn()
        self.lightingcontroller.turnOn()
        self.ventilationcontroller.turnOn()
        print("Smarthome Status: ",self.state)

    def systemShutdown(self):
        print("Herunterfahren:")
        self.turnOff()
        self.heatingcontroller.turnOff()
        self.lightingcontroller.turnOff()
        self.ventilationcontroller.turnOff()
        print("Smarthome Status: ",self.state)

    def findRoomById(self, id):
        for room in self.rooms:
            if room.id == id:
                return 1
        return 0

    def findRoomByName(self, lvl, name):
        for room in self.rooms:
            if room.level == lvl and room.name == name:
                return 1
        return 0

    def getRoomByName(self, lvl, name):
        for room in self.rooms:
            if room.level == lvl and room.name == name:
                return room
        return None

    def addRoom(self,lvl,name):
        if self.findRoomByName(lvl,name) == 1:
            print("Raum schon vorhanden")
        else:
            self.rooms.append(Room(lvl,name))
            print("Neuen Raum hinzugefügt: ",self.rooms[-1].id)
