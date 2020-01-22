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
                self.roomConfiguration()

        elif arg == "c":
            self.changeRoomConfig()
            self.roomConfiguration()

        elif arg == "a":
            self.addDevice()
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
            if arg == 1:
                self.addFridge()
            elif arg == 2:
                self.addLamp()

    def addFridge(self):
        # TODO
        pass

    def addConnectionDevice(self):
        # Just an idea... maybe not really useful
        pass

    def addSensor(self):
        pass

    def changeRoomConfig(self):
        print("Enter a new name: ")
        name = input()
        self.room.setName(name)
