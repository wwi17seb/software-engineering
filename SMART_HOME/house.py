
class Haus(object):
    __instance = None

    def __new__(cls, val):
        if Haus.__instance is None:
            Haus.__instance = object.__new__(cls)
        Haus.__instance.val = val
        return Haus.__instance

    def __init__(self, city, address):
        self.city = city
        self.address = address
        self.roomGroups = {}

    def addRoomGroup(self, roomGroup):
        self.roomGroups[roomGroup.name] = roomGroup






