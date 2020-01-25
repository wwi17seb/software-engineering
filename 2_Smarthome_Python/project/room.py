import itertools
from sensors.temperaturesensor import TemperatureSensor
from sensors.lightsensor import LightSensor

class Room:
    newId = itertools.count()
    def __init__(self,name):
        self.id = next(self.newId)
        self.name=name
        self.hsensor=None
        self.lsensor=None
        self.smartdevices=[]

    def addHsensor(self):
        if self.hsensor == None:
            self.hsensor=TemperatureSensor()

    def addLsensor(self):
        if self.lsensor == None:
            self.lsensor=LightSensor()
