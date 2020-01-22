from actuators.rgblight import RGBLight
from sensors.lightpushbutton import LightPushButton
from sensors.colorsetter import ColorSetter


class RGBLightController:
    def __init__(self, lightPushButtons, colorSetter, rgbLights):
        if (type(lightPushButtons) == list):
            self.lightPushButtons = lightPushButtons
        else:
            self.lightPushButtons = [lightPushButtons]

        # Observe push buttons
        for pushButton in self.lightPushButtons:
            pushButton.attach(self)

        self.colorSetter = colorSetter
        self.colorSetter.attach(self) # observe color setter

        if (type(rgbLights) == list):
            self.rgbLights = rgbLights
        else:
            self.rgbLights = [rgbLights]

    def update(self, sensor, value):
        if (sensor in self.lightPushButtons and value):
            for rgbLight in self.rgbLights:
                rgbLight.toggleLight()
        elif (sensor == self.colorSetter):
            red = int(value[1:3], 16)
            green = int(value[3:5], 16)
            blue = int(value[5:7], 16)
            for rgbLight in self.rgbLights:
                rgbLight.setColor(red, green, blue)

    def main(self):
        pass
