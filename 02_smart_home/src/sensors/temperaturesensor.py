from .sensor import Sensor


class TemperatureSensor(Sensor):

    def __init__(self, name, unit="°C"):
        Sensor.__init__(self, name)
        self.unit = unit

    def readValue(self):
        # value gets injected by command line
        if (type(self.value) == int):
            pass
        elif (type(self.value) == str and self.value.split()[0].isdigit()):
            self.value = int(self.value.split()[0])
        else:
            self.value = None

    def __str__(self):
        return str(self.name) + " (TemperatureSensor): " + str(self.value) + " " + str(self.unit)
