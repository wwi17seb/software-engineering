from .sensor import Sensor

class TemperatureSensor(Sensor):

    def __init__(self, name, description, serialNumber, conntections, status, trigger):
        super(name, description, serialNumber, conntections, status, trigger)
        self.currentTemp = 0

    def turnOn(self):
        print("Temperature sensor" + self.name + "turned on.")

    def turnOff(self):
        print("Temperature sensor" + self.name + "turned off.")

    def measure(self):
        self.currentTemp = 25


