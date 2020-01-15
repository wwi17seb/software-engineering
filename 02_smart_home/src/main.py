from room import Room

from actuators.actuator import Actuator
from actuators.firealert import FireAlert
from actuators.fridge import Fridge
from actuators.heating import Heating
from actuators.oven import Oven
from actuators.poweroutlet import PowerOutlet
from actuators.rgblight import RGBLight
from actuators.shutter import Shutter
from actuators.whitelight import WhiteLight

from sensors.sensor import Sensor
from sensors.colorsetter import ColorSetter
from sensors.lightswitch import Lightswitch
from sensors.microphone import Microphone
from sensors.motionsensor import MotionSensor
from sensors.smokedetector import SmokeDetector
from sensors.temperaturesensor import TemperatureSensor

from controllers.basic.heatingcontroller import HeatingController
from controllers.basic.rgblightcontroller import RGBLightController
from controllers.basic.whitelightcontroller import WhiteLightController
from controllers.kitchen.voiceassistant import VoiceAssistant
from controllers.security.fireAlertController import FireAlertController

COMMAND_EXIT = "exit"
COMMAND_CONTROLLER = ["c", "controller", "controllers"]
COMMAND_SENSORS = ["s", "sensor", "sensors"]
COMMAND_ACTUATORS = ["a", "actuator", "actuators"]


class SmartHome:
    def __init__(self):
        # create rooms
        self.livingRoom = Room("Living Room")
        self.kitchen = Room("Kitchen")
        self.bedroom = Room("Bedroom")
        self.bathroom = Room("Bathroom")

        # items are stored in a dictionary, names are NOT case-sensitive
        self.items = {}
        self.controllers = []

        # create sensors and actuators
        self.addItem(Lightswitch("lsbath1", self.bathroom))
        self.addItem(WhiteLight("wlbath1", self.bathroom))
        self.addItem(Lightswitch("lsbed1", self.bedroom))
        self.addItem(ColorSetter("csbed1", self.bedroom))
        self.addItem(RGBLight("rgblbed1", self.bedroom))

        self.addItem(TemperatureSensor("tsliving1", self.livingRoom))
        self.addItem(Heating("hliving1", self.livingRoom))
        self.addItem(SmokeDetector("sdliving1", self.livingRoom))
        self.addItem(FireAlert("fahouse1", None))

        self.addItem(Microphone("wife", self.kitchen))

        # create controllers
        self.controllers.append(WhiteLightController(
            self.getItemByName("lsbath1"),
            self.getItemByName("wlbath1")
        ))
        self.controllers.append(RGBLightController(
            self.getItemByName("lsbed1"),
            self.getItemByName("csbed1"),
            self.getItemByName("rgblbed1")
        ))

        self.controllers.append(HeatingController(
            self.getItemByName("tsliving1"),
            self.getItemByName("hliving1")
        ))

        self.controllers.append(FireAlertController(
            self.getItemByName("sdliving1"),
            self.getItemByName("tsliving1"),
            self.getItemByName("fahouse1")
        ))

        self.controllers.append(VoiceAssistant(
            self.getItemByName("wife"),
            self
        ))

    def addItem(self, item):
        self.items[item.name.lower()] = item
        # item gets returned so that you can use it like: Controller(self.addItem(Item(name))))
        return item

    def getItemByName(self, itemname):
        return self.items[itemname.lower()]

    def getAllItemNames(self):
        return self.items.keys()

    def runControllers(self):
        for controller in self.controllers:
            controller.main()

    def cli(self):
        print("Type \"" + COMMAND_EXIT + "\" to exit,")
        print("type \"" + str(COMMAND_CONTROLLER) + "\" to run all controllers,")
        print("type \"" + str(COMMAND_SENSORS) + "\" to list all sensors,")
        print("type \"" + str(COMMAND_ACTUATORS) + "\" to list all actuators")
        print("or set a value for a sensor by \"sensorname\" \"value\"")
        print("\nSensornames are NOT case-sensitive")
        while(1):
            userInput = input("\ncommand: ")
            if (userInput == COMMAND_EXIT):
                return
            elif (userInput in COMMAND_CONTROLLER):
                self.runControllers()
                print("Running of", len(self.controllers),
                      "controllers completed")
            elif (userInput in COMMAND_SENSORS):
                self._printSensors()
            elif (userInput in COMMAND_ACTUATORS):
                self._printActuators()
            else:
                try:
                    itemname = userInput.split(" ", 1)[0]
                    value = userInput[len(itemname)+1:]
                    # = userInput.split(" ", 1)[1]
                    item = self.getItemByName(itemname)
                    if (isinstance(item, Sensor)):
                        item.value = value
                    else:
                        raise ValueError
                except:
                    print("Setting value for sensor failed")

    def _printSensors(self):
        self._printItemsWhichAreOfClass(Sensor)

    def _printActuators(self):
        self._printItemsWhichAreOfClass(Actuator)

    def _printItemsWhichAreOfClass(self, cls):
        for itemname in self.items.keys():
            if (isinstance(self.items[itemname], cls)):
                print(self.items[itemname])


if __name__ == "__main__":
    s = SmartHome()
    s.cli()
