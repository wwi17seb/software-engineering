
class House(object):
    __instance = None

    def __new__(cls, city, address):
        if House.__instance is None:
            House.__instance = object.__new__(cls)
        House.__instance.city = city
        House.__instance.address = address
        return House.__instance

    def __init__(self, city, address):
        self.city = city
        self.address = address
        self.roomGroups = {}

    def addRoomGroup(self, roomGroup):
        self.roomGroups[roomGroup.name] = roomGroup

    def getRoomGroups(self):
        return self.roomGroups

    def getRoomGroupByName(self, name):
        return self.roomGroups[name]






