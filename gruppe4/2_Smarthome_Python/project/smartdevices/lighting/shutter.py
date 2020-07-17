from ..smartdevice import SmartDevice

class Shutter(SmartDevice):
    def __init__(self,room):
        SmartDevice.__init__(self,room)
        room.addLsensor()

    def open(self):
        print("Aktuelle Helligkeit in Raum: ",self.room.name, " beträgt: ", self.room.lsensor.getData())

        if self.state == 1:
            print("Rollladen ist schon geöffnet")
        else:
            self.state=1
            print("Rollladen wurde geöffnet. Status: ", self.state)

    def close(self):
        print("Aktuelle Helligkeit in Raum: ",self.room.name, " beträgt: ", self.room.lsensor.getData())

        if self.state == 0:
            print("Rollladen ist schon geschlossen")
        else:
            self.state=0
            print("Rollladen wurde geschlosses. Status: ", self.state)
