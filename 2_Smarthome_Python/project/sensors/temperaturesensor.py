from .isensor import ISensor

class TemperatureSensor(ISensor):

    def __init__(self):
        ISensor.__init__(self,"Temperatursensor")

    def getData(self):
        return 22
