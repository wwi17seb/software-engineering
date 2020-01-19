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
        print("Fenster hinzugefügt: " + str(window.id))

    def ventilateRoom(self,heatingcontroller,room):
        if self.state==1:
            available=0
            for window in self.windows:
                if window.room == room:
                    window.open()
                    available=1
            if available==1:
                heatingcontroller.stopHeatRoom(room)
            else:
                print("Kein automatisches Fenster in " + room.name + " verfügbar.")

    def stopVentilateRoom(self,room):
        if self.state==1:
            available=0
            for window in self.windows:
                if window.room == room:
                    window.close()
                    available=1
            if available==0:
                print("Kein automatisches Fenster in " + room.name + " verfügbar.")
