from ..isensor import ISensor
from ..itarget import ITarget
from sensors.observables.heatingobservable import heatingObservable

class TemperatureSensor(ISensor,ITarget):

    def __init__(self,room):
        ISensor.__init__(self,"Temperatursensor","Celsius",room)
        ITarget.__init__(self)
        self.observable = heatingObservable()
        self.setState(18)

    def setState(self,state):
        self.state=state
        self.observable.update(self)


    def measurement(self):
        self.setState(self.getData())
