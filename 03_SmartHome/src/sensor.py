from __future__ import annotations
from abc import abstractmethod
from abstractDevice import AbstractDevice

class Sensor(AbstractDevice):

    def __init__(self, name, description, serialNumber, macAddress, conntections, status, trigger):
        super(name, description, serialNumber, macAddress, conntections)
        self.status = status
        self.trigger = trigger

    @abstractmethod
    def mesure(self):
        pass

    @abstractmethod
    def transmitEvent(self):
        pass
