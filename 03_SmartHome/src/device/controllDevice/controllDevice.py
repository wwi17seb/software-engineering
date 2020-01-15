from __future__ import annotations
from abc import ABC, abstractmethod
from ..abstractDevice import AbstractDevice

class ControllDevice(AbstractDevice):

    @abstractmethod
    def transmitCommand(self, command):
        pass

    @abstractmethod
    def createRoutine(self):
        pass
