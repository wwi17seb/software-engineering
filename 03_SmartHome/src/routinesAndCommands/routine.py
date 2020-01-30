class Routine:

    def __init__(self, name):
        self.name = name
        self.commands = None

    def addCommand(self, command):
        self.commands.append(command)
    
    def executeCommands(self):
        for command in self.commands: 
            command.execute();
