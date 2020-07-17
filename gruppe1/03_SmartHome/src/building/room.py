# uses principle principle SDP, OCP, SRP, CCP
class Room():

    def __init__(self, height, name, area):
        self.__height = height
        self.__area = area
        self.__name = name
        self.__devices = []

    def addDevice(self, device):
        self.__devices.append(device)

    def getDevices(self):
        return self.__devices

    def removeDevice(self, name):
        for i in range(self.__devices):
            if self.__devices[i].getName() == name:
                self.__devices.pop(i)

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
