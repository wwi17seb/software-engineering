import abc
from gegenstand import Gegenstand 

class Sensor(Gegenstand):
    def __init__(self, gerät, data = None):
        #Konstruktor
        self.connectedDevice = gerät
        self.data = data

    @abc.abstractmethod
    def messen(self):
        pass

    def automationZuordnen(self, automation):
        self.automation = automation