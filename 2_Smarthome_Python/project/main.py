from room import Room
from controller.smarthome import Smarthome

def raumHinzufuegen(smarthome):
    print("\nBitte geben Sie die Ebene des Raumes an:")
    ebene = input("Ebene als Zahl: ")
    print("\nBitte geben Sie den Namen des Raumes an:")
    name = input("Raumname: ")
    smarthome.addRoom(ebene,name)

def heizungHinzufuegen(smarthome):
    print("\nBitte geben Sie die Ebene des Raumes an:")
    ebene = input("Ebene als Zahl: ")
    print("\nBitte geben Sie den Namen des Raumes an:")
    name = input("Raumname: ")
    raum = smarthome.getRoomByName(ebene,name)

    if raum!=None:
        smarthome.heatingcontroller.addHeater(raum)
    else:
        print("Raum existiert nicht.")

def lampeHinzufuegen(smarthome):
    print("\nBitte geben Sie die Ebene des Raumes an:")
    ebene = input("Ebene als Zahl: ")
    print("\nBitte geben Sie den Namen des Raumes an:")
    name = input("Raumname: ")
    raum = smarthome.getRoomByName(ebene,name)

    if raum!=None:
        smarthome.lightingcontroller.addLamp(raum)
    else:
        print("Raum existiert nicht.")

def rolladenHinzufuegen(smarthome):
    print("\nBitte geben Sie die Ebene des Raumes an:")
    ebene = input("Ebene als Zahl: ")
    print("\nBitte geben Sie den Namen des Raumes an:")
    name = input("Raumname: ")
    raum = smarthome.getRoomByName(ebene,name)

    if raum!=None:
        smarthome.lightingcontroller.addShutter(raum)
    else:
        print("Raum existiert nicht.")

def smartWindowHinzufuegen(smarthome):
    print("\nBitte geben Sie die Ebene des Raumes an:")
    ebene = input("Ebene als Zahl: ")
    print("\nBitte geben Sie den Namen des Raumes an:")
    name = input("Raumname: ")
    raum = smarthome.getRoomByName(ebene,name)

    if raum!=None:
        smarthome.ventilationcontroller.addWindow(raum)
    else:
        print("Raum existiert nicht.")

def zurueck():
    pass

def geraetHinzufuegen(smarthome):
    print("\nWelches Gerät möchten Sie hinzufügen?")
    print("\n1. Heizung hinzufügen")
    print("2. Lampe hinzufügen")
    print("3. Rolladen hinzufügen")
    print("4. Smart Window hinzufügen")
    print("5. zurück")
    eingabe = input("Wählen Sie eine Nummer: ")

    if eingabe=="1":
        heizungHinzufuegen(smarthome)
    elif eingabe=="2":
        lampeHinzufuegen(smarthome)
    elif eingabe=="3":
        rolladenHinzufuegen(smarthome)
    elif eingabe=="4":
        smartWindowHinzufuegen(smarthome)
    elif eingabe=="5":
        zurueck()
    else:
        print("Ungültige Zahl")

def beenden():
    return 1

def menu(smarthome):
    #Smarthome starten
    smarthome.systemStart()
    run = 0
    while run==0:
        print("\nSmarthome System: Bitte wählen Sie eine Option")
        print("\n1. Raum hinzufügen")
        print("2. Gerät hinzufügen")
        print("3. Raum heizen")
        print("4. Raum lüften")
        print("5. Licht an/aus")
        print("6. Beenden")
        eingabe = input("Wählen Sie eine Nummer: ")

        if eingabe == "1":
            raumHinzufuegen(smarthome)
        elif eingabe == "2":
            geraetHinzufuegen(smarthome)
        elif eingabe == "6":
            run=beenden()
        else:
            print("Ungültige Zahl")



def main():
    #neues Smarthome Objekt erzeugen
    smarthome = Smarthome("Smarthome",[])



    #ein paar Räume hinzufügen
#    smarthome.addRoom(2,"Wohnzimmer")
#    smarthome.addRoom(2,"Küche")
#    smarthome.addRoom(2,"Schlafzimmer")
    #Raum doppelt hinzufügen
#    smarthome.addRoom(2,"Küche")


    #Heizung hinzufügen
#    smarthome.heatingcontroller.addHeater(smarthome.rooms[0])

    #Lampe und Shutter hinzufügen
#    smarthome.lightingcontroller.addLamp(smarthome.rooms[0])
#    smarthome.lightingcontroller.addShutter(smarthome.rooms[0])

    #Smarte Fenster hinzufügen
#    smarthome.ventilationcontroller.addWindow(smarthome.rooms[0])
#    smarthome.ventilationcontroller.addWindow(smarthome.rooms[0])

    #Raum heizen
#    smarthome.heatingcontroller.heatRoom(smarthome.ventilationcontroller,smarthome.rooms[0],23)

    #Raum lueften
#    smarthome.ventilationcontroller.ventilateRoom(smarthome.heatingcontroller,smarthome.rooms[0])

    #Raum heizen
#    smarthome.heatingcontroller.heatRoom(smarthome.ventilationcontroller,smarthome.rooms[0],24)

    # Raum beleuchten
#    smarthome.lightingcontroller.lightRoom(smarthome.rooms[0])
#    smarthome.lightingcontroller.dimRoom(smarthome.rooms[0])

#    smarthome.systemShutdown()

    menu(smarthome)



if __name__ == "__main__":
    main()
