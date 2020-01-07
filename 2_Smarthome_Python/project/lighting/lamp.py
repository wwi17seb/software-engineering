import itertools

class Lamp:
    newId = itertools.count()
    def __init__(self,room):
        self.LampId = next(self.newId)
        room.addLsensor()
        self.room=room
        self.state=0

    def light(self):
        print("Aktuelle Helligkeit in Raum: ",self.room.name, " beträgt: ", self.room.lsensor.getData())

        if self.state == 0:
            self.state=1
            print("Lampe wurde angeschaltet. Status: ", self.state)

        else:
            print("Lampe ist schon angeschaltet")

    def dim(self):
        print("Aktuelle Helligkeit in Raum: ",self.room.name, " beträgt: ", self.room.lsensor.getData())

        if self.state == 1:
            self.state=0
            print("Lampe wurde ausgeschaltet. Status: ", self.state)

        else:
            print("Lampe ist schon ausgeschaltet")
