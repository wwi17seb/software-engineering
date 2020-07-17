from abc import ABC, abstractmethod 

class Controller(ABC):


    def templateMethod(self):
        self.on()
        self.off()

    def on(self):
        pass

    def off(self):
        pass


class Light_Controller(Controller):

    def on(self):
        #Licht anschalten

    def off(self):
        #Lich ausschalten

class Heating_Controller(Controller):

    def on(self):
        #Heizung anschalten

    def off(self):
        #Heizung ausschalten

class Ventilation_Controller(Controller):

    def on(self):
        #Lüftung anschalten

    def off(self):
        #Lüftung ausschalten


def main():
    controller = Controller()
    controller.templateMethod()


if __name__ == "__main__":
    main()