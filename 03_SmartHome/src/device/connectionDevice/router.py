from .connectionDevice import ConnectionDevice

class Router(ConnectionDevice):

    def __init__(self, name, description, serialNumber, macAddress, conntections, ports):
        super().__init__(name, description, serialNumber, macAddress, conntections)
        self.ports = ports

    def transmitData(self, data, src, target):
        print("Transmitting data from %s to %s." % src.name, target.name)


    def connectDevices(self, device1, device2):
        if len(self.connectionList) < self.ports:
            self.connectionList.append((device1, device2))
        else:
            raise Exception("All ports are used!")

    def turnOn(self):
        print("Router  " + self.name + "turned on.")

    def turnOff(self):
        print("Router " + self.name + "turned off.")