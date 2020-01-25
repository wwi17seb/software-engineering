import itertools

class ISensor:
    newId = itertools.count()
    def __init__(self,sensortype,unit):
        self.id = next(self.newId)
        self.sensortype=sensortype
        self.unit=unit
        self.state=0

    def getData(self):
        return self.state
    
    def setState(self,state):
        self.state=state
    
    def measurement(self):
        pass