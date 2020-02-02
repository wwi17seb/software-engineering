from .isensor import ISensor
from .itarget import ITarget

class LightSensor(ISensor,ITarget):

    def __init__(self,room):
        ISensor.__init__(self,"Lichtsensor","Lumen",room)
        ITarget.__init__(self)
        self.setTarget(80)

    def measurement(self):
        self.setState(80)
