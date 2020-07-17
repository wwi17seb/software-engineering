from device.smartDevice.smartDevice import SmartDevice
from device.sensor.temperatureSensor import TemperatureSensor
from device.sensor.sensor import Sensor


# uses principle principle SDP, OCP, SRP, CCP
class Microwave(SmartDevice):
    DEFAULT_TEMP = 20

    def __init__(self, name, description, serialNumber, connections, maxPower):
        super(Microwave, self).__init__(name, description, serialNumber, connections)
        self.__maxPower = maxPower
        self.__temperature = self.DEFAULT_TEMP
        self.__currentPower = 0
        self.__timer = 0
        self.__sensor = TemperatureSensor(name, description, None, None, 1, 20)
        self.__sensor.turnOff()
        self.__sensor.register(self, self.update)

    def collectData(self):
        """ test collectData execution
        >>> microwave = Microwave('test', 'test microwave', '123', [], 300)
        Temperature sensor test turned off.
        >>> microwave.collectData()
        Smart microwave test collects data from sensors...
        0
        """
        print("Smart microwave " + self.getName() + " collects data from sensors...")
        print(str(self.__sensor.getValue()))

    def executeCommand(self, command):
        """ test executeCommand execution
        >>> microwave = Microwave('test', 'test microwave', '123', [], 5)
        Temperature sensor test turned off.
        >>> microwave.executeCommand("increase power")
        Smart microwave test executed command increase power.
        """
        print("Smart microwave " + self.getName() + " executed command " + str(command) + ".")

    def turnOn(self):
        """ test turnOn execution
        >>> microwave = Microwave('test', 'test oven', '123', [], 50)
        Temperature sensor test turned off.
        >>> microwave.turnOn()
        Please set the power!
        >>> microwave.setPower(300)
        >>> microwave.turnOn()
        Please set a max temperature for your food!
        >>> microwave.setTemperature(50)
        >>> microwave.turnOn()
        Please set a timer for your food!
        >>> microwave.setTimer(5)
        >>> microwave.turnOn()
        Temperature sensor test turned on.
        Smart microwave test turned on.
        """
        if self.__currentPower == 0:
            print("Please set the power!")
            return
        elif self.__temperature == self.DEFAULT_TEMP:
            print("Please set a max temperature for your food!")
            return
        elif self.__timer == 0:
            print("Please set a timer for your food!")
            return

        self.__sensor.turnOn()
        print("Smart microwave " + self.getName() + " turned on.")

    def turnOff(self):
        """ test turnOff execution
        >>> microwave = Microwave('test', 'test microwave', '123', [], 300)
        Temperature sensor test turned off.
        >>> microwave.turnOff()
        Temperature sensor test turned off.
        Smart microwave test turned off.
        """
        self.__currentPower = 0
        self.__timer = 0
        self.__temperature = 0
        self.__sensor.turnOff()
        print("Smart microwave " + self.getName() + " turned off.")

    def update(self, sensor, value, status):
        """ test update execution
        >>> microwave = Microwave('test', 'test fridge', '123', [], 300)
        Temperature sensor test turned off.
        >>> microwave.setTemperature(50)
        >>> microwave.update(None, 50, 1)
        Microwave test temperature is 50
        >>> microwave.update(None, 10, 1)
        Microwave test got temperature problems!
        >>> microwave.update(None, 50, 2)
        Microwave test got temperature problems!
        """
        if status == Sensor.ERROR or value != self.__temperature:
            print("Microwave", self.getName(), "got temperature problems!")
            self.__temperature = value
        else:
            print("Microwave", self.getName(), "temperature is", value)

    def setTemperature(self, temp):
        self.__temperature = temp
        self.__sensor.setTrigger(temp)

    def setPower(self, power):
        self.__currentPower = power

    def setTimer(self, timer):
        self.__timer = timer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
