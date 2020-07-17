import itertools
from sensors.basicsensor.temperaturesensor import TemperatureSensor
from sensors.basicsensor.lightsensor import LightSensor

class Room:
    newId = itertools.count()

    # durch smarthome als input für Konstruktor wird möglicherweise gegen DIP verstoßen, 
    # hier im Kontext jedoch zu missachten, da raum nicht unabhängig vom Smarthome existieren sollte
    def __init__(self,name,smarthome):
        self.id = next(self.newId)
        self.name=name
        self.hsensor=None
        self.lsensor=None
        self.smarthome=smarthome
        self.smartdevices=[]

    def addHsensor(self):
        if self.hsensor == None:
            self.hsensor=TemperatureSensor(self)

    def addLsensor(self):
        if self.lsensor == None:
            self.lsensor=LightSensor(self)
