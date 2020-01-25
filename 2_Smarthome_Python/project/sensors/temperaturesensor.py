from .isensor import ISensor
from .heatingobservable import heatingObservable

class TemperatureSensor(ISensor):

    def __init__(self,room):
        ISensor.__init__(self,"Temperatursensor","Celsius",room)
        self.observable = heatingObservable()

    def setState(self,state):
        self.state=state
        self.observable.update(self)


    def measurement(self):
        self.setState(22)
