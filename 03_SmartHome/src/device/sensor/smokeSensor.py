from .sensor import Sensor


class SmokeSensor(Sensor):

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super.__init__(name, description, serialNumber, connections, status, trigger)
        self.__smoke = False

    def turnOn(self):
        print("Smoke sensor" + self.name + "turned on.")

    def turnOff(self):
        print("Smoke sensor" + self.name + "turned off.")

    def measure(self):
        self.__smoke = True

    def getValue(self):
        return self.__smoke
