from .sensor import Sensor


class TemperatureSensor(Sensor):

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super(TemperatureSensor, self).__init__(name, description, serialNumber, connections, status, trigger)
        self.__currentTemp = 0  # °Celsius

    def turnOn(self):
        print("Temperature sensor" + self.__name + "turned on.")

    def turnOff(self):
        print("Temperature sensor" + self.__name + "turned off.")

    def measure(self):
        self.__currentTemp = 25

    def getValue(self):
        return self.__currentTemp
