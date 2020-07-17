# Implementierung einer Factory Klasse für Geräte

from __future__ import annotations
from abc import ABC, abstractmethod
from geräte import beleuchtung, gerät, heizung, lautsprecher
import raum

class GeraeteFactory(ABC):

    @abstractmethod
    def factory_method(self):
        pass
    
    @staticmethod
    def BeleuchtungsFactory(**kwargs) -> beleuchtung.Beleuchtung:
        try:
            return beleuchtung.Beleuchtung(**kwargs)
        except Exception:
            return None
    
    @staticmethod       
    def HeizungsFactory(**kwargs) -> heizung.Heizung:
        try:
            return heizung.Heizung(**kwargs)
        except Exception:
            return None
    
    @staticmethod
    def LautsprecherFactory(**kwargs) -> lautsprecher.Lautsprecher:
        try:
            return lautsprecher.Lautsprecher(**kwargs)
        except Exception:
            return None