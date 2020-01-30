from building.room import Room
from building.roomgroup import RoomGroup
from controller.roomController import RoomController
from device.smartDevice.kitchen.fridge import Fridge
from device.smartDevice.lamp.lamp import Lamp
from connection.wlan import WLAN
from connection.bluetooth import BlueTooth
from controller.deviceController import DeviceController
from routinesAndCommands.routine import Routine

class RoutineController:

    def __init__(self, smartHome):
        self.__smartHome = smartHome
        self.__RoomList = []
        self.__DeviceList = []
        self.__Routines = []

    def routineConfiguration(self):
        roomGroups = self.__smartHome.getRoomGroups() 
        for group in roomGroups:
            rooms = group.getRooms()
            for room in rooms: 
                self.__RoomList.append(room)

        print("What do you want to do with Routines? You got the following Options:")
        print("  c - Create a new Routine")
        print("  l - List all Routines")
        print("  e - Execute an existing Routine")

        arg = input()
        self.checkArgument(str(arg))

    def checkArgument(self, arg):
        if arg == "c":
            self.createRoutine()
        elif arg == "l":
            self.listRoutines()
        elif arg == "e":
            self.executeRoutine()

    def createRoutine(self):
        print("Enter the name of your new Routine: ")
        arg = input()
        newRoutine = Routine(arg);
        print("Now you need to add commands by selecting SmartDevices")
        self.selectRoom(newRoutine)
    
    def selectRoom(routine):
        print("In which room is your SmartDevice located? Select by Number!")
        for i in range(len(self.__RoomList)):
            print(i, "-", self.__RoomList[i].getName())
            arg = input()
            if arg.isdigit():
                arg = int(arg)
                if 0 >= arg >= len(self.__RoomList):
                    self.addCommand()
                else:
                    self.selectDevice(self.__RoomList[arg])

    def selectDevice(room):
        print("Which device should work in your routine?")
            


    def listRoutines(self): 
        print("Listing Routines...")
    
    def executeRoutine(self): 
        print("Executing: ")


