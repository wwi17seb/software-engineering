from device.smartDevice.fridge import Fridge
from device.smartDevice.lamp import Lamp
from connection.wlan import WLAN
from connection.bluetooth import BlueTooth
from controller.deviceController import DeviceController

class RoomController:

    def __init__(self, room):
        self.room = room

    def roomConfiguration(self):
        print("Room configuration of", self.room.getName())
        print("Select on of this options: ")
        print("l - list all devices")
        print("c - change room settings")
        print("a - add new device")
        print("else for return...")
        print("Selection: ")
        arg = input()
        if arg == "l":
            if len(self.room.getDevices()) == 0:
                print("There are no devices.")
                print("Do you want to create add a new device[y/n]?")
                arg = input()
                if arg == "y":
                    self.addDevice()
            else:
                for i in range(len(self.room.getDevices())):
                    print(i, "-", self.room.getDevices()[i].getName())

                print("Do you want do change device settings [y/n]? ")
                arg = input()
                if arg == "y":
                    print("Selection (Number): ")
                    arg = input()
                    if arg.isdigit():
                        arg = int(arg)
                        if 0 >= arg <= len(self.roomGroups):
                            deviceController = DeviceController(self.room.getDevices()[i])
                            deviceController.deviceConfiguration()


        elif arg == "c":
            self.changeRoomConfig()

        elif arg == "a":
            self.addDevice()

        else:
            return

        self.roomConfiguration()

    def addDevice(self):
        print("Select a kind of device to add:")
        print("1 - Smart Device")
        print("2 - Sensor")
        print("3 - Connection Device")
        print("Selection: ")
        arg = input()
        if arg.isdigit():
            arg = int(arg)
            if arg == 1:
                self.addSmartDevice()
            elif arg == 2:
                self.addSensor()
            elif arg == 3:
                self.addConnectionDevice()

    def addSmartDevice(self):
        print("Select a smart device:")
        print("1 - Fridge")
        print("2 - Lamp")
        print("Selection: ")
        arg = input()
        if arg.isdigit():
            arg = int(arg)

            print("Device name: ")
            name = input()
            print("Description: ")
            description = input()
            print("Serial Number: ")
            serial = input()
            print("Type of connection (WLAN/Bluetooth) [w/b]: ")
            connection = input()
            connections = []
            if connection == "w":
                con = WLAN()
            elif connection == "b":
                con = BlueTooth()
            connections.append(con)

            if arg == 1:
                self.addFridge(name, description, serial, connections)
            elif arg == 2:
                self.addLamp(name, description, serial, connections)

    def addFridge(self, name, description, serial, connections):
        print("Temperature: ")
        temp = input()
        fridge = Fridge(name, description, serial, connections, temp)
        self.room.addDevice(fridge)

    def addLamp(self, name, description, serial, connections):
        print("Brightness(0-100): ")
        brightness = input()
        lamp = Lamp(name, description, serial, connections, brightness)
        self.room.addDevice(lamp)

    def addConnectionDevice(self):
        print("Currently not supported.... :-(")

    def addSensor(self):
        pass

    def changeRoomConfig(self):
        print("Enter a new name: ")
        name = input()
        self.room.setName(name)
