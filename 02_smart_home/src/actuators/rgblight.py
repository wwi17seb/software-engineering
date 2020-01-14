from actuators import Actuator


class RGBLight(Actuator):

    def __init__(self):
        Actuator.__init__(self)
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
