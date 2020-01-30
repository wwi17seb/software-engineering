from __future__ import annotations
from abc import abstractmethod
from ..abstractDevice import AbstractDevice

# uses principle LSP, SDP, OCP, SRP, CCP
# uses Observer pattern with specified sensors
class Sensor(AbstractDevice):
    GOOD = 1
    ERROR = 2

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super(Sensor, self).__init__(name, description, serialNumber, connections)
        self.__status = status
        self.__trigger = trigger
        self.__subscribers = dict()

    @abstractmethod
    def measure(self):
        raise NotImplementedError

    @abstractmethod
    def getValue(self):
        raise NotImplementedError

    def setTrigger(self, trigger):
        self.__trigger = trigger

    def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.__subscribers[who] = callback

    def unregister(self, who):
        del self.__subscribers[who]

    def dispatch(self):
        if self.getValue() != self.__trigger:
            self.__status = self.ERROR
        else:
            self.__status = self.GOOD

        for subscriber, callback in self.__subscribers.items():
            callback(self, self.getValue(), self.getStatus())
