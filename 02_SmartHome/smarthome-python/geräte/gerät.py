from abc import ABC, abstractmethod 
from gegenstand import Gegenstand

class Gerät (Gegenstand):
    
    @abstractmethod
    def aendern(self):
        pass
