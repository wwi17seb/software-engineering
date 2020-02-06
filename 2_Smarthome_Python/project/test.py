import unittest
from controller.basiccontroller.smarthome import Smarthome


class SmarthomeTest(unittest.TestCase):

    def testHeating(self):
        #set up smarthome and room with smart heater
        smarthome = Smarthome("Smarthome",[])
        smarthome.addRoom("Testzimmer")
        smarthome.heatingcontroller.addHeater(smarthome.rooms[0])

        #test1: is the controller successfully turned on
        smarthome.heatingcontroller.turnOn()
        self.assertEqual(smarthome.heatingcontroller.state, 1)

        #test2: is the temperature heated from room temperature to 21 degrees
        smarthome.heatingcontroller.heatRoom(smarthome.ventilationcontroller,smarthome.rooms[0],21)
        smarthome.rooms[0].hsensor.setState(smarthome.rooms[0].hsensor.target)
        self.assertEqual(smarthome.rooms[0].hsensor.getData(), 21)

        #test3: is the temperature heated from 21 to 23 degrees
        smarthome.heatingcontroller.heatRoom(smarthome.ventilationcontroller,smarthome.rooms[0],23)
        smarthome.rooms[0].hsensor.setState(smarthome.rooms[0].hsensor.target)
        self.assertEqual(smarthome.rooms[0].hsensor.getData(), 23)

        #test4: is the temperature still 23 degrees when trying to 'heat' to a lower temperature
        smarthome.heatingcontroller.heatRoom(smarthome.ventilationcontroller,smarthome.rooms[0],20)
        smarthome.rooms[0].hsensor.setState(smarthome.rooms[0].hsensor.target)
        self.assertEqual(smarthome.rooms[0].hsensor.getData(), 23)

    def testLighting(self):
        #set up smarthome and room with smart lamp and shutter
        smarthome = Smarthome("Smarthome", [])
        smarthome.addRoom("Testzimmer")
        smarthome.lightingcontroller.addLamp(smarthome.rooms[0])
        smarthome.lightingcontroller.addShutter(smarthome.rooms[0])

        #test1: is the controller successfully turned on
        smarthome.lightingcontroller.turnOn()
        self.assertEqual(smarthome.lightingcontroller.state, 1)

        #testcase: lighting the room
        #test2: is the lighting increased to 80 lumen
        #test3: is the lamp turned on
        #test4: is the shutter open
        smarthome.lightingcontroller.lightRoom(smarthome.rooms[0])
        smarthome.rooms[0].lsensor.setState(smarthome.rooms[0].lsensor.target)
        self.assertEqual(smarthome.rooms[0].lsensor.getData(), 80)
        self.assertEqual(smarthome.rooms[0].smartdevices[0].state, 1)
        self.assertEqual(smarthome.rooms[0].smartdevices[1].state, 1)

        #testcase: dimming the room
        #test5: is the lamp turned off 
        #test6: is the shutter closed 
        smarthome.lightingcontroller.dimRoom(smarthome.rooms[0])
        smarthome.rooms[0].lsensor.setState(smarthome.rooms[0].lsensor.target)
        self.assertEqual(smarthome.rooms[0].smartdevices[0].state, 0)
        self.assertEqual(smarthome.rooms[0].smartdevices[1].state, 0)


    def testVentilation(self):
        #set up smarthome and room with smart window
        smarthome = Smarthome("Smarthome", [])
        smarthome.addRoom("Testzimmer")
        smarthome.ventilationcontroller.addWindow(smarthome.rooms[0])

        #test1: is the ventilation controller turned on
        smarthome.ventilationcontroller.turnOn()
        self.assertEqual(smarthome.ventilationcontroller.state, 1)

        #test2: is the window opened when ventilating the room
        smarthome.ventilationcontroller.ventilateRoom(smarthome.heatingcontroller, smarthome.rooms[0])
        self.assertEqual(smarthome.rooms[0].smartdevices[0].state, 1)

        #test3: is the window closed when stopping to ventilate the room
        smarthome.ventilationcontroller.stopVentilateRoom(smarthome.rooms[0])
        self.assertEqual(smarthome.rooms[0].smartdevices[0].state, 0)
        


if __name__ == "__main__":
    unittest.main()