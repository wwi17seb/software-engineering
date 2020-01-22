
class RoomController:

    def __init__(self, room):
        self.room = room

    def roomConfiguration(self):
        print("Room configuration of", self.room.getName())
        print("Select on of this options: ")
        print("l - list all devices")
        print("c - change room settings")
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


    def addDevice(self):
        pass

    def changeRoomConfig(self):
        print("Enter a new name: ")
        name = input()
        self.room.setName(name)