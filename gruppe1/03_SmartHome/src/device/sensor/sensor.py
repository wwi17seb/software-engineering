from __future__ import annotations
from abc import abstractmethod
from device.abstractDevice import AbstractDevice

# uses principle LSP, SDP, OCP, SRP, CCP
# uses Observer pattern with specified sensors
class Sensor(AbstractDevice):
    GOOD = 1
    ERROR = 2

    def __init__(self, name, description, serialNumber, connections, status, trigger):
        super(Sensor, self).__init__(name, description, serialNumber, connections)
        self._status = status
        self._trigger = trigger
        self._subscribers = dict()

    @abstractmethod
    def measure(self):
        raise NotImplementedError

    @abstractmethod
    def getValue(self):
        raise NotImplementedError

    def setTrigger(self, trigger):
        self._trigger = trigger

    def getStatus(self):
        return self._status

    def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self._subscribers[who] = callback

    def unregister(self, who):
        del self._subscribers[who]

    def dispatch(self):
        if self.getValue() != self._trigger:
            self._status = self.ERROR
        else:
            self._status = self.GOOD

        print("Sensor", self.getName(), "dispatching data...")
        for subscriber, callback in self._subscribers.items():
            callback(self, self.getValue(), self.getStatus())
