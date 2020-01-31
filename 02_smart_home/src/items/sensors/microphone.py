from .sensor import Sensor


class Microphone(Sensor):

    def __init__(self, name, room):
        Sensor.__init__(self, name, room)

    def readValue(self):
        pass

    def parseValue(self, value):
        return str(value)

    def __str__(self):
        return str(self.name) + " (Microphone, " + str(self.room) + ")"
