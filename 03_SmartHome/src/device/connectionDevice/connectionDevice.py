from __future__ import annotations
from abc import abstractmethod
from ..abstractDevice import AbstractDevice

# uses principle principle SDP, OCP, SRP, CCP, LSP
class ConnectionDevice(AbstractDevice):
    connectionList = []

    @abstractmethod
    def transmitData(self, data, src, target):
        pass

    @abstractmethod
    def connectDevices(self, device1, device2):
        pass
