from actuators.whitelight import WhiteLight
from actuators.rgblight import RGBLight
from sensors.lightswitch import Lightswitch
from controllers.rgblightcontroller import RGBLightController
from controllers.whitelightcontroller import WhiteLightController


class SmartHome:
    def __init__(self):
        self.controllers = []

        self.lightswitchBathroom = Lightswitch()
        self.whiteLightBathroom = WhiteLight()
        self.lightswitchBedroom = Lightswitch()
        self.rgbLightBedroom = RGBLight()

        self.controllers.append(WhiteLightController(
            self.lightswitchBathroom, self.whiteLightBathroom))
        self.controllers.append(RGBLightController(
            self.lightswitchBedroom, self.rgbLightBedroom))

    def main(self):
        for controller in self.controllers:
            controller.main()


if __name__ == "__main__":
    s = SmartHome()
    s.main()
