from __future__ import annotations
from abc import abstractmethod
from ..abstractDevice import AbstractDevice


class SmartDevice(AbstractDevice):

    @abstractmethod
    def collectData(self):
        raise NotImplementedError

    @abstractmethod
    def exectuteCommand(self, command):
        raise NotImplementedError

    @abstractmethod
    def update(self, sensor, value):
        raise NotImplementedError
