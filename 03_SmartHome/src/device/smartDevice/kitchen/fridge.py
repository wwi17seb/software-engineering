from device.smartDevice.smartDevice import SmartDevice
from device.sensor.temperatureSensor import TemperatureSensor
from device.sensor.sensor import Sensor

class Fridge(SmartDevice):

    def __init__(self, name, description, serialNumber, connections, temperature):
        super(Fridge, self).__init__(name, description, serialNumber, connections)
        self.__defaultTemperature = temperature
        self.__sensor = TemperatureSensor(name, description, None, None, 1, temperature)
        self.__sensor.register(self, self.update)
        self.__sensor.turnOff()
        self.currentTemp = temperature

    def collectData(self):
        print("Smart fridge " + self.__name + "collects data from sensors...")
        print(str(self.sensor.getValue()))

    def exectuteCommand(self, command):
        self.__setTemperature(command)
        print("Smart fridge " + self.__name + "executed command " + str(command) + ".")

    def turnOn(self):
        self.__sensor.turnOn()
        print("Smart fridge  " + self.__name + "turned on.")

    def turnOff(self):
        self.__sensor.turnOff()
        print("Smart fridge  " + self.__name + "turned off.")

    def update(self, sensor, value, status):
        if status == Sensor.ERROR or value != self.__defaultTemperature:
            print("Fridge", self.__name, "got temperature problems!")
            self.currentTemp = value
        else:
            print("Fridge", self.__name, "temperature is", value)

    def __setTemperature(self, temp):
        self.__defaultTemperature = temp
        self.__sensor.setTrigger(temp)
