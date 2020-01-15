from .actuator import Actuator


class Shutter(Actuator):

    def __init__(self, name, room, maxDimoutLevel=100):
        Actuator.__init__(self, name, room)
        self.dimoutevel = 0
        self.maxDimoutLevel = maxDimoutLevel

    def increaseLevel(self):
        self.dimoutLevel = min(self.dimoutLevel+1, self.maxDimoutLevel)

    def decreaseLevel(self):
        self.dimoutLevel = max(self.dimoutLevel-1, 0)

    def open(self):
        self.dimoutLevel = 0

    def close(self):
        self.dimoutLevel = self.maxDimoutLevel

    def setLevel(self, level):
        self.dimoutLevel = max(0, min(level, self.maxDimoutLevel))

    def __str__(self):
        return str(self.name) + " (Shutter, " + str(self.room) + \
            "): " + str(round(100*self.dimoutLevel /
                              self.maxDimoutLevel)) + "% dimout"
