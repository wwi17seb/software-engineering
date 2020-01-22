import abc


class Client:

    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()


class Command(metaclass=abc.ABCMeta):

    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass


# concrete Command
class LampSwitch(Command):

    def execute(self):
        self._receiver.switchLamp()


# concrete Command
class PlayMusic(Command):

    def execute(self):
        self._receiver.switchMusicOnOff()


# Lampe
class Lamp:

    def __init__(self):
        self.lampOn = False

    def switchLamp(self):
        if self.lampOn == False:
            self.lampOn = True
            print("Lampe an")
            # print(self.lampOn)
        else:
            self.lampOn = False
            print("Lampe aus")
            # print(self.lampOn)


class SonosBox:

    def __init__(self):
        self.musicOn = False

    def switchMusicOnOff(self):
        if self.musicOn == False:
            self.musicOn = True
            print("The beat drops!")
            # print(self.musicOn)
        else:
            self.musicOn = False
            print("Enjoy the silence!")
            # print(self.musicOn)


def main():
    philipsHue = Lamp()
    lampSwitch = LampSwitch(philipsHue)
    sonosBox = SonosBox()
    musicSwitch = PlayMusic(sonosBox)
    client = Client()
    client.store_command(lampSwitch)
    client.store_command(musicSwitch)
    client.store_command(musicSwitch)
    client.execute_commands()


if __name__ == "__main__":
    main()
