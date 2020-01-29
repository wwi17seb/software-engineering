
from device.smartDevice.smartDevice import SmartDevice
from device.sensor.temperatureSensor import LightSensor
from device.sensor.sensor import Sensor


class SmartTV(SmartDevice):

    def __init__(self, name, description, serialNumber, conntections):
        super(SmartTV, self).__init__(name, description, serialNumber, conntections)
        self.__sensor = LightSensor(name, description, None, None, 1, None)
        self.__sensor.register(self, self.update())
        self.__sensor.turnOff()
        self.__brightness = 30

    def collectData(self):
        print("SmartTV " + self.__name + " collects data from sensors...")
        print("Environmental brightness:", self.__sensor.getValue())

    def exectuteCommand(self, command):
        self.__changeBrightness(command)
        print("Smart TV " + self.__name + " executed command " + str(command) + ".")

    def turnOn(self):
        self.__sensor.turnOn()
        print("Smart TV " + self.__name + " turned on.")

    def turnOff(self):
        self.__sensor.turnOff()
        print("Smart TV " + self.__name + " turned off.")

    def update(self, sensor, value, status):
        if status == Sensor.ERROR or value != self.maxTemp:
            print("Smart TV", self.__name, "got environmental brightness problems -> increasing brightness!")
            self.__brightness += 1
        else:
            print("Smart TV", self.__name, "works fine.")

    def __changeBrightness(self, brightness):
        self.__brightness = brightness
