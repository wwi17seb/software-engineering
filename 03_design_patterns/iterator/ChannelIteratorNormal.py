from IChannelIterator import IChannelIterator

# ConcreteAggregate
class ChannelIteratorNormal(IChannelIterator):
    
    # constructor of ChannelIteratorNormal
    def __init__(self, channels):
        # private variables
        self.__listChannels = channels
        self.__currentPosition  = 0

    # has list of chanel has a next object
    def hasNext(self):
        return self.__currentPosition < len(self.__listChannels)
    
    # get channel at current position
    def next(self):
        nextChannel = self.__listChannels[self.__currentPosition]
        self.__currentPosition += 1
        return nextChannel

def main():
    pass
    

if __name__ == "__main__":
    import doctest
    main()
    doctest.testmod()