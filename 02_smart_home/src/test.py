import unittest
from main import SmartHome
from sensors import *
from actuators import *
from controllers import *

class SmartHomeTest(unittest.TestCase):

    def testRGBLights(self):
        sh = SmartHome()
        sh.addController(basic.rgblightcontroller.RGBLightController(
            sh.addItem(lightpushbutton.LightPushButton("testLightPushButton", None)),
            sh.addItem(colorsetter.ColorSetter("testColorSetter", None)),
            sh.addItem(rgblight.RGBLight("testRGBLight", None))
        ))
        sh.getItemByName("testColorSetter").setValue("red")
        sh.getItemByName("testLightPushButton").setValue(True)
        
        light = sh.getItemByName("testRGBLight")
        self.assertEqual(light.state, True)
        self.assertEqual(light.red, 255)
        self.assertEqual(light.green, 0)
        self.assertEqual(light.blue, 0)

if __name__ == "__main__":
    unittest.main()