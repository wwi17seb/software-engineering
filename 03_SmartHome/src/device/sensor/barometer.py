from .sensor import Sensor


class Bachometer(Sensor):

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super.__init__(name, description, serialNumber, connections, status, trigger)
        self.__currentPressure = 0  # in PSI

    def turnOn(self):
        print("Bachometer" + self.name + "turned on.")

    def turnOff(self):
        print("Bachometer" + self.name + "turned off.")

    def measure(self):
        self.__currentPressure = 25

    def getValue(self):
        return self.__currentPressure
