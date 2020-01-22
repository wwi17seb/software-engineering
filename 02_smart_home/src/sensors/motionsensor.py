from .sensor import Sensor


class MotionSensor(Sensor):

    def __init__(self, name, room):
        Sensor.__init__(self, name, room)

    def readValue(self):
        pass

    def parseValue(self, value):
        if (value in (1, "1", True, "True", "true", "moving", "move", "action")):
            return True
        else:
            return False

    def __str__(self):
        return str(self.name) + " (MotionSensor, " + str(self.room) + \
            "): " + str(self._value)
