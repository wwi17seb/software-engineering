import abc


class Actuator(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.name = name
