from device.sensor.sensor import Sensor

# uses principle LSP, SDP, OCP, SRP, CCP
# implements Observer
class LightSensor(Sensor):

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super(LightSensor, self).__init__(name, description, serialNumber, connections, status, trigger)
        self.__currentBrightness = 0  # Lumen

    def turnOn(self):
        """ test turnOn execution
        >>> sensor = LightSensor('test', 'test sensor', '123', None, 1, None)
        >>> sensor.turnOn()
        Light sensor test turned on.
        """
        print("Light sensor " + self.getName() + " turned on.")

    def turnOff(self):
        """ test turnOff execution
        >>> sensor = LightSensor('test', 'test sensor', '123', None, 1, None)
        >>> sensor.turnOff()
        Light sensor test turned off.
        """
        print("Light sensor " + self.getName() + " turned off.")

    def measure(self):
        self.__currentBrightness = 25

    def getValue(self):
        return self.__currentBrightness

if __name__ == "__main__":
    import doctest

    doctest.testmod()