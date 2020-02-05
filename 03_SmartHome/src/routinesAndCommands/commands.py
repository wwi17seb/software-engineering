from routinesAndCommands.abstractCommand import Command

class turnOn(Command):
    _name = "Turn On"

    def execute(self):
        self._receiver.turnOn()

class turnOff(Command):
    _name = "Turn On"

    def execute(self):
        self._receiver.turnOff()