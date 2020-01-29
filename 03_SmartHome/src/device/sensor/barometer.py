from .sensor import Sensor


class Barometer(Sensor):

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super(Barometer, self).__init__(name, description, serialNumber, connections, status, trigger)
        self.__currentPressure = 0  # in PSI

    def turnOn(self):
        print("Barometer" + self.__name + "turned on.")

    def turnOff(self):
        print("Barometer" + self.__name + "turned off.")

    def measure(self):
        self.__currentPressure = 25

    def getValue(self):
        return self.__currentPressure
