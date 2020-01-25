from .smartDevice import SmartDevice
from device.sensor.temperatureSensor import TemperatureSensor
from device.sensor.sensor import Sensor


class Fridge(SmartDevice):

    def __init__(self, name, description, serialNumber, connections, temperature):
        super(Fridge, self).__init__(name, description, serialNumber, connections)
        self.defaultTemperature = temperature
        self.sensor = TemperatureSensor(name, description, None, None, 1, temperature)
        self.sensor.register(self, self.update())
        self.currentTemp = temperature

    def collectData(self):
        print("Smart fridge " + self.name + "collects data from sensors...")
        print(str(self.sensor.getValue()))

    def exectuteCommand(self, command):
        self.__setTemperature(command)
        print("Smart fridge " + self.name + "executed command " + str(command) + ".")

    def turnOn(self):
        print("Smart fridge  " + self.name + "turned on.")

    def turnOff(self):
        print("Smart fridge  " + self.name + "turned off.")

    def update(self, sensor, value, status):
        if status == Sensor.ERROR or value != self.defaultTemperature:
            print("Fridge", self.name, "got temperature problems!")
            self.currentTemp = value
        else:
            print("Fridge", self.name, "temperature is", value)

    def __setTemperature(self, temp):
        self.defaultTemperature = temp
        self.sensor.setTrigger(temp)
