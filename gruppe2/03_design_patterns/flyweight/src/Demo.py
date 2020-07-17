from TreeFactory import TreeFactory
from TreeType import TreeType

def main():
    treeFactory = TreeFactory()

    tree1 = treeFactory.getTree("TANNE")
    tree1.drawTree(10, 10, 30)

    tree2 = treeFactory.getTree("TANNE")
    tree2.drawTree(5, 5, 20)
    
    tree3 = treeFactory.getTree("BIRKE")
    tree3.drawTree(2, 2, 22)

    tree4 = treeFactory.getTree("TANNE")
    tree4.drawTree(3, 4, 5)

    tree5 = treeFactory.getTree("TANNE")
    tree5.drawTree(70, 60, 45)


if __name__ == "__main__":
    #import doctest
    main()
    #doctest.testmod()