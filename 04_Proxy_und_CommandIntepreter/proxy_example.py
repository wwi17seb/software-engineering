import abc

class AbstractCmd(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, command):
        pass

class RealCmd(AbstractCmd):

    def execute(self, command):
        """ test command execution
        >>> cmd = RealCmd()
        >>> cmd.execute('test')
        test command executed.
        """
        print(f"{command} command executed.")


class ProxyCmd(AbstractCmd):

    def __init__(self, user):
        self.is_authorized = False

        if user == "Martin":
            self.is_authorized = True

        self.executor = RealCmd()
        self.restricted_commands = ['Alexa, mach dir Rollos runter!']

    def execute(self, command):
        """ test proxy command

        >>> admin_executor = ProxyCmd('Martin')
        >>> other_executor = ProxyCmd('Erik')
        >>> admin_executor.execute('Alexa, Licht an!')
        Alexa, Licht an! command executed.
        >>> admin_executor.execute('Alexa, mach dir Rollos runter!')
        Alexa, mach dir Rollos runter! command executed.
        >>> other_executor.execute('Alexa, Licht an!')
        Alexa, Licht an! command executed.
        >>> other_executor.execute('Alexa, mach dir Rollos runter!')
        Traceback (most recent call last):
        Exception: Alexa, mach dir Rollos runter! command is not allowed for non-owner users.
        """

        if self.is_authorized:
            self.executor.execute(command)
        else:
            if any([command.strip().startswith(cmd) for cmd in self.restricted_commands]):       
                raise Exception(f"{command} command is not allowed for non-owner users.")
            else:
                self.executor.execute(command)


if __name__ == '__main__':
    import doctest
    doctest.testmod()