from .sensor import Sensor


class SmokeDetector(Sensor):

    def __init__(self, name, room):
        Sensor.__init__(self, name, room)

    def readValue(self):
        pass

    def parseValue(self, value):
        if (value in (1, "1", True, "True", "true", "onfire", "on fire", "fire", "smoke")):
            return True
        else:
            return False

    def __str__(self):
        return str(self.name) + " (SmokeDetector, " + str(self.room) + \
            "): " + str(self._value)
