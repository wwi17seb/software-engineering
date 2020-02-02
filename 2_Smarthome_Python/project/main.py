from house.room import Room
from controller.smarthome import Smarthome

def raumHinzufuegen(smarthome):

    print("\nBitte geben Sie den Namen des Raumes an:")
    name = input("Raumname: ")
    smarthome.addRoom(name)

def raumEingabe(smarthome):

    print("\nBitte geben Sie den Namen des Raumes an:")
    name = input("Raumname: ")
    raum = smarthome.getRoomByName(name)

    return raum

def heizungHinzufuegen(smarthome):
    raum=raumEingabe(smarthome)

    if raum!=None:
        smarthome.heatingcontroller.addHeater(raum)

def lampeHinzufuegen(smarthome):
    raum=raumEingabe(smarthome)

    if raum!=None:
        smarthome.lightingcontroller.addLamp(raum)

def rolladenHinzufuegen(smarthome):
    raum=raumEingabe(smarthome)

    if raum!=None:
        smarthome.lightingcontroller.addShutter(raum)

def smartWindowHinzufuegen(smarthome):
    raum=raumEingabe(smarthome)

    if raum!=None:
        smarthome.ventilationcontroller.addWindow(raum)

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

def heizen(smarthome):
    raum=raumEingabe(smarthome)

    if raum!=None:
        print("\nBitte geben Sie die gewünschte Temperatur ein:")
        temperatur=input("in Grad Celsius: ")
        smarthome.heatingcontroller.heatRoom(smarthome.ventilationcontroller,raum,int(temperatur))

def lueften(smarthome):
    raum=raumEingabe(smarthome)
    if raum!=None:
        smarthome.ventilationcontroller.ventilateRoom(smarthome.heatingcontroller,raum)

def lichtAn(smarthome):
    raum=raumEingabe(smarthome)
    if raum!=None:
        smarthome.lightingcontroller.lightRoom(raum)

def lichtAus(smarthome):
    raum=raumEingabe(smarthome)
    if raum!=None:
        smarthome.lightingcontroller.dimRoom(raum)

def lichtAnAus(smarthome):
    print("\nWas möchten Sie tun?")
    print("\n1. Licht anschalten")
    print("2. Licht ausschalten")
    print("3. zurück")
    eingabe = input("Wählen Sie eine Nummer: ")
    if eingabe=="1":
        lichtAn(smarthome)
    elif eingabe=="2":
        lichtAus(smarthome)
    elif eingabe=="5":
        zurueck()
    else:
        print("Ungültige Zahl")

def beenden(smarthome):
    smarthome.systemShutdown()
    return 1

def menu(smarthome):
    #Smarthome starten
    smarthome.systemStart()
    #Raum heizen
    smarthome.heatingcontroller.heatRoom(smarthome.ventilationcontroller,smarthome.rooms[0],23)
    smarthome.rooms[0].hsensor.setState(23)
    run = 0
    while run==0:
        print("\nSmarthome System: Bitte wählen Sie eine Option")
        print("\n1. Raum hinzufügen")
        print("2. Gerät hinzufügen")
        print("3. Raum heizen")
        print("4. Raum lüften")
        print("5. Licht an/aus")
        print("6. Beenden")
        eingabe = input("> ")

        if eingabe == "1":
            raumHinzufuegen(smarthome)
        elif eingabe == "2":
            geraetHinzufuegen(smarthome)
        elif eingabe == "3":
            heizen(smarthome)
        elif eingabe == "4":
            lueften(smarthome)
        elif eingabe == "5":
            lichtAnAus(smarthome)
        elif eingabe == "6":
            run=beenden(smarthome)
        else:
            print("Ungültige Zahl")



def main():
    #neues Smarthome Objekt erzeugen
    smarthome = Smarthome("Smarthome",[])



    #ein paar Räume hinzufügen
    smarthome.addRoom("Wohnzimmer")
    smarthome.addRoom("Küche")
    smarthome.addRoom("Schlafzimmer")
    #Raum doppelt hinzufügen
#    smarthome.addRoom(2,"Küche")


    #Heizung hinzufügen
    smarthome.heatingcontroller.addHeater(smarthome.rooms[0])

    #Lampe und Shutter hinzufügen
    smarthome.lightingcontroller.addLamp(smarthome.rooms[0])
    smarthome.lightingcontroller.addShutter(smarthome.rooms[0])

    #Smarte Fenster hinzufügen
    smarthome.ventilationcontroller.addWindow(smarthome.rooms[0])
    smarthome.ventilationcontroller.addWindow(smarthome.rooms[0])



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
