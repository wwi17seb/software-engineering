from .sensor import Sensor


class Microphone(Sensor):

    def __init__(self, name, room):
        Sensor.__init__(self, name, room)

    def readValue(self):
        # value gets injected by command line
        pass

    def clear(self):
        self.value = None

    def __str__(self):
        return str(self.name) + " (Microphone, " + str(self.room) + \
            "): " + str(self.value)
