

class RoomGroup():
    def __init__(self, name):
        self.name = name
        self.rooms = {}

    def addRoom(self, room):
        self.rooms[room.name] = room

    def getRooms(self):
        return self.rooms

    def getRoomByName(self, name):
        return self.rooms[name]