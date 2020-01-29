from .sensor import Sensor

# uses principle LSP, SDP, OCP, SRP, CCP
# implements Observer
class LightSensor(Sensor):

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super(LightSensor, self).__init__(name, description, serialNumber, connections, status, trigger)
        self.__currentBrightness = 0  # Lumen

    def turnOn(self):
        print("Light sensor" + self.__name + "turned on.")

    def turnOff(self):
        print("Light sensor" + self.__name + "turned off.")

    def measure(self):
        self.__currentBrightness = 25

    def getValue(self):
        return self.__currentBrightness
