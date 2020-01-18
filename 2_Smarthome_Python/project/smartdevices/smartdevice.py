import itertools

class SmartDevice:
    newId = itertools.count()
    def __init__(self,room):
        self.id = next(self.newId)
        self.room=room
        self.state=0
        self.room.smartdevices.append(self)
