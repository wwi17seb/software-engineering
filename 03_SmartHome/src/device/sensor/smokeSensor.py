from .sensor import Sensor

# uses principle LSP, SDP, OCP, SRP, CCP
# implements Observer
class SmokeSensor(Sensor):

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super(SmokeSensor, self).__init__(name, description, serialNumber, connections, status, trigger)
        self.__smoke = False

    def turnOn(self):
        print("Smoke sensor" + self.__name + "turned on.")

    def turnOff(self):
        print("Smoke sensor" + self.__name + "turned off.")

    def measure(self):
        self.__smoke = True

    def getValue(self):
        return self.__smoke
