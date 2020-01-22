import abc


class Controller(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self, sensor, value):
        raise NotImplementedError

    @abc.abstractmethod
    def main(self):
        raise NotImplementedError
