from items.item import Item
import abc


class Actuator(Item, metaclass=abc.ABCMeta):

    def __init__(self, name, room):
        Item.__init__(self, name, room)
