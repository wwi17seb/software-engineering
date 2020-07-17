from .actuator import Actuator


class Fridge(Actuator):

    def __init__(self, name, room, minLevel=-2, maxLevel=7, unit="°C"):
        Actuator.__init__(self, name, room)
        self.level = None
        self.minLevel = minLevel
        self.maxLevel = maxLevel
        self.unit = unit

    def increaseLevel(self):
        if (self.level is None):
            self.turnOn()

        self.level = min(self.level+1, self.maxLevel)

    def decreaseLevel(self):
        if (self.level is None):
            self.turnOn()

        self.level = max(self.level-1, self.minLevel)

    def turnOff(self):
        self.level = None

    def turnOn(self):
        self.level = self.maxLevel

    def setToMaxLevel(self):
        self.level = self.maxLevel

    def setToMinLevel(self):
        self.level = self.minLevel

    def setLevel(self, level):
        self.level = max(0, min(level, self.maxLevel))

    def __str__(self):
        return str(self.name) + " (Fridge, " + str(self.room) + \
            "): " + str(self.level) + "(Range: " + str(self.minLevel) + " " + \
            str(self.unit) + " to " + str(self.maxLevel) + \
            " " + str(self.unit) + ")"
