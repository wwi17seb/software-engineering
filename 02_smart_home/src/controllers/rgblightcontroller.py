from actuators.rgblight import RGBLight
from sensors.lightswitch import Lightswitch


class RGBLightController:
    def __init__(self, switch, light):
        self.Lightswitch = switch
        self.RGBLight = light

    def main(self):
        print("RGBLightcontroller created.")
