from abc import ABC, abstractmethod 

class Spielfigur (ABC):
    @abstractmethod
    def Drohe(self):
        pass

class Monster (Spielfigur):
    def Drohe(self):
        print("Grrrrrrrrrr.")

class Dekorierer (Spielfigur):
    def __init__(self, spielfigur):
        self.meineFigur = spielfigur

    def Drohe(self):
        self.meineFigur.Drohe()

class HustenDekorierer (Dekorierer):
    def __init__ (self, spielfigur):
        super().__init__(spielfigur)

    def Drohe(self):
        print("Hust, hust. ")
        super().Drohe()

class SchnupfenDekorierer (Dekorierer):
    def __init__ (self, spielfigur):
        super().__init__(spielfigur)

    def Drohe(self):
        print("Schniff. ")
        super().Drohe()

if __name__ == "__main__":
    meinMonster = Monster()
    meinMonster.Drohe()
    print ("")
    
    meinVerhustetesMonster = HustenDekorierer(meinMonster)
    meinVerhustetesMonster.Drohe()
    print ("")

    meinVerschnupftesMonster = SchnupfenDekorierer(meinMonster)
    meinVerschnupftesMonster.Drohe()
    print ("")

    meinVerschnupftesVerhustetesMonster = SchnupfenDekorierer(HustenDekorierer(meinMonster))
    meinVerschnupftesVerhustetesMonster.Drohe()
    print ("")

    meinVerhustetesVerschnupftesMonster = HustenDekorierer(SchnupfenDekorierer(meinMonster))
    meinVerhustetesVerschnupftesMonster.Drohe()
    print ("")
