from .sensor import Sensor


class Lightswitch(Sensor):

    def __init__(self, name, room):
        Sensor.__init__(self, name, room)

    def readValue(self):
        # value gets injected by command line
        if (self.value in (1, "1", True, "True", "true", "on")):
            self.value = True
        else:
            self.value = False

    def __str__(self):
        return str(self.name) + " (LightSwitch, " + str(self.room) + \
            "): " + str(self.value)
