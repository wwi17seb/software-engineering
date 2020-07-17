from __future__ import annotations
from abc import abstractmethod
from ..abstractDevice import AbstractDevice

# uses principle principle SDP, OCP, SRP, CCP, LSP
class SmartDevice(AbstractDevice):

    @abstractmethod
    def collectData(self):
        raise NotImplementedError

    @abstractmethod
    def executeCommand(self, command):
        raise NotImplementedError

    @abstractmethod
    def update(self, sensor, value):
        raise NotImplementedError
