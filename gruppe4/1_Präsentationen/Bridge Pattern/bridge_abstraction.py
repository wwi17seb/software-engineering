from bridge_implementation import Device

class Controller:

    def __init__(self, device: Device):
        self.device = device

    def togglePower(self):
        # anschalten, wenn device aus, bzw. 
        # ausschalten, wenn device an
        if self.device.isEnabled() == True:
            self.device.disable()
        else:
            self.device.enable()

    def increase(self):
        # 1 Stufe hoch
        self.device.setLevel(self.device.getLevel() + 1)

    def decrease(self):
        # 1 Stufe herunter
        self.device.setLevel(self.device.getLevel() - 1)



class AdvancedController(Controller):

    def setTimer(self, time):
        # einen Timer stellen zum An-/Ausschalten
        pass
