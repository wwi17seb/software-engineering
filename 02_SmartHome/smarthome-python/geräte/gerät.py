from abc import ABC, abstractmethod 
from gegenstand import Gegenstand

# Es wurd besonders darauf geachtet, dass unsere Softwarearchitektur
# nach Funktionalität sinnvoll in Pakete eingeteilt wird.
# Aus diesem Grund sind nun alle Bestandteile des Smarthomes, welche
# eine Gerät darstellen, in dem Paket "geräte".

class Gerät (Gegenstand):
    
    @abstractmethod
    def setState(self):
        pass
