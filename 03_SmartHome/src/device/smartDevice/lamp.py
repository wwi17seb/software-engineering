from .smartDevice import SmartDevice
from device.sensor.temperatureSensor import TemperatureSensor
from device.sensor.sensor import Sensor


class Lamp(SmartDevice):

    def __init__(self, name, description, serialNumber, conntections, brightness):
        super().__init__(name, description, serialNumber, conntections)
        self.__brightness = brightness
        self.__maxTemp = 40
        self.__sensor = TemperatureSensor(name, description, None, None, 1, self.__maxTemp)
        self.__sensor.register(self, self.update())

    def collectData(self):
        print("Smart lamp " + self.name + " collects data from sensors...")
        print("Temperature:", self.__sensor.getValue())

    def exectuteCommand(self, command):
        self.__changeBrightness(command)
        print("Smart lamp " + self.name + " executed command " + str(command) + ".")

    def turnOn(self):
        print("Lamp " + self.name + " turned on.")

    def turnOff(self):
        print("Lamp " + self.name + " turned off.")

    def update(self, sensor, value, status):
        if status == Sensor.ERROR or value != self.maxTemp:
            print("Lamp", self.name, "got temperature problems -> reducing brightness!")
            self.brightness -= 1
        else:
            print("Lamp", self.name, "works fine.")

    def __changeBrightness(self, brightness):
        self.__brightness = brightness
