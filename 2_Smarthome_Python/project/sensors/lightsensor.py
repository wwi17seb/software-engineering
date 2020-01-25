from .isensor import ISensor

class LightSensor(ISensor):

    def __init__(self):
        ISensor.__init__(self,"Lichtsensor","Lumen")
        self.setTarget(80)

    def measurement(self):
        self.setState(80)
