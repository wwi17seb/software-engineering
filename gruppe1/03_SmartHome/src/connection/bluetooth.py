from .connection import Connection

# uses principle principle SDP, OCP, SRP, CCP, LSP
class Bluetooth(Connection):

    def __init__(self):
        super(Bluetooth, self).__init__()

    def connect(self, device):
        pass

    def disconnect(self, device):
        pass

    def checkCompatibility(self, device):
        pass