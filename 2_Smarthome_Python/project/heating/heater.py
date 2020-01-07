import itertools

class Heater:
    newId = itertools.count()
    def __init__(self,room):
        self.HeaterId = next(self.newId)
        room.addHsensor()
        self.room=room


    def heat(self,target):
        print("Der Raum: ",self.room.name," hat aktuell ",self.room.hsensor.getData(), " Grad Celsius")

        if target > self.room.hsensor.getData():
            print("Ich beginne auf ", target, " zu heizen.")
        else:
            print("Die Zieltemperatur liegt unter der Raumtemperatur.")
