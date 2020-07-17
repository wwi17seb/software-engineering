from .actuator import Actuator


class WhiteLight(Actuator):

    def __init__(self, name, room):
        Actuator.__init__(self, name, room)
        self.state = False

    def turnOn(self):
        self.state = True

    def turnOff(self):
        self.state = False

    def toggleLight(self):
        self.state = not self.state

    def __str__(self):
        return str(self.name) + " (WhiteLight, " + str(self.room) + \
            "): " + str(self.state)


if __name__ == "__main__":
    whiteLight = WhiteLight("testLight", None)
