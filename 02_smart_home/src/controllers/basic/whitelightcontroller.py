from actuators.whitelight import WhiteLight
from sensors.lightpushbutton import LightPushButton
from controllers.controller import Controller


class WhiteLightController(Controller):
    def __init__(self, lightPushButtons, lights):
        if (type(lightPushButtons) == list):
            self.lightPushButtons = lightPushButtons
        else:
            self.lightPushButtons = [lightPushButtons]

        # Observe push buttons
        for pushButton in self.lightPushButtons:
            pushButton.attach(self)

        if (type(lights) == list):
            self.lights = lights
        else:
            self.lights = [lights]

    def update(self, sensor, value):
        if (sensor in self.lightPushButtons and value):
            for light in self.lights:
                light.toggleLight()

    def main(self):
        pass
