from .sensor import Sensor

COLOR_MAP = {
    "white": "#ffffff",
    "red": "#ff0000",
    "green": "#00ff00",
    "blue": "#0000ff",
    "yellow": "#ffff00",
    "orange": "#ff8000"
}

class ColorSetter(Sensor):

    def __init__(self, name):
        Sensor.__init__(self, name)

    def readValue(self):
        # value gets injected by command line
        if (self.value == None):
            self.value = "#000000"
        elif (self.value in COLOR_MAP):
            self.value = COLOR_MAP[self.value]
        elif (self.value[0] == "#" and len(self.value) == 7):
            pass
        else:
            self.value = "#000000"

    def __str__(self):
        return str(self.name) + " (ColorSetter): " + str(self.value)
