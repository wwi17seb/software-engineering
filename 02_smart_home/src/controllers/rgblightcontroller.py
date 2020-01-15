from actuators.rgblight import RGBLight
from sensors.lightswitch import Lightswitch


class RGBLightController:
    def __init__(self, switch, light):
        self.lightswitch = switch
        self.rgbLight = light

    def main(self):
        lightswitchValue = self.lightswitch.getValue()
        if (lightswitchValue == True):
            self.rgbLight.turnOn()
        elif (lightswitchValue == False):
            self.rgbLight.turnOff()
        
        # TODO: colors