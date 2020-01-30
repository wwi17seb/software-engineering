from __future__ import annotations
from abc import ABC, abstractmethod

# uses SRP, OCP, LSP(Oberklasse), 
class AbstractDevice(ABC):

    def __init__(self, name, description, serialNumber, conntections):
        self.__name = name
        self.__description = description
        self.__serialNumber = serialNumber
        self.__connections = conntections

    @abstractmethod
    def turnOn(self):
        raise NotImplementedError

    @abstractmethod
    def turnOff(self):
        raise NotImplementedError

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__description = description

    def getSerialNumber(self):
        return self.__serialNumber

    def getConnections(self):
        return self.__connections
