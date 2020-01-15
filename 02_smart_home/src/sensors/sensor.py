import abc


class Sensor(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.name = name
        self.value = None

    def getValue(self):
        self.readValue()
        return self.value

    @abc.abstractmethod
    def readValue(self):
        raise NotImplementedError
