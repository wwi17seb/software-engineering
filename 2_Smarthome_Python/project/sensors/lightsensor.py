from .isensor import ISensor

class LightSensor(ISensor):

    def __init__(self,room):
        ISensor.__init__(self,"Lichtsensor","Lumen",room)
        self.setTarget(80)

    def measurement(self):
        self.setState(80)
