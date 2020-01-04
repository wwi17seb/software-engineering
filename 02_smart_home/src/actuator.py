from item import Item

class Actuator(Item):
    def __init__(self, room):
        Item.__init__(self, room)

    def write(self, value):
        print("Not implemented!")