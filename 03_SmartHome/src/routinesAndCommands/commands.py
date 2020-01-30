from routinesAndCommands.abstractCommand import Command

class turnOn(Command):
    def execute(self):
        self._receiver.turnOn()

class turnOff(Command):
    def execute(self):
        self._receiver.turnOff()
