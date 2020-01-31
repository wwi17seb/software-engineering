from Channel import Channel
from abc import ABC, abstractmethod

class IChannelCollection(ABC):
    @abstractmethod
    def addChannel(self):
        pass
    @abstractmethod
    def removeChannel(self):
        pass
    @abstractmethod
    def createIterator(self):
        pass

def main(): 
    pass 

if __name__ == "__main__":
    import doctest
    main()
    doctest.testmod()