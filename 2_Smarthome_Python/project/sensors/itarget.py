from abc import ABC, abstractmethod

# zur erfüllung des ISP notwendig, da Lichtsensor keinen Zielwert benötigt
class ITarget(ABC):
    def __init__(self):
        self.target=0

    def setTarget(self,target):
        self.target=target