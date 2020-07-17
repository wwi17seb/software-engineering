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

    def removeRoom(self, name):
        for i in range(self.__rooms):
            if self.__rooms[i].getName() == name:
                room = self.__rooms[i]
                if len(room.getDevices()) == 0:
                    self.__rooms.pop(i)
                else:
                    print("Can not remove room " + name)
                    # TODO Exception?