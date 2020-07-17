from device.smartDevice.smartDevice import SmartDevice
from device.sensor.temperatureSensor import TemperatureSensor
from device.sensor.sensor import Sensor


# uses principle principle SDP, OCP, SRP, CCP
class Fridge(SmartDevice):

    def __init__(self, name, description, serialNumber, connections, temperature):
        super(Fridge, self).__init__(name, description, serialNumber, connections)
        self.__defaultTemperature = temperature
        self.__sensor = TemperatureSensor(name, description, None, None, 1, temperature)
        self.__sensor.register(self, self.update)
        self.__sensor.turnOff()
        self.currentTemp = temperature

    def collectData(self):
        """ test collectData execution
        >>> fridge = Fridge('test', 'test fridge', '123', [], 5)
        Temperature sensor test turned off.
        >>> fridge.collectData()
        Smart fridge test collects data from sensors...
        0
        """
        print("Smart fridge " + self.getName() + " collects data from sensors...")
        print(str(self.__sensor.getValue()))

    def executeCommand(self, command):
        """ test executeCommand execution
        >>> fridge = Fridge('test', 'test fridge', '123', [], 5)
        Temperature sensor test turned off.
        >>> fridge.executeCommand(5)
        Smart fridge test executed command 5.
        """
        self.__setTemperature(command)
        print("Smart fridge " + self.getName() + " executed command " + str(command) + ".")

    def turnOn(self):
        """ test turnOn execution
        >>> fridge = Fridge('test', 'test fridge', '123', [], 5)
        Temperature sensor test turned off.
        >>> fridge.turnOn()
        Temperature sensor test turned on.
        Smart fridge test turned on.
        """
        self.__sensor.turnOn()
        print("Smart fridge " + self.getName() + " turned on.")

    def turnOff(self):
        """ test turnOff execution
        >>> fridge = Fridge('test', 'test fridge', '123', [], 5)
        Temperature sensor test turned off.
        >>> fridge.turnOff()
        Temperature sensor test turned off.
        Smart fridge test turned off.
        """
        self.__sensor.turnOff()
        print("Smart fridge " + self.getName() + " turned off.")

    def update(self, sensor, value, status):
        """ test update execution
        >>> fridge = Fridge('test', 'test fridge', '123', [], 5)
        Temperature sensor test turned off.
        >>> fridge.update(None, 5, 1)
        Fridge test temperature is 5
        >>> fridge.update(None, 10, 1)
        Fridge test got temperature problems!
        >>> fridge.update(None, 5, 2)
        Fridge test got temperature problems!
        """
        if status == Sensor.ERROR or value != self.__defaultTemperature:
            print("Fridge", self.getName(), "got temperature problems!")
            self.currentTemp = value
        else:
            print("Fridge", self.getName(), "temperature is", value)

    def __setTemperature(self, temp):
        self.__defaultTemperature = temp
        self.__sensor.setTrigger(temp)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
