
from __future__ import annotations
from abc import ABC, abstractmethod
class Connection(ABC):

    def __init__(self):
        self.connectedDevices = {}

    @abstractmethod
    def connect(self, device):
        pass

    
    @abstractmethod
    def disconnect(self, device):
        pass

    @abstractmethod
    def checkCompatibility(self, device):
        pass