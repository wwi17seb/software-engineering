from device.smartDevice.smartDevice import SmartDevice
from device.sensor.temperatureSensor import TemperatureSensor
from device.sensor.sensor import Sensor
from routinesAndCommands.commands import turnOn, turnOff

# uses principle principle SDP, OCP, SRP, CCP
class Lamp(SmartDevice):

    def __init__(self, name, description, serialNumber, connections, brightness):
        super(Lamp, self).__init__(name, description, serialNumber, connections)
        self.__brightness = brightness
        self.__maxTemp = 40
        self.__sensor = TemperatureSensor(name, description, None, None, 1, self.__maxTemp)
        self.__sensor.register(self, self.update)
        self.__commands = {turnOn(self), turnOff(self)}
        self.__sensor.turnOff()

    def collectData(self):
        print("Smart lamp " + self.getName() + " collects data from sensors...")
        print("Temperature:", self.__sensor.getValue())

    def executeCommand(self, command):
        self.__changeBrightness(command)
        print("Smart lamp " + self.getName() + " executed command " + str(command) + ".")

    def turnOn(self):
        self.__sensor.turnOn()
        print("Lamp " + self.getName() + " turned on.")

    def turnOff(self):
        self.__sensor.turnOff()
        print("Lamp " + self.getName() + " turned off.")

    def update(self, sensor, value, status):
        if status == Sensor.ERROR or value != self.__maxTemp:
            print("Lamp", self.__name, "got temperature problems -> reducing brightness!")
            self.__brightness -= 1
        else:
            print("Lamp", self.getName(), "works fine.")

    def __changeBrightness(self, brightness):
        self.__brightness = brightness

