from device.sensor.sensor import Sensor
from device.smartDevice.smartDevice import SmartDevice


class DeviceController:

    def __init__(self, device):
        self.__device = device

    def deviceConfiguration(self):
        print("What do you want to do with your device:", self.__device.getName())
