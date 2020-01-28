from .sensor import Sensor


class SmokeSensor(Sensor):

    def __init__(self, name, description, serialNumber, conntections, status, trigger):
        super(name, description, serialNumber, conntections, status, trigger)
        self.__smoke = False

    def turnOn(self):
        print("Smoke sensor" + self.name + "turned on.")

    def turnOff(self):
        print("Smoke sensor" + self.name + "turned off.")

    def measure(self):
        self.__smoke = True

    def getValue(self):
        return self.__smoke
