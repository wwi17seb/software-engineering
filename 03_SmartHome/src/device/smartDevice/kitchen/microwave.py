from device.smartDevice.smartDevice import SmartDevice
from device.sensor.temperatureSensor import TemperatureSensor
from device.sensor.sensor import Sensor

class Microwave(SmartDevice):

    DEFAULT_TEMP = 20

    def __init__(self, name, description, serialNumber, connections, maxPower):
        super(Microwave, self).__init__(name, description, serialNumber, connections)
        self.__maxPower = maxPower
        self.__temperature = self.DEFAULT_TEMP
        self.__currentPower = 0
        self.__sensor = TemperatureSensor(name, description, None, None, 1, 20)
        self.__sensor.turnOff()
        self.__sensor.register(self, self.update)


    def collectData(self):
        print("Smart microwave " + self.__name + "collects data from sensors...")
        print(str(self.sensor.getValue()))

    def exectuteCommand(self, command):
        print("Smart microwave " + self.__name + "executed command " + str(command) + ".")

    def turnOn(self):
        if self.__currentPower == 0:
            print("Please set the power!")
            return
        elif self.__temperature == self.DEFAULT_TEMP:
            print("Please set a max temperature for your food!")
            return

        self.__sensor.turnOn()
        print("Smart microwave  " + self.__name + "turned on.")

    def turnOff(self):
        self.__currentPower = 0
        self.__sensor.turnOff()
        print("Smart microwave  " + self.__name + "turned off.")

    def update(self, sensor, value, status):
        if status == Sensor.ERROR or value != self.__temperature:
            print("Microwave", self.__name, "got temperature problems!")
            self.__temperature = value
        else:
            print("Microwave", self.__name, "temperature is", value)

    def setTemperature(self, temp):
        self.__temperature = temp
        self.sensor.setTrigger(temp)

    def setPower(self, power):
        self.__currentPower = power
