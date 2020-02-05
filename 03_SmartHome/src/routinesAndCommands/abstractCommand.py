import abc;

class Command(metaclass=abc.ABCMeta):

    def getName(self):
        return _name

    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass