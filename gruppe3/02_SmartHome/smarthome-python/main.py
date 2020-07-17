#Hier könnte man beispielhaft unterschiedliche Modules veranschaulichen

import automation, steuerzentrale, netzwerk, raum, haus
from geräte import beleuchtung, gerät, heizung, lautsprecher
from sensoren import bewegungssensor, feuermelder, schalter, sensor, temperatursensor
from geräte.GeräteFactory import GeraeteFactory
from decorator import SiriDekorierer, AlexaDekorierer, GoogleDekorierer
print("Welcome to our Smart Home")

#sample Setup
hub = steuerzentrale.Steuerzentrale()
heim = haus.Haus("HomeSweetHome", 330)
zimmer = raum.Raum ("Wohnzimmer", 2.30, heim)
wlan = netzwerk.Netzwerk("MeinNetz", "usr:pass", "settings[]")
wlan.verbindeSteuerzentrale(hub)


#example use
lampe1 = beleuchtung.Beleuchtung(zimmer, "Stehlampe", hub)
lampe1 = AlexaDekorierer(SiriDekorierer(lampe1)) #make it alexa and siri compatible
lampe2 = GeraeteFactory.BeleuchtungsFactory(raum=zimmer, name="Deckenlampe",steuerzentrale=hub)
lampe2 = GoogleDekorierer(lampe2)
lampe1.verbinden()
lampe2.verbinden()
lampe1.smartAssistant()
lampe2.smartAssistant()
lampe1.anschalten()
lampe2.anschalten()
lampe1.ausschalten()
lampe2.ausschalten()

switch = schalter.Schalter(lampe1, "Switch")
m_sensor = bewegungssensor.Bewegungssensor(lampe1, lampe1.standort, "Motion Sensor", lampe1.steuerzentrale)

szene = automation.Automation(m_sensor, lampe1, "an/aus")
szene.ausführen()