import abc;

class Command(metaclass=abc.ABCMeta):

    def __init__(self, receiver):
        self._receiver = receiver
        self._name = " "

    def getName(self):
        return self._name

    @abc.abstractmethod
    def execute(self):
        pass