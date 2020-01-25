from .isensor import ISensor

class LightSensor(ISensor):

    def __init__(self):
        ISensor.__init__(self,"Lichtsensor","Lumen")

    def measurement(self):
        self.setState(80)
