from abc import ABCMeta, abstractmethod


""" Abstract Factory """

class Gadget(metaclass=ABCMeta):
    @abstractmethod
    def sellSmartPhone(self):
        pass

    @abstractmethod
    def sellSmartWatch(self):
        pass


""" Concrete Factories """

class Samsung(Gadget):
    def sellSmartPhone(self):
        return GalaxySeries()

    def sellSmartWatch(self):
        return SamsungGearSeries()

class Apple(Gadget):
    def sellSmartPhone(self):
        return IphoneSeries()

    def sellSmartWatch(self):
        return AppleWatchSeries()


""" Abstract Products """

class SmartPhone(metaclass=ABCMeta):
    @abstractmethod
    def callingGadget(self, SmartPhone):
        pass

class SmartWatch(metaclass=ABCMeta):
    @abstractmethod
    def wearableGadget(self, SmartWatch):
        pass


""" Concrete Products """

class GalaxySeries(SmartPhone):
    def callingGadget(self):
        print("Samsung Galaxy S10 Plus")

class IphoneSeries(SmartPhone):
    def callingGadget(self):
        print("Apple iPhone 11 Pro Max")

class SamsungGearSeries(SmartWatch):
    def wearableGadget(self):
        print("Samsung Galaxy Watch Active 2")

class AppleWatchSeries(SmartWatch):
    def wearableGadget(self):
        print("Apple Watch Series 5")


""" Client """

class GadgetStore:
    def __init__(self):
        pass

    def storeGadgets(self):
        for store in [Apple(), Samsung()]:
            self.store = store
            self.SmartPhone = self.store.sellSmartPhone()
            self.SmartPhone.callingGadget()
            self.SmartWatch = self.store.sellSmartWatch()
            self.SmartWatch.wearableGadget()


def main():
    account = GadgetStore()
    account.storeGadgets()


main()
