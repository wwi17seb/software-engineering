from .icontroller import IController
from .heatingcontroller import HeatingController
from room import Room
from .lightingcontroller import LightingController

class Smarthome(IController):

    def __init__(self,name,rooms=[]):
        IController.__init__(self,name)
        self.rooms=rooms
        self.heatingcontroller = HeatingController()
        self.lightingcontroller = LightingController()

    def systemStart(self):
        print("Systemstart:")
        self.turnOn()
        self.heatingcontroller.turnOn()
        self.lightingcontroller.turnOn()

    def systemShutdown(self):
        print("Herunterfahren:")
        self.turnOff()
        self.heatingcontroller.turnOff()
        self.lightingcontroller.turnOff()

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

    def addRoom(self,lvl,name):
        if self.findRoomByName(lvl,name) == 1:
            print("Raum schon vorhanden")
        else:
            self.rooms.append(Room(lvl,name))
            print("Neuen Raum hinzugefügt: ",self.rooms[-1])
