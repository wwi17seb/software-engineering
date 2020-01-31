from .sensor import Sensor


class TemperatureSensor(Sensor):

    def __init__(self, name, room, unit="°C"):
        Sensor.__init__(self, name, room)
        self.unit = unit

    def readValue(self):
        pass

    def parseValue(self, value):
        if (type(value) == int):
            return value
        elif (type(value) == str and
            (value.split()[0].isdigit() or
            (value[0] == "-" and value.split()[0][1:].isdigit()))):
            return int(value.split()[0])
        else:
            return None

    def __str__(self):
        return str(self.name) + " (TemperatureSensor, " + str(self.room) + \
            "): " + str(self._value) + " " + str(self.unit)
