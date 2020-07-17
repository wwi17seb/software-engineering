from abc import ABC, abstractmethod

class IObservable(ABC):

    @abstractmethod
    def update(self):
        pass