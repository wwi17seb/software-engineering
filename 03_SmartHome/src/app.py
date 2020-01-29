import building.house as house
import controller.roomGroupController as roomGroupController

# uses principle principle SDP, OCP, SRP, CCP
class MainController():

    def __init__(self):
        self.smartHome = None
        self.roomGroupController = None

    def transmitCommand(self, command):
        pass

    def createRoutine(self):
        pass

    def startSmartHome(self):
        print("Welcome to your perfect SMART HOME System!")
        self.startPoint()

    def startPoint(self):
        print("What do you want to do next? Press h for help or e for exit.")
        arg = input()
        self.checkArgument(str(arg))
        self.startPoint()

    def checkArgument(self, arg):
        if arg == "h":
            print("Here is your help. These are the possible commands: ")
            print("s  - Smart Home basic configs.")
            print("rg - Roomgroup and room configs.")
            print("e  - Exit SMART HOME System.")
        elif arg == "s":
            self.smartHomeController()
        elif arg == "rg":
            if self.roomGroupController is None:
                self.smartHomeController()
            self.roomGroupController.roomGroupConfiguration()
        elif arg == "e":
            import sys
            sys.exit()

    def smartHomeController(self):
        if self.smartHome is None:
            print("There is no SMART HOME configured! Do you want to create a new one? [y/n]")
            arg = input()
            if arg == "y":
                print("Please enter your city: ")
                city = input()
                print("Please enter your address: ")
                address = input()
                self.smartHome = house.House(city, address)
                self.roomGroupController = roomGroupController.RoomGroupController(self.smartHome.getRoomGroups())
                print("Your SMART HOME is now ready for take off!")
                self.smartHomeController()
        else:
            print("Your SMART HOME has the following values: ")
            print("City - %s" % self.smartHome.getCity())
            print("Address - %s" % self.smartHome.getAddress())
            print("Do you want to change city [c] or the address [a]? Press something else to return.")
            arg = input()
            if arg == "c":
                print("Enter the new city: ")
                city = input()
                self.smartHome.setCity(city)
            elif arg == "a":
                print("Enter the new address: ")
                address = input()
                self.smartHome.setAddress(address)


if __name__ == "__main__":

    mainController = MainController()
    mainController.startSmartHome()
