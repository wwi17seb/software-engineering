from actuators.whitelight import WhiteLight
from sensors.lightswitch import Lightswitch


class WhiteLightController:
    def __init__(self, switch, light):
        self.lightswitch = switch
        self.whiteLight = light

    def main(self):
        lightswitchValue = self.lightswitch.getValue()
        if (lightswitchValue == True):
            self.whiteLight.turnOn()
        elif (lightswitchValue == False):
            self.whiteLight.turnOff()
