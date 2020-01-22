from item import Item
import abc

# Observer Pattern: Sensor is Subject
class Sensor(Item, metaclass=abc.ABCMeta):

    def __init__(self, name, room):
        Item.__init__(self, name, room)
        self._value = None
        self.observers = []

        self.setValue(None)

    def getValue(self):
        self.readValue()
        return self._value

    @abc.abstractmethod
    def readValue(self):
        # this would read the sensor in real life
        # needs to use setValue() instead of setting it directly
        raise NotImplementedError

    def parseValue(self, value):
        # converting raw data to desired type
        return value

    def setValue(self, value):
        value = self.parseValue(value)
        if (value != self._value):
            self._value = value
            self.notify()
        else:
            self._value = value

    def attach(self, obj):
        if (obj not in self.observers):
            self.observers.append(obj)

    def detach(self, obj):
        self.observers.remove(obj)

    def notify(self):
        for obj in self.observers:
            obj.update(self, self._value)
