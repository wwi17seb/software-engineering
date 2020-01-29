from .sensor import Sensor

class HumiditySensor(Sensor):

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super.__init__(name, description, serialNumber, connections, status, trigger)
        self.__currentHumidity = 0 #Percentage

    def turnOn(self):
        print("Humidity sensor" + self.name + "turned on.")

    def turnOff(self):
        print("Humidity sensor" + self.name + "turned off.")

    def measure(self):
        self.__currentHumidity = 25

    def getValue(self):
         return self.__currentHumidity