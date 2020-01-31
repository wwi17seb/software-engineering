from .actuator import Actuator


class RGBLight(Actuator):

    def __init__(self, name, room):
        Actuator.__init__(self, name, room)
        self.state = False
        self.red = 0
        self.green = 0
        self.blue = 0

    def turnOn(self):
        self.state = True

    def turnOff(self):
        self.state = False

    def toggleLight(self):
        self.state = not self.state

    def setColor(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return str(self.name) + " (RGBLight, " + str(self.room) + \
            "): " + str(self.state) + " (" + str(self.red) + ", " + \
            str(self.green) + ", " + str(self.blue) + ")"
