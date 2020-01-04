from actuator import Actuator

class LED(Actuator):
    def __init__(self):
        pass

    def write(self, value):
        if (value):
            print("LED turned on")
        else:
            print("LED turned off")