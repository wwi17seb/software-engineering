from .sensor import Sensor


class LightPushButton(Sensor):

    def __init__(self, name, room):
        Sensor.__init__(self, name, room)

    def readValue(self):
        pass

    def parseValue(self, value):
        if (value in (1, "1", True, "True", "true", "on", "press")):
            return True
        else:
            return False

    def setValue(self, value):
        super().setValue(value)
        super().setValue(None) # reset since it is a push-button

    def __str__(self):
        return str(self.name) + " (LightPushButton, " + str(self.room) + ")"
