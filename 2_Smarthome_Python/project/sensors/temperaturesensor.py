from .isensor import ISensor

class TemperatureSensor(ISensor):

    def __init__(self):
        ISensor.__init__(self,"Temperatursensor","Celsius")

    def measurement(self):
        self.setState(22)
