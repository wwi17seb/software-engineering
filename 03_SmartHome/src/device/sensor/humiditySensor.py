from .sensor import Sensor

# uses principle LSP, SDP, OCP, SRP, CCP
# implements Observer
class HumiditySensor(Sensor):

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super(HumiditySensor,self).__init__(name, description, serialNumber, connections, status, trigger)
        self.__currentHumidity = 0 #Percentage

    def turnOn(self):
        print("Humidity sensor" + self.__name + "turned on.")

    def turnOff(self):
        print("Humidity sensor" + self.__name + "turned off.")

    def measure(self):
        self.__currentHumidity = 25

    def getValue(self):
         return self.__currentHumidity
