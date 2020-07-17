class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name
    def makeSound(self):
        pass

class Lion(Animal):
    def makeSound(self):
        print('roar!')
        pass

class Mouse(Animal):
    def makeSound(self):
        print('squeak')
        pass

class Snake(Animal):
    def makeSound(self):
        print('hisss')

if __name__ == '__main__':
    animals = [
        Lion('lion'),
        Mouse('mouse'),
        Snake('snake')
    ]
    for animal in animals:
        animal.makeSound()
