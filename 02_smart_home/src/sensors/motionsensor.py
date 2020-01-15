from .sensor import Sensor


class MotionSensor(Sensor):

    def __init__(self, name):
        Sensor.__init__(self, name)

    def readValue(self):
        # value gets injected by command line
        if (self.value in (1, "1", True, "True", "true", "moving", "move", "action")):
            self.value = True
        else:
            self.value = False

    def __str__(self):
        return str(self.name) + " (MotionSensor): " + str(self.value)
