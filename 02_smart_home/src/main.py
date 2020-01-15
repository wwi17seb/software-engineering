from actuators.actuator import Actuator
from actuators.whitelight import WhiteLight
from actuators.rgblight import RGBLight
from sensors.sensor import Sensor
from sensors.lightswitch import Lightswitch
from controllers.rgblightcontroller import RGBLightController
from controllers.whitelightcontroller import WhiteLightController


COMMAND_EXIT       = "exit"
COMMAND_CONTROLLER = "controller"
COMMAND_SENSORS    = "sensors"
COMMAND_ACTUATORS  = "actuators"


class SmartHome:
    def __init__(self):
        # items are stored in a dictionary, names are NOT case-sensitive
        self.items = {}
        self.controllers = []

        self.addItem(Lightswitch("lightswitchBathroom"))
        self.addItem(WhiteLight("whiteLightBathroom"))
        self.addItem(Lightswitch("lightswitchBedroom"))
        self.addItem(RGBLight("rgbLightBedroom"))

        self.controllers.append(WhiteLightController(
            self.getItemByName("lightswitchBathroom"), self.getItemByName("whiteLightBathroom")))
        self.controllers.append(RGBLightController(
            self.getItemByName("lightswitchBedroom"), self.getItemByName("rgbLightBedroom")))

    def addItem(self, item):
        self.items[item.name.lower()] = item
        return item # item gets returned so that you can use it like: Controller(self.addItem(Item(name))))

    def getItemByName(self, itemname):
        return self.items[itemname.lower()]

    def runControllers(self):
        for controller in self.controllers:
                controller.main()

    def cli(self):
        print("Type \"" + COMMAND_EXIT + "\" to exit,")
        print("type \"" + COMMAND_CONTROLLER + "\" to run all controllers,")
        print("type \"" + COMMAND_SENSORS + "\" to list all sensors,")
        print("type \"" + COMMAND_ACTUATORS + "\" to list all actuators")
        print("or set a value for a sensor by \"sensorname\" \"value\"")
        print("\nSensornames are NOT case-sensitive")
        while(1):
            userInput = input("\ncommand: ")
            if (userInput == COMMAND_EXIT):
                return
            elif (userInput == COMMAND_CONTROLLER):
                self.runControllers()
                print("Running of", len(self.controllers), "controllers completed")
            elif (userInput == COMMAND_SENSORS):
                self._printSensors()
            elif (userInput == COMMAND_ACTUATORS):
                self._printActuators()
            else:
                try:
                    itemname = userInput.split(" ",1)[0]
                    value = userInput.split(" ",1)[1]
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
