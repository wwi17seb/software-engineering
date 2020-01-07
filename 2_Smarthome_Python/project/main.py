from room import Room
from controller.smarthome import Smarthome

def main():
    #neues Smarthome Objekt erzeugen
    smarthome = Smarthome("Smarthome",[])

    #ein paar Räume hinzufügen
    smarthome.addRoom(2,"Wohnzimmer")
    smarthome.addRoom(2,"Küche")
    smarthome.addRoom(2,"Schlafzimmer")
    #Raum doppelt hinzufügen
    smarthome.addRoom(2,"Küche")

    #Smarthome starten
    smarthome.systemStart()
    print("Smarthome Status: ",smarthome.status)

    #Heizung hinzufügen
    smarthome.heatingcontroller.addHeater(smarthome.rooms[0])

    #Lampe und Shutter hinzufügen
    smarthome.lightingcontroller.addLamp(smarthome.rooms[0])
    smarthome.lightingcontroller.addShutter(smarthome.rooms[0])

    #Raum heizen
    smarthome.heatingcontroller.heatRoom(smarthome.rooms[0],23)

    # Raum beleuchten
    smarthome.lightingcontroller.lightRoom(smarthome.rooms[0])
    smarthome.lightingcontroller.dimRoom(smarthome.rooms[0])

    smarthome.systemShutdown()
    print("Smarthome Status: ",smarthome.status)



if __name__ == "__main__":
    main()
