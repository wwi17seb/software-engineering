from __future__ import annotations
from abc import abstractmethod
from ..abstractDevice import AbstractDevice


class ConnectionDevice(AbstractDevice):
    connectionList = []

    @abstractmethod
    def transmitData(self, data, src, target):
        pass

    @abstractmethod
    def connectDevices(self, device1, device2):
        pass
