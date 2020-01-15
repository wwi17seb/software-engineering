import abc


class Sensor(metaclass=abc.ABCMeta):

    def __init__(self, name, room):
        self.name = name
        self.value = None
        self.room = room

    def getValue(self):
        self.readValue()
        return self.value

    @abc.abstractmethod
    def readValue(self):
        raise NotImplementedError
