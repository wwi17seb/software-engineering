import itertools
from sensors.temperaturesensor import TemperatureSensor
from sensors.lightsensor import LightSensor

class Room:
    newId = itertools.count()
    def __init__(self,level,name):
        self.id = next(self.newId)
        self.level=level
        self.name=name
        self.hsensor=None
        self.lsensor=None

    def addHsensor(self):
        if self.hsensor == None:
            self.hsensor=TemperatureSensor()

    def addLsensor(self):
        if self.lsensor == None:
            self.lsensor=LightSensor()
