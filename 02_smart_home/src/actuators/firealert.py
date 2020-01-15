from .actuator import Actuator


class FireAlert(Actuator):

    def __init__(self, name, room):
        Actuator.__init__(self, name, room)
        self.state = False

    def turnOff(self):
        self.state = False

    def turnOn(self):
        self.state = True
        print("SHIT'S ON FIRE; YO!")

    def __str__(self):
        return str(self.name) + " (FireAlert, " + str(self.room) + \
            "): " + str(self.state)
