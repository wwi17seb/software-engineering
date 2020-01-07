from __future__ import annotations
from abc import ABC, abstractmethod
class AbstractDevice(ABC):

    def __init__(self, name, description, serialNumber, macAddress, conntections):
        self.name = name
        self.description = description
        self.serialNumber = serialNumber
        self.macAddress = macAddress
        self.connections = conntections

    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass