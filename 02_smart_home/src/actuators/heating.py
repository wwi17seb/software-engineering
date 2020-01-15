from .actuator import Actuator


class Heating(Actuator):

    def __init__(self, name, maxLevel=5):
        Actuator.__init__(self, name)
        self.level = 0
        self.maxLevel = maxLevel

    def increaseLevel(self):
        self.level = min(self.level+1, self.maxLevel)

    def decreaseLevel(self):
        self.level = max(self.level-1, 0)

    def turnOff(self):
        self.level = 0

    def setToMaxLevel(self):
        self.level = self.maxLevel

    def setLevel(self, level):
        self.level = max(0, min(level, self.maxLevel))

    def __str__(self):
        return str(self.name) + " (Heating): " + str(self.level) + "/" + str(self.maxLevel)
