from .smartDevice import SmartDevice

class Fridge(SmartDevice):

    def __init__(self, name, description, serialNumber, conntections, temperature, sensor):
        super(Fridge, self).__init__(name, description, serialNumber, conntections)
        self.temperature = temperature
        self.sensor = sensor

    def collectData(self):
        print("Smart fridge " + self.name + "collects data from sensors...")

    def exectuteCommand(self, command):
        print("Smart fridge " + self.name + "executed command " + str(command) + ".")

    def turnOn(self):
        print("Smart fridge  " + self.name + "turned on.")

    def turnOff(self):
        print("Smart fridge  " + self.name + "turned off.")