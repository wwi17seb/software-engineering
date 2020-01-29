# uses principle principle SDP, OCP, SRP, CCP
class RoomGroup():
    def __init__(self, name):
        self.__name = name
        self.__rooms = []

    def addRoom(self, room):
        self.__rooms.append(room)

    def getRooms(self):
        return self.__rooms

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
