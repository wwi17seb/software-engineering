import building.roomgroup as rg
import building.room as room
import building.house as house
import connection.wlan as con
import device.smartDevice.lamp as lamp


if __name__ == "__main__":
     h1 = house.House("Mannheim", "Beilstraße 7")
     rg1 = rg.RoomGroup("Erdgeschoss")
     r1 = room.Room(3, "Wohnzimmer", 25)
     c1 = con.WLAN()
     device = lamp.Lamp("Tischlampe", "Tischlampe im Wohnzimmer", 1234, "00:80:41:ae:fd:7e", [c1], 5)
     r1.addDevice(device)
     rg1.addRoom(r1)
     h1.addRoomGroup(rg1)

     device.turnOn()
     device.turnOff()

