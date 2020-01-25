from building.room import Room
from building.roomgroup import RoomGroup
from controller.roomController import RoomController

class RoomGroupController:

    def __init__(self, roomGroups):
        self.roomGroups = roomGroups

    def roomGroupConfiguration(self):
        print("Here you can change your room and room group configurations.")
        print("%d room groups are registered." % len(self.roomGroups))
        if len(self.roomGroups) == 0:
            print("Do you want to create a new room group [y/n]? ")
            arg = input()
            if arg == "y":
                self.addRoomGroup()
                self.roomGroupConfiguration()
        else:
            for i in range(len(self.roomGroups)):
                print(i, "-", self.roomGroups[i].getName())
            print("Type s to select a room group, c to create a new room group or something else to return.")
            arg = input()
            if arg == "s":
                print("Select the group to change [number]: ")
                arg = input()
                if arg.isdigit():
                    arg = int(arg)
                    if 0 >= arg >= len(self.roomGroups):
                        self.roomGroupConfiguration()
                    else:
                        self.groupConfiguration(self.roomGroups[arg])
                        self.roomGroupConfiguration()

            elif arg == "c":
                self.addRoomGroup()
                self.roomGroupConfiguration()


    def addRoomGroup(self):
        print("Enter group name: ")
        arg = input()
        self.roomGroups.append(RoomGroup(arg))

    def addRoom(self, roomgroup):
        print("Room name: ")
        name = input()
        print("Height (Integer): ")
        height = int(input())
        print("Area in square meters (Integer): ")
        area = int(input())
        room = Room(height, name, area)
        roomgroup.addRoom(room)

    def groupConfiguration(self, roomgroup):
        print("You selected the %s group." % roomgroup.getName())
        print("Type r to list all connected rooms or type n to change group name or something else to return: ")
        arg = input()
        if arg == "r":
            if len(roomgroup.getRooms()) == 0:
                print("There is no room to change. Do you want to create a room [y/n]? ")
                arg = input()
                if arg == "y":
                    self.addRoom(roomgroup)
                    self.groupConfiguration(roomgroup)
            else:
                print("Following rooms belongs to this group: ")
                rooms = roomgroup.getRooms()
                for i in range(len(rooms)):
                    print(i, "-", rooms[i].getName())

                print("Type s to select room or something else to return: ")
                arg = input()
                if arg == "s":
                    print("Please select room: ")
                    arg = input()
                    if arg.isdigit():
                        arg = int(arg)
                        if arg >= len(rooms):
                            self.groupConfiguration(roomgroup)
                        else:
                            roomController = RoomController(rooms[arg])
                            roomController.roomConfiguration()
        elif arg == "n":
            print("New group name: ")
            arg = input()
            roomgroup.setName(arg)
            self.groupConfiguration(roomgroup)







