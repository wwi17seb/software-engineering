# Director
class HouseDirector:
    def __init__(self):
        self.house = None

    def construct(self, builder):
        self.builder = builder
        self.builder.buildWall()
        self.builder.buildDoor()

# Abstract Builder
class Builder:
    def __init__(self):
        self.house = House()

    def buildWall(self):
        raise Exception("Abstract Class: Please Implement!")

    def buildDoor(self):
        raise Exception("Abstract Class: Please Implement!")

# Concrete Builder
class WoodHouseBuilder(Builder):
    def buildWall(self):
        pass # building wooden walls

    def buildDoor(self):
        pass # inserting a wooden door

# Product
class House:
    def __init__(self):
        pass

def main():
    concreteBuilder = WoodHouseBuilder()
    director = HouseDirector()
    director.construct(concreteBuilder)
    product = concreteBuilder.house

if __name__ == "__main__":
    main()
