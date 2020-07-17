from IChannelCollection import IChannelCollection 
from Channel import Channel
from ChannelIteratorNormal import ChannelIteratorNormal 

# Aggregate
class CarRadio(IChannelCollection):
    
    # constructor of channel
    def __init__(self):
        # private variables
        self.__listChannels = [] # empty array

    def addChannel(self, Channel):
        self.__listChannels.append(Channel)

    def removeChannel(self, Channel):
        self.__listChannels.remove(Channel)

    def createIterator(self):
        return ChannelIteratorNormal(self.__listChannels)

def main():
    pass

if __name__ == "__main__":
    import doctest
    main()
    doctest.testmod()