from .isensor import ISensor

class LightSensor(ISensor):

    def __init__(self):
        ISensor.__init__(self,"Lichtsensor")

    def getData(self):
        return 80
