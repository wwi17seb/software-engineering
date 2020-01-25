import copy

class Prototype:

   _type = None
   _sound = None

   def clone(self):
      pass

   def getType(self):
      return self._type

   def getSound(self):
      return self._sound

# konkrete Subklasse Schaf
class Schaf(Prototype):

   def __init__(self, sound):
      self._type = "Schaf"
      self._sound = sound

   def clone(self):
      return copy.copy(self)

# konkrete Subklasse Hund
class Hund(Prototype):

   def __init__(self, sound):
      self._type = "Hund"
      self._sound = sound

   def clone(self):
      return copy.copy(self)

# hier wird der Prototyp initialisiert und die Instanzen der Klassen des Prototyps instanziiert
class ObjectFactory:

   __schafSound1 = None
   __schafSound2 = None
   __hundSound1 = None
   __hundSound2 = None

   @staticmethod
   def initialize():
      ObjectFactory.__schafSound1 = Schaf("Mäh")
      ObjectFactory.__schafSound2 = Schaf("Möhh")
      ObjectFactory.__hundSound1 = Hund("Wau")
      ObjectFactory.__hundSound2 = Hund("Wuff")

   @staticmethod
   def getSchafSound1():
      return ObjectFactory.__schafSound1.clone()

   @staticmethod
   def getSchafSound2():
      return ObjectFactory.__schafSound2.clone()

   @staticmethod
   def getHundSound1():
      return ObjectFactory.__hundSound1.clone()

   @staticmethod
   def getHundSound2():
      return ObjectFactory.__hundSound2.clone()

def main():
   ObjectFactory.initialize()

   instance = ObjectFactory.getSchafSound1()
   print(instance.getType(), ": ", instance.getSound())

   instance = ObjectFactory.getSchafSound2()
   print(instance.getType(), ": ", instance.getSound())

   instance = ObjectFactory.getHundSound1()
   print(instance.getType(), ": ", instance.getSound())

   instance = ObjectFactory.getHundSound2()
   print(instance.getType(), ": ", instance.getSound())

if __name__ == "__main__":
   main()
