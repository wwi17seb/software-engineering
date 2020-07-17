from device.sensor.sensor import Sensor


# uses principle LSP, SDP, OCP, SRP, CCP
# implements Observer
class HumiditySensor(Sensor):

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super(HumiditySensor, self).__init__(name, description, serialNumber, connections, status, trigger)
        self.__currentHumidity = 0  # Percentage

    def turnOn(self):
        """ test turnOn execution
        >>> sensor = HumiditySensor('test', 'test sensor', '123', None, 1, None)
        >>> sensor.turnOn()
        Humidity sensor test turned on.
        """
        print("Humidity sensor " + self.getName() + " turned on.")

    def turnOff(self):
        """ test turnOff execution
        >>> sensor = HumiditySensor('test', 'test sensor', '123', None, 1, None)
        >>> sensor.turnOff()
        Humidity sensor test turned off.
        """
        print("Humidity sensor " + self.getName() + " turned off.")

    def measure(self):
        self.__currentHumidity = 25

    def getValue(self):
        return self.__currentHumidity


if __name__ == "__main__":
    import doctest

    doctest.testmod()
