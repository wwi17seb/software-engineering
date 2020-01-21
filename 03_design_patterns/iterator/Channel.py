class Channel:
     
    # constructor of channel
    def __init__(self, name, frequenz):
        # private variables
        self.__name = name
        self.__frequenz = frequenz

    def getInformation(self):
        print ("Du hoerst " + self.__name + " auf " + self.__frequenz)

def main():
    c = Channel("ABC", "454")
    c.getInformation()
    

if __name__ == "__main__":
    import doctest
    main()
    doctest.testmod()