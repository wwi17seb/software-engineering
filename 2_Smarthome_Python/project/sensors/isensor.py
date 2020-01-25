import itertools
from abc import ABC, abstractmethod

class ISensor(ABC):
    newId = itertools.count()
    def __init__(self,sensortype,unit,room):
        self.id = next(self.newId)
        self.sensortype=sensortype
        self.unit=unit
        self.room=room
        self.state=0

    def getData(self):
        return self.state
    
    def setState(self,state):
        self.state=state
    
    @abstractmethod
    def measurement(self):
        pass