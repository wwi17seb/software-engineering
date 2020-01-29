from device.smartDevice.smartDevice import SmartDevice
from device.sensor.temperatureSensor import TemperatureSensor
from device.sensor.sensor import Sensor

# uses principle principle SDP, OCP, SRP, CCP
class Oven(SmartDevice):


    def __init__(self, name, description, serialNumber, connections, maxTemp):
        super(Oven, self).__init__(name, description, serialNumber, connections)
        self.__maxTemp = maxTemp
        self.__temperature = 0
        self.__timer = 0
        self.__sensor = TemperatureSensor(name, description, None, None, 1, 0)
        self.__sensor.turnOff()
        self.sensor.register(self, self.update)


    def collectData(self):
        print("Smart oven " + self.__name + "collects data from sensors...")
        print(str(self.sensor.getValue()))

    def exectuteCommand(self, command):
        print("Smart oven " + self.__name + "executed command " + str(command) + ".")

    def turnOn(self):
        if self.__temperature == 0:
            print("Please set the temperature!")
            return
        elif self.__timer == 0:
            print("Please set a timer!")
            return

        self.__sensor.turnOn()
        print("Smart oven  " + self.__name + "turned on.")

    def turnOff(self):
        self.__temperature = 0
        self.__timer = 0
        self.__sensor.turnOff()
        print("Smart oven  " + self.__name + "turned off.")

    def update(self, sensor, value, status):
        if status == Sensor.ERROR or value != self.__temperature:
            print("Microwave", self.__name, "got temperature problems!")
            self.__temperature = value
        else:
            print("Microwave", self.__name, "temperature is", value)

    def setTemperature(self, temp):
        self.__temperature = temp
        self.sensor.setTrigger(temp)

    def setTimer(self, timer):
        self.__timer = timer
