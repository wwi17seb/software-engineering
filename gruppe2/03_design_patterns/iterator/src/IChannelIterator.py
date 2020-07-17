from abc import ABC, abstractmethod

class IChannelIterator(ABC):

    @abstractmethod
    def hasNext(self):
        pass
    @abstractmethod
    def next(self):
        pass
    
def main():
    pass

if __name__ == "__main__":
    import doctest
    main()
    doctest.testmod()