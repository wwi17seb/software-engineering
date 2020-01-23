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
from sensors.lightpushbutton import LightPushButton
from sensors.microphone import Microphone
from sensors.motionsensor import MotionSensor
from sensors.smokedetector import SmokeDetector
from sensors.temperaturesensor import TemperatureSensor

from controllers.basic.heatingcontroller import HeatingController
from controllers.basic.rgblightcontroller import RGBLightController
from controllers.basic.whitelightcontroller import WhiteLightController
from controllers.kitchen.voiceassistant import VoiceAssistant
from controllers.security.firealertcontroller import FireAlertController

COMMAND_EXIT = "exit"
COMMAND_HELP = "help"
COMMANDS_CONTROLLER = ["c", "controller", "controllers"]
COMMANDS_SENSORS = ["s", "sensor", "sensors"]
COMMANDS_ACTUATORS = ["a", "actuator", "actuators"]


class SmartHome:
    def __init__(self):
        # create rooms
        self.livingRoom = Room("Living Room")
        self.kitchen = Room("Kitchen")
        self.bedroom = Room("Bedroom")

        # items are stored in a dictionary, names are NOT case-sensitive
        self.items = {}
        self.controllers = []

        # create sensors and actuators
        self.addItem(LightPushButton("lpbbed1", self.bedroom))
        self.addItem(ColorSetter("csbed1", self.bedroom))
        self.addItem(RGBLight("rgblbed1", self.bedroom))

        self.addItem(TemperatureSensor("tsliving1", self.livingRoom))
        self.addItem(Heating("hliving1", self.livingRoom))
        self.addItem(SmokeDetector("sdliving1", self.livingRoom))
        self.addItem(FireAlert("fahouse1", None))

        self.addItem(LightPushButton("lpbkitchen1", self.kitchen))
        self.addItem(WhiteLight("wlkitchen1", self.kitchen))
        self.addItem(Oven("okitchen1", self.kitchen))
        self.addItem(Microphone("wife", self.kitchen))

        # create controllers
        self.addController(RGBLightController(
            self.getItemByName("lpbbed1"),
            self.getItemByName("csbed1"),
            self.getItemByName("rgblbed1")
        ))

        self.addController(HeatingController(
            self.getItemByName("tsliving1"),
            self.getItemByName("hliving1")
        ))

        self.addController(FireAlertController(
            self.getItemByName("sdliving1"),
            self.getItemByName("tsliving1"),
            self.getItemByName("fahouse1")
        ))

        self.addController(WhiteLightController(
            self.getItemByName("lpbkitchen1"),
            self.getItemByName("wlkitchen1")
        ))

        self.addController(VoiceAssistant(
            self.getItemByName("wife"),
            self
        ))

    def addItem(self, item):
        if (item.name.lower() in self.items):
            return False
        self.items[item.name.lower()] = item
        # item gets returned so that you can use it like: Controller(self.addItem(Item(name))))
        return item

    def getItemByName(self, itemName):
        return self.items[itemName.lower()]

    def getAllItemNames(self):
        return self.items.keys()

    def addController(self, controller):
        self.controllers.append(controller)

    def runControllers(self, printNumberOfControllers=True):
        for controller in self.controllers:
            controller.main()
        
        if (printNumberOfControllers):
            print("Running of", len(self.controllers),
                      "controllers completed")

    def cli(self):
        def printHelp():
            print("Type '" + COMMAND_EXIT + "' to exit,")
            print("type '" + COMMAND_HELP + "' to print this help,")
            print("type one of " + str(COMMANDS_CONTROLLER) + " to run all controllers,")
            print("type one of " + str(COMMANDS_SENSORS) + " to list all sensors,")
            print("type one of " + str(COMMANDS_ACTUATORS) + " to list all actuators,")
            print("or set a value for a sensor by 'sensorName' 'value'")
            print("\nSensor names are NOT case-sensitive, controllers will run automatically when sensor values change")
        printHelp()
        while(1):
            userInput = input("\n> ")
            if (userInput == COMMAND_EXIT):
                return
            elif (userInput == COMMAND_HELP):
                printHelp()
            elif (userInput in COMMANDS_CONTROLLER):
                self.runControllers()
            elif (userInput in COMMANDS_SENSORS):
                self._printSensors()
            elif (userInput in COMMANDS_ACTUATORS):
                self._printActuators()
            else:
                try:
                    itemName = userInput.split(" ", 1)[0]
                    value = userInput[len(itemName)+1:] # everything after item name -> in worst case an empty string
                    item = self.getItemByName(itemName)
                    if (isinstance(item, Sensor)):
                        item.setValue(value)
                    else:
                        raise ValueError
                except:
                    print("Unexpected command")

    def _printSensors(self):
        self._printItemsWhichAreOfClass(Sensor)

    def _printActuators(self):
        self._printItemsWhichAreOfClass(Actuator)

    def _printItemsWhichAreOfClass(self, cls):
        for itemName in self.items.keys():
            if (isinstance(self.items[itemName], cls)):
                print(self.items[itemName])


if __name__ == "__main__":
    s = SmartHome()
    s.cli()
