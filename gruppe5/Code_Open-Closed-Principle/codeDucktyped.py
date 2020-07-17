class Lion():
    def makeSound(self):
        print('roar!')
        pass
    def hunt(self):
        print('the Lions hunts food')

class Mouse():
    def makeSound(self):
        print('squeak')
        pass

class Snake():
    def makeSound(self):
        print('hisss')
    def hunt(self):
        print('the Snake hunts food')



animals = [
    Lion(),
    Mouse(),
    Snake()
]

if __name__ == '__main__':
    for animal in animals:
        animal.makeSound()
    for animal in animals:
        animal.hunt()
