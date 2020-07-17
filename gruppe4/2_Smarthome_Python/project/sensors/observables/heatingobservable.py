from ..iobservable import IObservable
#Observer Verhaltensmuster
class heatingObservable(IObservable):

    def update(self, hsensor):
        if hsensor.getData() == hsensor.target:
            print("Zieltemperatur erreicht: " + str(hsensor.getData()) + " Grad " +hsensor.unit)
            hsensor.room.smarthome.heatingcontroller.stopHeatRoom(hsensor.room)