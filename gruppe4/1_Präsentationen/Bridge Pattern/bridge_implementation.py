class Device:

    def isEnabled(self):
        # True, wenn an / False, wenn aus
        pass

    def enable(self):
        # anschalten
        pass


    def disable(self):
        # ausschalten
        pass

    def getLevel(self):
        # Helligkeits/Wärme/... -Stufe zurückgeben
        pass 

    def setLevel(self, level):
        # Stufe setzen
        pass



class Lamp(Device):
    # ...
    pass


class Heater(Device):
    # ...
    pass


class Ventilator(Device):
    # ...
    pass
