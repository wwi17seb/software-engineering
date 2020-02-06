from routinesAndCommands.abstractCommand import Command

class turnOn(Command):
    def __init__(self, receiver):
        self._receiver = receiver
        self._name = " "
        self._name = "Turn On"

    def execute(self):
        self._receiver.turnOn()

class turnOff(Command):
    def __init__(self, receiver):
        self._receiver = receiver
        self._name = " "
        self._name = "Turn Off"

    def execute(self):
        self._receiver.turnOff()