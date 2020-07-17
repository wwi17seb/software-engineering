from device.smartDevice.smartDevice import SmartDevice
from device.sensor.temperatureSensor import TemperatureSensor
from device.sensor.sensor import Sensor

# uses principle principle SDP, OCP, SRP, CCP
class Lamp(SmartDevice):

    def __init__(self, name, description, serialNumber, connections, brightness):
        super(Lamp, self).__init__(name, description, serialNumber, connections)
        self.__brightness = brightness
        self.__maxTemp = 50
        self.__sensor = TemperatureSensor(name, description, None, None, 1, self.__maxTemp)
        self.__sensor.register(self, self.update)
        self.__sensor.turnOff()

    def collectData(self):
        """ test collectData execution
        >>> lamp = Lamp('test', 'test lamp', '123', [], 50)
        Temperature sensor test turned off.
        >>> lamp.collectData()
        Smart lamp test collects data from sensors...
        Temperature: 0
        """
        print("Smart lamp " + self.getName() + " collects data from sensors...")
        print("Temperature:", self.__sensor.getValue())

    def executeCommand(self, command):
        """ test executeCommand execution
        >>> lamp = Lamp('test', 'test lamp', '123', [], 50)
        Temperature sensor test turned off.
        >>> lamp.executeCommand("do something")
        Smart lamp test executed command do something.
        """
        self.__changeBrightness(command)
        print("Smart lamp " + self.getName() + " executed command " + str(command) + ".")

    def turnOn(self):
        """ test turnOn execution
        >>> lamp = Lamp('test', 'test lamp', '123', [], 5)
        Temperature sensor test turned off.
        >>> lamp.turnOn()
        Temperature sensor test turned on.
        Smart lamp test turned on.
        """
        self.__sensor.turnOn()
        print("Smart lamp " + self.getName() + " turned on.")

    def turnOff(self):
        """ test turnOff execution
        >>> lamp = Lamp('test', 'test fridge', '123', [], 5)
        Temperature sensor test turned off.
        >>> lamp.turnOff()
        Temperature sensor test turned off.
        Smart lamp test turned off.
        """
        self.__sensor.turnOff()
        print("Smart lamp " + self.getName() + " turned off.")

    def update(self, sensor, value, status):
        """ test update execution
        >>> lamp = Lamp('test', 'test lamp', '123', [], 30)
        Temperature sensor test turned off.
        >>> lamp.update(None, 30, 1)
        Lamp test works fine.
        >>> lamp.update(None, 51, 1)
        Lamp test got temperature problems -> reducing brightness!
        >>> lamp.update(None, 30, 2)
        Lamp test got temperature problems -> reducing brightness!
        """
        if status == Sensor.ERROR or value > self.__maxTemp:
            print("Lamp", self.getName(), "got temperature problems -> reducing brightness!")
            self.__brightness -= 1
        else:
            print("Lamp", self.getName(), "works fine.")

    def __changeBrightness(self, brightness):
        self.__brightness = brightness


if __name__ == "__main__":
    import doctest

    doctest.testmod()
