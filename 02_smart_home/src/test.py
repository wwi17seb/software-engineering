import unittest
from main import SmartHome
from sensors import *
from actuators import *
from controllers import *

class SmartHomeTest(unittest.TestCase):

    def testRGBLights(self):
        self.sh = SmartHome()
        self.sh.addController(basic.rgblightcontroller.RGBLightController(
            self.sh.addItem(lightpushbutton.LightPushButton("testLightPushButton", None)),
            self.sh.addItem(colorsetter.ColorSetter("testColorSetter", None)),
            self.sh.addItem(rgblight.RGBLight("testRGBLight", None))
        ))
        self.sh.getItemByName("testColorSetter").setValue("red")
        self.sh.getItemByName("testLightPushButton").setValue(True)
        
        light = self.sh.getItemByName("testRGBLight")
        self.assertEqual(light.state, True)
        self.assertEqual(light.red, 255)
        self.assertEqual(light.green, 0)
        self.assertEqual(light.blue, 0)

if __name__ == "__main__":
    unittest.main()
