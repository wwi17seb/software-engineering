from building.room import Room
from building.roomgroup import RoomGroup
from controller.roomController import RoomController
from device.smartDevice.kitchen.fridge import Fridge
from device.smartDevice.lamp.lamp import Lamp
from connection.wlan import WLAN
from connection.bluetooth import Bluetooth
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
        print("  l - List and execute Routines")
        print("  b - Back to main menu")

        arg = input()
        self.checkArgument(str(arg))

    def checkArgument(self, arg):
        if arg == "c":
            self.createRoutine()
        elif arg == "l":
            self.executeRoutine()
        elif arg == "b":
            print()
        else: 
            print("There is no such option as: ", arg)
            self.routineConfiguration()

    def createRoutine(self):
        print("Enter the name of your new Routine: ")
        arg = input()
        newRoutine = Routine(arg);

        print("Now you need to add commands by selecting SmartDevices")
        self.selectRoom(newRoutine)
    
    def selectRoom(self, routine):
        print("In which room is your SmartDevice located? Select by Number!")
        for i in range(len(self.__RoomList)):
            print(i, "-", self.__RoomList[i].getName())
        arg = input()
        if arg.isdigit():
            arg = int(arg)
            if 0 >= arg >= len(self.__RoomList):
                print("There is no room with that Number!")
                self.selectRoom(routine)
            else:
                self.selectDevice(routine, self.__RoomList[arg])

    def selectDevice(self,routine, room):
        devices = room.getDevices(); 
        print("Which device should work in your routine?")
        for i in range(len(devices)):
            print(i, "-", devices[i].getName())
        arg = input()
        if arg.isdigit():
            arg = int(arg)
            if 0 >= arg >= len(devices):
                print("There is no Device with that Number!")
                self.selectRoom(room)
            else: 
               self.selectTask(routine, devices[arg])
        
    def selectTask(self, routine, device):
        commands = device.getCommands()
        print("Which command should the Device perform?")
        for i in range(len(commands)):
            print(i, "-", commands[i].getName())
        arg = input()
        if arg.isdigit():
            arg = int(arg)                
            if 0 >= arg >= len(commands):
                print("There is no command with that number!")
                self.selectTask(routine, device)
            else:      
                routine.addCommand(commands[arg])  
                print()          
                print("Command", commands[arg].getName(), "added to routine:", routine.getName(), "!")
                print()
                print("Do you want to add another command?")
                print("y - Yes")
                print("anything else - Safe routine")
                arg = input()
                if arg == "y":
                    self.selectRoom(routine)
                else:
                    self.__Routines.append(routine)
                    print("Successfully safed routine: ", routine.getName())

    def executeRoutine(self): 
        print("You configured the following Routines: ")
        for i in range(len(self.__Routines)):
            print(i, "-" , self.__Routines[i].getName())
        print()
        print("Select Routine by number to execute. (Anything else to return)")
        arg = input()
        if arg.isdigit():
            arg = int(arg)
            if 0 >= arg >= len(self.__Routines):
                print("There is no routine with that number")
                self.executeRoutine()
            else: 
                print("Starting routine:", self.__Routines[arg].getName())
                self.__Routines[arg].executeCommands()
            



