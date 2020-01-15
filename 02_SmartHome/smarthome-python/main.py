#Hier könnte man beispielhaft unterschiedliche Modules veranschaulichen

import automation, steuerzentrale, netzwerk, raum, haus
from geräte import beleuchtung, gerät, heizung, lautsprecher
from sensoren import bewegungssensor, feuermelder, schalter, sensor, temperatursensor

print("Welcome to our Smart Home")

#sample Setup
hub = steuerzentrale.Steuerzentrale()
heim = haus.Haus("HomeSweetHome", 330)
zimmer = raum.Raum ("Wohnzimmer", 2.30, heim)
wlan = netzwerk.Netzwerk("MeinNetz", "usr:pass", "settings[]")
wlan.verbindeSteuerzentrale(hub)


#example use
lampe1 = beleuchtung.Beleuchtung(zimmer, "Stehlampe", hub)
lampe1.verbinden()
lampe1.anschalten()
lampe1.ausschalten()

switch = schalter.Schalter(lampe1)
m_sensor = bewegungssensor.Bewegungssensor(lampe1)

szene = automation.Automation(m_sensor, lampe1, "an/aus")
szene.ausführen()