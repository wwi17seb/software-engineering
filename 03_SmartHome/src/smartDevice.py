from __future__ import annotations
from abc import abstractmethod
from abstractDevice import AbstractDevice

class SmartDevice(AbstractDevice):

    @abstractmethod
    def collectData(self):
        pass

    @abstractmethod
    def exectuteCommand(self):
        pass
