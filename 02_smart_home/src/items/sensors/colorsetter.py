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

    def __init__(self, name, room):
        Sensor.__init__(self, name, room)

    def readValue(self):
        pass

    def parseValue(self, value):
        if (value == None):
            return "#000000"
        elif (value in COLOR_MAP):
            return COLOR_MAP[value]
        elif (value[0] == "#" and len(value) == 7):
            return value
        else:
            return "#000000"

    def __str__(self):
        return str(self.name) + " (ColorSetter, " + str(self.room) + \
            "): " + str(self._value)
