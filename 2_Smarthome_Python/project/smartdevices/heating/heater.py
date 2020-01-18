from ..smartdevice import SmartDevice

class Heater(SmartDevice):
    def __init__(self,room):
        SmartDevice.__init__(self,room)
        room.addHsensor()


    def heat(self,target):
        print("Der Raum: ",self.room.name," hat aktuell ",self.room.hsensor.getData(), " Grad Celsius")

        if target > self.room.hsensor.getData():
            self.state=1
            print("Ich beginne auf ", target, " zu heizen.")
        else:
            self.state=0
            print("Die Zieltemperatur liegt unter der Raumtemperatur.")

    def stopHeating(self):
        self.state=0
        print("Heizung ausgeschaltet")
