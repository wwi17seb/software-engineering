from .sensor import Sensor


class SmokeDetector(Sensor):

    def __init__(self, name, room):
        Sensor.__init__(self, name, room)

    def readValue(self):
        # value gets injected by command line
        if (self.value in (1, "1", True, "True", "true", "onfire", "on fire", "smoke")):
            self.value = True
        else:
            self.value = False

    def __str__(self):
        return str(self.name) + " (SmokeDetector, " + str(self.room) + \
            "): " + str(self.value)
