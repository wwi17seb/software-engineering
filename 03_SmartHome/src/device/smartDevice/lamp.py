from .smartDevice import SmartDevice

class Lamp(SmartDevice):

    def __init__(self, name, description, serialNumber, macAddress, conntections, brightness):
        super().__init__(name, description, serialNumber, macAddress, conntections)
        self.brightness = brightness

    def collectData(self):
        print("Smart lamp " + self.name + " collects data from sensors...")

    def exectuteCommand(self, command):
        print("Smart lamp " + self.name + " executed command " + str(command) + ".")

    def turnOn(self):
        print("Lamp " + self.name + " turned on.")

    def turnOff(self):
        print("Lamp " + self.name + " turned off.")