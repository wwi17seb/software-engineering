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
            print("Here is what I can do:")
            print("- heat oven to ...")
            print("- switch kitchen lights off")
        elif (voiceInput.lower().startswith("heat oven to")):
            # TODO: split string etc.
            pass
        elif (voiceInput.lower() == "switch kitchen lights off"):
            for itemName in self.smartHome.getAllItemNames():
                currentItem = self.smartHome.getItemByName(itemName)
                if(isinstance(currentItem, rgblight.RGBLight) or
                   isinstance(currentItem, whitelight.WhiteLight)):
                    currentItem.turnOff()
        else:
            print("I can't do this yet.")
            print("Here is what I can do:")
            print("- heat oven to ...")
            print("- switch kitchen lights off")

        self.microphone.clear()
