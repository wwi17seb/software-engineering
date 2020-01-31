from TreeType import TreeType
from ITree import ITree

class Birke(ITree):
    
    def __init__(self):
        self.__color = "keine ahnung"
        self.__treeType = "BIRKE"

    def getColor(self):
        return self.__color
    
    def getTreeType(self):
        return self.__treeType
    
    def drawTree(self, x, y, height):
        # zeichnen der birke mit den extrinsischen werten bzw. daten aus dem kontext
        print("Birke wurde an Position x:{0} y:{1} mit einer Hoehe von {2}m positioniert.".format(x, y, height))