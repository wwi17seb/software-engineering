from .sensor import Sensor
from .observer import Publisher, Subscriber

pub = Publisher()
temp1 = Subscriber('Temp1')
temp2 = Subscriber('Temp2')

pub.register(temp1, temp1.update)
pub.register(temp2, temp2.update)

class TemperatureSensor(Sensor):

    def __init__(self, name, description, serialNumber, macAddress, conntections, status, trigger):
        super(name, description, serialNumber, macAddress, conntections, status, trigger)
        self.currentTemp = 0

    def measure(self):
        print("Measurement of the current temperature.")
        pub.dispatch("Your value has been updated")
        self.currentTemp += 1

    def transmitEvent(self):
        print("Transmitting temperature sensor data from" + self.name + "to all connected devices ...")

    def turnOn(self):
        print("Temperature sensor" + self.name + "turned on.")

    def turnOff(self):
        print("Temperature sensor" + self.name + "turned off.")


