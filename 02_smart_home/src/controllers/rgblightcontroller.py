from actuators.rgblight import RGBLight
from sensors.lightswitch import Lightswitch
from sensors.colorsetter import ColorSetter


class RGBLightController:
    def __init__(self, switch, colorSetter, light):
        self.lightswitch = switch
        self.colorSetter = colorSetter
        self.rgbLight = light

    def main(self):
        lightswitchValue = self.lightswitch.getValue()
        if (lightswitchValue == True):
            self.rgbLight.turnOn()
        elif (lightswitchValue == False):
            self.rgbLight.turnOff()
        
        colorValue = self.colorSetter.getValue()
        # TODO: colors