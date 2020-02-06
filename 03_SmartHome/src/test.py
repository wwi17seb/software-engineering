from building.roomgroup import RoomGroup
from building.house import House
from building.room import Room
from connection.wlan import WLAN
from connection.bluetooth import Bluetooth
from device.smartDevice.lamp.lamp import Lamp
from device.smartDevice.entertainment.smartTV import SmartTV
from device.smartDevice.kitchen.oven import Oven
from device.smartDevice.kitchen.fridge import Fridge
from device.sensor.smokeSensor import SmokeSensor

if __name__ == "__main__":
    ## Create SMART HOME
    smartHome = House("Mannheim", "Coblizallee")
    groundFloor = RoomGroup("Erdgeschoss")
    firstFloor = RoomGroup("1. Etage")
    smartHome.addRoomGroup(groundFloor)
    smartHome.addRoomGroup(firstFloor)

    livingRoom = Room(3, "Wohnzimmer", 25)
    kitchen = Room(3, "Küche", 20)
    groundFloor.addRoom(livingRoom)
    groundFloor.addRoom(kitchen)

    bedRoom = Room(3, "Schlafzimmer", 25)
    firstFloor.addRoom(bedRoom)

    # Add Smart Devices
    print("Creating Smart Home....")
    btLamp = Bluetooth()
    lampLR = Lamp("LampeWZ", "Lampe Wohnzimmer", "0815", btLamp, 30)

    wlanLamp = WLAN()
    lampKitchen = Lamp("LampeK", "Lampe Küche", "083415", wlanLamp, 30)

    btLamp = Bluetooth()
    lampBed = Lamp("LampeSchlaf", "Lampe Schlafzimmer", "375220", btLamp, 30)

    livingRoom.addDevice(lampLR)
    kitchen.addDevice(lampKitchen)
    bedRoom.addDevice(lampBed)

    wlanFridge = WLAN()
    fridge = Fridge("Kühlschrank", "Kühlschrank", "0980", wlanFridge, 5)

    wlanOven = WLAN()
    oven = Oven("Ofen", "Ofen in der Küche", "666.666", wlanOven, 250)
    oven.setTemperature(200)
    oven.setTimer(30)

    btSensor = Bluetooth()
    smokeSensor = SmokeSensor("Rauchsensor", "Rauchsensor Küche", "1111", btSensor, 1, None)

    kitchen.addDevice(fridge)
    kitchen.addDevice(oven)

    wlanTV = WLAN()
    tv = SmartTV("Fernseher", "Fernseher Wohnzimmer", "448373", wlanTV)
    livingRoom.addDevice(tv)

    import time
    time.sleep(5)

    # Activate devices
    print("#######################################")
    print("ACTIVATE DEVICES")
    for rg in smartHome.getRoomGroups():
        for r in rg.getRooms():
            for d in r.getDevices():
                d.turnOn()
                time.sleep(3)
    print("#######################################")

    # Register Device to Sensor
    print("Register oven to smoke sensor")
    smokeSensor.register(oven, oven.update)
    smokeSensor.measure()
    print("Dispatch sensor information....")
    time.sleep(3)
    smokeSensor.dispatch()

    # Deregister Device from Sensor
    print("Unregister oven to smoke sensor")
    smokeSensor.unregister(oven)
    time.sleep(1)
    print("#######################################")
    print("DEACTIVATE DEVICES")
    for rg in smartHome.getRoomGroups():
        for r in rg.getRooms():
            for d in r.getDevices():
                d.turnOff()
                time.sleep(3)
    print("#######################################")


