from CarRadio import CarRadio
from Channel import Channel
from ChannelIteratorNormal import ChannelIteratorNormal

def main():
    radio = CarRadio()
    radio.addChannel(Channel("Antenne Mannheim", "105,6"))
    radio.addChannel(Channel("Bayern 3", "102,1"))
    radio.addChannel(Channel("HR 3", "89,3"))
    radio.addChannel(Channel("Radio Binzen FFM", "100,0"))

    itt = radio.createIterator()

    while itt.hasNext():
        channel = itt.next()
        print(channel.getInformation())

if __name__ == "__main__":
    #import doctest
    main()
    #doctest.testmod()