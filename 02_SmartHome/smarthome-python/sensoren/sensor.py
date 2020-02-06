import abc
from gegenstand import Gegenstand 

# Es wurd besonders darauf geachtet, dass unsere Softwarearchitektur
# nach Funktionalität sinnvoll in Pakete eingeteilt wird.
# Aus diesem Grund sind nun alle Bestandteile des Smarthomes, welche
# einen Sensor darstellen, in dem Paket "sensoren".

class Sensor(Gegenstand):
    def __init__(self, gerät, raum, name, steuerzentrale, data = None):
        # Konstruktor
        # Ein Sensor kann an ein Gerät gebunden sein, aus diesem Grund
        # kann hier über den Konstruktor die betreffende Instanz des 
        # Gerätes referenziert werden. Hier wird auch das 
        # Dependency-Inversion-Prinzip insoweit eingehalten, dass sich 
        # "Sensor" und "Gerät" auf der selben Ebene befinden
        super().__init__(raum, name, steuerzentrale, data = None)
        self.connectedDevice = gerät
        self.data = data

    # bei der Methode "messen" kann besonders gut die 
    # Realisierung des Interface-Segregation-Prinzip
    # verdeutlicht werden, denn der Sensor enthält nur
    # methoden, welche durch alle davon abgeleiteten 
    # Sensoren benötigt werden
    # ------- zur Funktionalität --------------------------
    # Diese Methode benötigt noch keine Funktionalität, da diese 
    # Methode abstract ist und die Funktionalität durch die ab-
    # geleiteten Klassen bestimmt wird.
    @abc.abstractmethod
    def messen(self):
        pass
    
    # diese muss keine abstracte Methode sein, denn es wird
    # keine erweiterung der Funktionalität erzwungen
    # ------- zur Funktionalität --------------------------
    # Diese Methode enthält keine weiterführende Funktionalität, sondern 
    # den Grungedanken veranschaulichen: Hier wird eine Automation
    # zugeordnet, die beim auslösen des Sensors ausgeführt werden soll.
    def automationZuordnen(self, automation):
        self.automation = automation