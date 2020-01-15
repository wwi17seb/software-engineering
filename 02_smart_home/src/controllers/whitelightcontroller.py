from actuators.whitelight import WhiteLight
from sensors.lightswitch import Lightswitch


class WhiteLightController:
    def __init__(self, switch, light):
        self.Lightswitch = switch
        self.WhiteLight = light

    def main(self):
        print("WhiteLightcontroller created.")
