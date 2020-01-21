from abc import ABC, abstractmethod

# Flyweight
class ITree(ABC):
    
    @abstractmethod
    def getColor(self):
        pass
    @abstractmethod
    def getTreeType(self):
        pass

    # extrinsischer zustand wird übergeben -> kontext!!!
    @abstractmethod
    def drawTree(self, x, y, height):
        pass