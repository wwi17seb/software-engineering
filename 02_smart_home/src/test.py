import unittest
from main import SmartHome
from room import Room
from items.sensors import *
from items.actuators import *
from controllers import *

class SmartHomeTest(unittest.TestCase):

    def testRGBLights(self):
        # setup
        sh = SmartHome()
        sh.addController(basic.rgblightcontroller.RGBLightController(
            sh.addItem(lightpushbutton.LightPushButton("testLightPushButton", None)),
            sh.addItem(colorsetter.ColorSetter("testColorSetter", None)),
            sh.addItem(rgblight.RGBLight("testRGBLight", None))
        ))
        sh.getItemByName("testColorSetter").setValue("red")
        sh.getItemByName("testLightPushButton").setValue(True)

        # testing
        light = sh.getItemByName("testRGBLight")
        self.assertEqual(light.state, True)
        self.assertEqual(light.red, 255)
        self.assertEqual(light.green, 0)
        self.assertEqual(light.blue, 0)
        
        sh.getItemByName("testLightPushButton").setValue(True)
        self.assertEqual(light.state, False)

    def testHeating(self):
        # setup
        sh = SmartHome()
        t = sh.addItem(temperaturesensor.TemperatureSensor("testTemperatureSensor", None))
        maxLevel = 8
        h = sh.addItem(heating.Heating("testHeating", None, maxLevel))
        desiredTemperature = 25
        acceptableDiff = 2

        sh.addController(basic.heatingcontroller.HeatingController(
            t, h, desiredTemperature, acceptableDiff
        ))

        # test1: stay at maxLevel if temperature still too low
        h.setToMaxLevel()
        t.setValue(desiredTemperature - (acceptableDiff + 1))
        self.assertEqual(h.level, maxLevel)

        # test2: decrease by one level if too warm
        h.setToMaxLevel()
        t.setValue(desiredTemperature + (acceptableDiff + 1))
        self.assertEqual(h.level, maxLevel-1)

        # test3: stay at same level if temperature remains in acceptable range
        h.setLevel(maxLevel//2)
        t.setValue(desiredTemperature + acceptableDiff//2)
        self.assertEqual(h.level, maxLevel//2)

    def testFireAlert(self):
        # setup
        sh = SmartHome()
        s = sh.addItem(smokedetector.SmokeDetector("testSmokeDetector", None))
        t = sh.addItem(temperaturesensor.TemperatureSensor("testTemperatureSensor", None))
        f = sh.addItem(firealert.FireAlert("testFireAlert", None))

        sh.addController(security.firealertcontroller.FireAlertController(
            s, t, f
        ))

        # test1: don't go off when everything normal
        s.setValue(False)
        t.setValue(25)
        self.assertEqual(f.state, False)

        # test2: go off when really warm
        s.setValue(False)
        t.setValue(100)
        self.assertEqual(f.state, True)

        # test3: go off when smoke detected
        s.setValue(True)
        t.setValue(25)
        self.assertEqual(f.state, True)

        # test4: go off when smoke and really hot
        s.setValue(True)
        t.setValue(100)
        self.assertEqual(f.state, True)

        # test5: don't go off during hot summer
        s.setValue(False)
        t.setValue(40)
        self.assertEqual(f.state, False)

    def testVoiceAssistantKitchenLights(self):
        # setup
        sh = SmartHome()
        sh.kitchen = Room("kitchen")
        wlk1 = sh.addItem(whitelight.WhiteLight("testWhiteLightKitchen1", sh.kitchen))
        wlk2 = sh.addItem(whitelight.WhiteLight("testWhiteLightKitchen2", sh.kitchen))
        rgblk = sh.addItem(whitelight.WhiteLight("testRGBLightKitchen", sh.kitchen))
        rgbln = sh.addItem(whitelight.WhiteLight("testRGBLightNotKitchen", None))
        m = sh.addItem(microphone.Microphone("testMicrophone", None))
        cmd = "switch kitchen lights off"

        sh.addController(kitchen.voiceassistant.VoiceAssistant(
            m, sh
        ))

        wlk1.turnOn()
        wlk2.turnOff()
        rgblk.turnOn()
        rgbln.turnOn()
        m.setValue(cmd)
        self.assertEqual(wlk1.state, False)
        self.assertEqual(wlk2.state, False)
        self.assertEqual(rgblk.state, False)
        self.assertEqual(rgbln.state, True)

if __name__ == "__main__":
    unittest.main()
