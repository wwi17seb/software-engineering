from device.sensor.sensor import Sensor


# uses principle LSP, SDP, OCP, SRP, CCP
# implements Observer
class SmokeSensor(Sensor):

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super(SmokeSensor, self).__init__(name, description, serialNumber, connections, status, trigger)
        self.__smoke = False

    def turnOn(self):
        """ test turnOn execution
        >>> sensor = SmokeSensor('test', 'test sensor', '123', None, 1, None)
        >>> sensor.turnOn()
        Smoke sensor test turned on.
        """
        print("Smoke sensor " + self.getName() + " turned on.")

    def turnOff(self):
        """ test turnOff execution
        >>> sensor = SmokeSensor('test', 'test sensor', '123', None, 1, None)
        >>> sensor.turnOff()
        Smoke sensor test turned off.
        """
        print("Smoke sensor " + self.getName() + " turned off.")

    def measure(self):
        self.__smoke = True
        return self.__smoke

    def getValue(self):
        return self.__smoke


if __name__ == "__main__":
    import doctest

    doctest.testmod()
