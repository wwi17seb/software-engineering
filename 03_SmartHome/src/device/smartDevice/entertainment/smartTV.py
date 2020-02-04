from device.smartDevice.smartDevice import SmartDevice
from device.sensor.lightSensor import LightSensor
from device.sensor.sensor import Sensor


class SmartTV(SmartDevice):

    def __init__(self, name, description, serialNumber, connections):
        super(SmartTV, self).__init__(name, description, serialNumber, connections)
        self.__sensor = LightSensor(name, description, None, None, 1, None)
        self.__sensor.register(self, self.update)
        self.__sensor.turnOff()
        self.__brightness = 30

    def collectData(self):
        """ test collectData execution
        >>> tv = SmartTV('test', 'test tv', '123', [])
        Light sensor test turned off.
        >>> tv.collectData()
        SmartTV test collects data from sensors...
        Environmental brightness: 0
        """
        print("SmartTV " + self.getName() + " collects data from sensors...")
        print("Environmental brightness:", self.__sensor.getValue())

    def executeCommand(self, command):
        """ test executeCommand execution
        >>> tv = SmartTV('test', 'test tv', '123', [])
        Light sensor test turned off.
        >>> tv.executeCommand("40")
        Smart TV test executed command 40.
        """
        self.__changeBrightness(command)
        print("Smart TV " + self.getName() + " executed command " + str(command) + ".")

    def turnOn(self):
        """ test turnOn execution
        >>> tv = SmartTV('test', 'test tv', '123', [])
        Light sensor test turned off.
        >>> tv.turnOn()
        Light sensor test turned on.
        Smart TV test turned on.
        """
        self.__sensor.turnOn()
        print("Smart TV " + self.getName() + " turned on.")

    def turnOff(self):
        """ test turnOn execution
        >>> tv = SmartTV('test', 'test tv', '123', [])
        Light sensor test turned off.
        >>> tv.turnOff()
        Light sensor test turned off.
        Smart TV test turned off.
        """
        self.__sensor.turnOff()
        print("Smart TV " + self.getName() + " turned off.")

    def update(self, sensor, value, status):
        """ test update execution
        >>> tv = SmartTV('test', 'test tv', '123', [])
        Light sensor test turned off.
        >>> tv.update(None, 30, 1)
        Smart TV test works fine.
        >>> tv.update(None, 40, 1)
        Smart TV test got environmental brightness problems -> increasing brightness!
        >>> tv.update(None, 5, 2)
        Smart TV test got environmental brightness problems -> increasing brightness!
        """
        if status == Sensor.ERROR or value > self.__brightness:
            print("Smart TV", self.getName(), "got environmental brightness problems -> increasing brightness!")
            self.__brightness += 1
        else:
            print("Smart TV", self.getName(), "works fine.")

    def __changeBrightness(self, brightness):
        self.__brightness = brightness


if __name__ == "__main__":
    import doctest

    doctest.testmod()
