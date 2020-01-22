class Room():

    def __init__(self, height, name, area):
        self.__height = height
        self.__area = area
        self.__name = name
        self.__devices = []

    def addDevice(self, device):
        self.devices[device.name] = device

    def getDevices(self):
        return self.devices

    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    def setArea(self, area):
        self.__area = area

    def getArea(self):
        return self.__area

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
