import unittest
from controller.basiccontroller.smarthome import Smarthome


class SmarthomeTest(unittest.TestCase):

    def testSmarthome(self):
        #set up smarthome
        smarthome = Smarthome("Smarthome",[])

        #test1: add a room
        smarthome.addRoom("Testzimmer")
        self.assertEqual(smarthome.findRoomByName("Testzimmer"),1)

        #test2: add same room again
        self.assertEqual(smarthome.addRoom("Testzimmer"),0)

        #testcase: start smarthome system
        #test3: smarthome running
        #test4: heatingcontroller running
        #test5: lightingcontroller running
        #test6: ventilationcontroller running
        smarthome.systemStart()
        self.assertEqual(smarthome.state,1)
        self.assertEqual(smarthome.heatingcontroller.state,1)
        self.assertEqual(smarthome.lightingcontroller.state,1)
        self.assertEqual(smarthome.ventilationcontroller.state,1)

        #testcase: shut down smarthome system
        #test3: smarthome not running
        #test4: heatingcontroller not running
        #test5: lightingcontroller not running
        #test6: ventilationcontroller not running
        smarthome.systemShutdown()
        self.assertEqual(smarthome.state,0)
        self.assertEqual(smarthome.heatingcontroller.state,0)
        self.assertEqual(smarthome.lightingcontroller.state,0)
        self.assertEqual(smarthome.ventilationcontroller.state,0)

    def testHeating(self):
        #set up smarthome and room with smart heater
        smarthome = Smarthome("Smarthome",[])
        smarthome.addRoom("Testzimmer")

        #test1: add heater for room
        smarthome.heatingcontroller.addHeater(smarthome.rooms[0])
        self.assertNotEqual(smarthome.heatingcontroller.heater, [])

        #test2: is the controller successfully turned on
        smarthome.heatingcontroller.turnOn()
        self.assertEqual(smarthome.heatingcontroller.state, 1)

        #testcase: heat room to target
        #test3: heater turned on
        #test4: temperature sensor target set to target temperature
        smarthome.heatingcontroller.heatRoom(smarthome.ventilationcontroller,smarthome.rooms[0],23)
        self.assertEqual(smarthome.heatingcontroller.heater[0].state, 1)
        self.assertEqual(smarthome.rooms[0].hsensor.target, 23)


        #test5: shutdown heating, when target reached
        smarthome.rooms[0].hsensor.setState(smarthome.rooms[0].hsensor.target)
        self.assertEqual(smarthome.heatingcontroller.heater[0].state, 0)

        #testcase: heat to temperature lower then actual temperature
        #test6: heater turned off
        #test7: temperature sensor target set to target temperature
        smarthome.heatingcontroller.heatRoom(smarthome.ventilationcontroller,smarthome.rooms[0],20)
        self.assertEqual(smarthome.heatingcontroller.heater[0].state, 0)
        self.assertEqual(smarthome.rooms[0].hsensor.target, 20)

    def testLighting(self):
        #set up smarthome and room with smart lamp and shutter
        smarthome = Smarthome("Smarthome", [])
        smarthome.addRoom("Testzimmer")

        #test0: add window and shutter
        smarthome.lightingcontroller.addLamp(smarthome.rooms[0])
        smarthome.lightingcontroller.addShutter(smarthome.rooms[0])
        self.assertNotEqual(smarthome.lightingcontroller.lamps, [])
        self.assertNotEqual(smarthome.lightingcontroller.shutters, [])

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

        #test0: add window
        smarthome.ventilationcontroller.addWindow(smarthome.rooms[0])
        self.assertNotEqual(smarthome.ventilationcontroller.windows, [])

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
