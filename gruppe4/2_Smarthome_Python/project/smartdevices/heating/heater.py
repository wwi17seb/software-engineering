from ..smartdevice import SmartDevice

class Heater(SmartDevice):
    def __init__(self,room):
        SmartDevice.__init__(self,room)
        room.addHsensor()


    def heat(self,target):
        self.state=1
        print("Ich beginne auf ", target, " zu heizen.")

    def stopHeating(self):
        if self.state==1:
            self.state=0
            print("Heizung ausgeschaltet")
