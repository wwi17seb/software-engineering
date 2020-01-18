from ..smartdevice import SmartDevice

class Window(SmartDevice):
    def __init__(self,room):
        SmartDevice.__init__(self,room)

    def open(self):

        if self.state == 0:
            self.state=1
            print("Fenster wurde geöffnet")

        else:
            print("Fenster ist bereits geöffnet")

    def close(self):

        if self.state == 1:
            self.state=0
            print("Fenster wurde geschlossen")
        else:
            print("Fenster ist bereits geschlossen")
