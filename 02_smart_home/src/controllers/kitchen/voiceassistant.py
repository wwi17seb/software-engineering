from actuators import *
from sensors import *


class VoiceAssistant:
    def __init__(self, microphone, smartHome):
        self.microphone = microphone
        self.smartHome = smartHome

    def main(self):
        voiceInput = self.microphone.getValue()
        if (voiceInput is None):
            pass
        elif (voiceInput == ""):
            print("Yes..?")
        elif (voiceInput.lower() == "what can you do"):
            self.printListOfAvailableCommands()
        elif (voiceInput.lower().startswith("heat oven to")):
            temperature = voiceInput[len("heat oven to "):].split()[0]
            if (temperature.isdigit()):
                temperature = int(temperature)
                oven = self.smartHome.getItemByName("okitchen1")
                oven.setTemp(temperature)
                if (temperature > oven.maxTemp):
                    print("Oh honey, how often did I tell you that the oven can only reach " +
                          str(oven.maxTemp) + " " + str(oven.unit) + "?")
            else:
                print(
                    "I don't know what you mean, I can't heat the oven to", temperature)
        elif (voiceInput.lower() == "switch kitchen lights off"):
            for itemName in self.smartHome.getAllItemNames():
                currentItem = self.smartHome.getItemByName(itemName)
                if(currentItem.room == self.smartHome.kitchen and
                   (isinstance(currentItem, rgblight.RGBLight) or
                        isinstance(currentItem, whitelight.WhiteLight))):
                    currentItem.turnOff()
        else:
            print("I can't do this yet.")
            self.printListOfAvailableCommands()

        self.microphone.clear()

    def printListOfAvailableCommands(self):
        print("Here is what I can do:")
        print("- heat oven to ...")
        print("- switch kitchen lights off")
