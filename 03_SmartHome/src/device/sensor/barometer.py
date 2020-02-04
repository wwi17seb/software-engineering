from device.sensor.sensor import Sensor

# uses principle LSP, SDP, OCP, SRP, CCP
# implements Observer
class Barometer(Sensor):

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super(Barometer, self).__init__(name, description, serialNumber, connections, status, trigger)
        self.__currentPressure = 0  # in PSI

    def turnOn(self):
        """ test turnOn execution
        >>> sensor = Barometer('test', 'test sensor', '123', None, 1, None)
        >>> sensor.turnOn()
        Barometer test turned on.
        """
        print("Barometer " + self.getName() + " turned on.")

    def turnOff(self):
        """ test turnOff execution
        >>> sensor = Barometer('test', 'test sensor', '123', None, 1, None)
        >>> sensor.turnOff()
        Barometer test turned off.
        """
        print("Barometer " + self.getName() + " turned off.")

    def measure(self):
        self.__currentPressure = 25

    def getValue(self):
        return self.__currentPressure

if __name__ == "__main__":
    import doctest

    doctest.testmod()