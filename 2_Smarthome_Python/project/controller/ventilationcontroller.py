from .icontroller import IController
from smartdevices.ventilation.window import Window

class VentilationController(IController):
    def __init__(self):
        IController.__init__(self,"LueftungsController")
        self.windows=[]

    def addWindow(self, room):
        window = Window(room)
        self.windows.append(window)
        room.smartdevices.append(window)

    def ventilateRoom(self,room):
        if self.status==1:
            for window in self.windows:
                if window.room == room:
                    window.open()
                else:
                    print("Kein automatisches Fenster in " + room.name + " verfügbar.")

    def stopVentilateRoom(self,room):
        if self.status==1:
            for window in self.windows:
                if window.room == room:
                    window.close()
                else:
                    print("Kein automatisches Fenster in " + room.name + " verfügbar.")
