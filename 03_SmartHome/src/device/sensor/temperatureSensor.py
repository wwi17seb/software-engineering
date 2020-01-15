from .sensor import Sensor


class TemperatureSensor(Sensor):

    def __init__(self, name, description, serialNumber, macAddress, conntections, status, trigger):
        super(name, description, serialNumber, macAddress, conntections, status, trigger)
        self.currentTemp = 0

    def measure(self):
        print("Measurement of the current temperature.")
        self.currentTemp += 1

    def transmitEvent(self):
        print("Transmitting temperature sensor data from" + self.name + "to all connected devices ...")

    def turnOn(self):
        print("Temperature sensor" + self.name + "turned on.")

    def turnOff(self):
        print("Temperature sensor" + self.name + "turned off.")

