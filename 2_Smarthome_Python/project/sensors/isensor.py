import itertools
from abc import ABC, abstractmethod

class ISensor(ABC):
    newId = itertools.count()
    def __init__(self,sensortype,unit):
        self.id = next(self.newId)
        self.sensortype=sensortype
        self.unit=unit
        self.target=0
        self.state=0

    def getData(self):
        return self.state
    
    def setState(self,state):
        self.state=state

    def setTarget(self,target):
        self.target=target
    
    @abstractmethod
    def measurement(self):
        pass