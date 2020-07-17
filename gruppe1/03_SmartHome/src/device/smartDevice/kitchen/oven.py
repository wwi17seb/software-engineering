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
        self.__sensor.register(self, self.update)

    def collectData(self):
        """ test collectData execution
        >>> oven = Oven('test', 'test oven', '123', [], 50)
        Temperature sensor test turned off.
        >>> oven.collectData()
        Smart oven test collects data from sensors...
        0
        """
        print("Smart oven " + self.getName() + " collects data from sensors...")
        print(str(self.__sensor.getValue()))

    def executeCommand(self, command):
        """ test executeCommand execution
        >>> oven = Oven('test', 'test oven', '123', [], 50)
        Temperature sensor test turned off.
        >>> oven.executeCommand("do something")
        Smart oven test executed command do something.
        """
        print("Smart oven " + self.getName() + " executed command " + str(command) + ".")

    def turnOn(self):
        """ test turnOn execution
        >>> oven = Oven('test', 'test oven', '123', [], 50)
        Temperature sensor test turned off.
        >>> oven.turnOn()
        Please set the temperature!
        >>> oven.setTemperature(30)
        >>> oven.turnOn()
        Please set a timer!
        >>> oven.setTimer(30)
        >>> oven.turnOn()
        Temperature sensor test turned on.
        Smart oven test turned on.
        """
        if self.__temperature == 0:
            print("Please set the temperature!")
            return
        elif self.__timer == 0:
            print("Please set a timer!")
            return

        self.__sensor.turnOn()
        print("Smart oven " + self.getName() + " turned on.")

    def turnOff(self):
        """ test turnOff execution
        >>> oven = Oven('test', 'test oven', '123', [], 50)
        Temperature sensor test turned off.
        >>> oven.turnOff()
        Temperature sensor test turned off.
        Smart oven test turned off.
        """
        self.__temperature = 0
        self.__timer = 0
        self.__sensor.turnOff()
        print("Smart oven " + self.getName() + " turned off.")

    def update(self, sensor, value, status):
        """ test update execution
        >>> oven = Oven('test', 'test fridge', '123', [], 50)
        Temperature sensor test turned off.
        >>> oven.setTemperature(50)
        >>> oven.update(None, 50, 1)
        Oven test temperature is 50
        >>> oven.update(None, 10, 1)
        Oven test got temperature problems!
        >>> oven.update(None, 50, 2)
        Oven test got temperature problems!
        """
        if sensor == self.__sensor:
            if status == Sensor.ERROR or value > self.__maxTemp or value != self.__temperature:
                print("Oven", self.getName(), "got temperature problems!")
                self.__temperature = value
            else:
                print("Oven", self.getName(), "temperature is", value)
        else:
            if status == Sensor.GOOD:
                print("Oven: "+ self.getName() + " registert sensor " + sensor.getName() + " status is good.")
            else:
                print("Oven: "+ self.getName() + " registert sensor " + sensor.getName() + " status is bad!! Please help!! :D")


    def setTemperature(self, temp):
        self.__temperature = temp
        self.__sensor.setTrigger(temp)

    def setTimer(self, timer):
        self.__timer = timer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
