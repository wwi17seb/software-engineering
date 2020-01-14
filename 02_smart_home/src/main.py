class SmartHome:
    def __init__(self):
        self.controllers = []

        self.lightswitchBathroom = Lightswitch()
        self.whiteLightBathroom = WhiteLight()
        self.lightswitchBedroom = Lightswitch()
        self.rgbLightBedroom = RGBLight()

        self.controllers.append(LightController(self.lightswitchBathroom, self.whiteLightBathroom))
        self.controllers.append(LightController(self.lightswitchBedroom, self.rgbLightBedroom))

    def main(self):
        for controller in self.controllers:
            controller.main()

if __name__ == "__main__":
    s = SmartHome()
    s.main()