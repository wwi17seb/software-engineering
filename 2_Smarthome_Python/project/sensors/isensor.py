import itertools

class ISensor:
    newId = itertools.count()
    def __init__(self,sensortype):
        self.id = next(self.newId)
        self.sensortype=sensortype

    def getData(self):
        pass
