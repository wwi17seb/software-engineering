from item import Item
import abc


class Sensor(Item, metaclass=abc.ABCMeta):

    def __init__(self, name, room):
        Item.__init__(self, name, room)
        self.value = None

    def getValue(self):
        self.readValue()
        return self.value

    @abc.abstractmethod
    def readValue(self):
        raise NotImplementedError
