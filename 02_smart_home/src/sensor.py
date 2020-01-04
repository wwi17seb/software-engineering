from item import Item

class Sensor(Item):
    def __init__(self, room):
        Item.__init__(self, room)
        self.value = None

    def getValue(self):
        self.readValue()
        return self.value

    def readValue(self):
        print("Not implemented!")
