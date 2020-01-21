from TreeType import TreeType
from ITree import ITree

# ConcreteFlyweight
class Tanne(ITree):
    
    def __init__(self):
        self.__color = "grün"
        self.__treeType = "TANNE"

    def getColor(self):
        return self.__color
    
    def getTreeType(self):
        return self.__treeType
    
    def drawTree(self, x, y, height):
        # zeichnen der tanne mit den extrinsischen werten bzw. daten aus dem kontext
        # https://stackoverflow.com/questions/52225721/typeerror-can-only-concatenate-str-not-int-to-str-simple-python-programme
        print("Tanne wurde an Position x:{0} y:{1} mit einer Hoehe von {2}m positioniert.".format(x, y, height))