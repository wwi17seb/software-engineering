from Birke import Birke
from Tanne import Tanne
from TreeType import TreeType

#Flyweight-Factory
class TreeFactory:
    
    def __init__(self):
        self.__listOfTrees = []

    def getTree(self, treeType):
        treeExists = False
        counter = -1
        typeToCompare = None
        if treeType == "BIRKE":
            typeToCompare = Birke
        elif treeType == "TANNE":
            typeToCompare = Tanne

        for i in self.__listOfTrees:
            if isinstance(i, Birke):
                print("is Birke")
            elif isinstance(i, Tanne):
                print("is Tanne")
            if isinstance(i, typeToCompare):
                treeExists = True
                counter += 1

        if (not treeExists):
            print("tree from type " + treeType + " does not exists")
            tree = None
            if treeType == "TANNE":
                print("Tanne wurde erstellt!")
                tree = Tanne()
            elif treeType == "BIRKE":
                print("Birke wurde erstellt!")
                tree = Birke()
            else:
                raise NotImplementedError

            print("Tree of type " + treeType + " added to array")
            self.__listOfTrees.append(tree)
            return tree
        else: 
            print('in else')
            return self.__listOfTrees[counter]
            
    # https://www.programiz.com/python-programming/methods/built-in/isinstance
    # https://www.journaldev.com/18722/python-static-method
    # create getTree static method