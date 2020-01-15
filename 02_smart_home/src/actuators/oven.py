from .actuator import Actuator


class Oven(Actuator):

    def __init__(self, name, room, maxTemp=240, unit="°C"):
        Actuator.__init__(self, name, room)
        self.temp = 0
        self.maxTemp = maxTemp

    def turnOff(self):
        self.temp = 0

    def setTemp(self, temp):
        self.temp = max(0, min(temp, self.maxTemp))

    def __str__(self):
        return str(self.name) + " (Oven, " + str(self.room) + \
            "): " + str(self.temp) + \
            "/" + str(self.maxTemp) + " " + self.unit
