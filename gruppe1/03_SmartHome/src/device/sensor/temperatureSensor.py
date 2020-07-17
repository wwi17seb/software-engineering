from device.sensor.sensor import Sensor


# uses principle LSP, SDP, OCP, SRP, CCP
# implements Observer
class TemperatureSensor(Sensor):

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super(TemperatureSensor, self).__init__(name, description, serialNumber, connections, status, trigger)
        self.__currentTemp = 0  # °Celsius

    def turnOn(self):
        """ test turnOn execution
        >>> sensor = TemperatureSensor('test', 'test sensor', '123', None, 1, None)
        >>> sensor.turnOn()
        Temperature sensor test turned on.
        """
        print("Temperature sensor " + self.getName() + " turned on.")

    def turnOff(self):
        """ test turnOff execution
        >>> sensor = TemperatureSensor('test', 'test sensor', '123', None, 1, None)
        >>> sensor.turnOff()
        Temperature sensor test turned off.
        """
        print("Temperature sensor " + self.getName() + " turned off.")

    def measure(self):
        self.__currentTemp = 25
        return self.__currentTemp

    def getValue(self):
        return self.__currentTemp


if __name__ == "__main__":
    import doctest

    doctest.testmod()
