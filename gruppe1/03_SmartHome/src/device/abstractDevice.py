from __future__ import annotations
from abc import ABC, abstractmethod
from routinesAndCommands.commands import turnOn, turnOff

# uses SRP, OCP, LSP(Oberklasse), 
class AbstractDevice(ABC):

    def __init__(self, name, description, serialNumber, conntections):
        self._name = name
        self._description = description
        self._serialNumber = serialNumber
        self._connections = conntections
        self._commands = [turnOn(self), turnOff(self)]

    @abstractmethod
    def turnOn(self):
        raise NotImplementedError

    @abstractmethod
    def turnOff(self):
        raise NotImplementedError

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getDescription(self):
        return self._description

    def setDescription(self, description):
        self._description = description

    def getSerialNumber(self):
        return self._serialNumber

    def getConnections(self):
        return self._connections

    def getCommands(self):
        return self._commands
