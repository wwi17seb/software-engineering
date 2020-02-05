class Routine:

    def __init__(self, name):
        self.name = name
        self.commands = []

    def addCommand(self, command):
        self.commands.append(command)
    
    def executeCommands(self):
        for command in self.commands: 
            command.execute();

    def getName(self):
        return self.name