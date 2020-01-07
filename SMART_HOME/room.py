

class Room():

    def __init__(self, height, name, area):
        self.height = height
        self.area = area
        self.name = name
        self.devices = {}

    def addDevice(self, device):
        self.devices[device.name] = device

    def getDevices(self):
        return self.devices

    def getDeviceByName(self, name):
        return self.devices[name]