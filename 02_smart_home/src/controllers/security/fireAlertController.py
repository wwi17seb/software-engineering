from sensors.smokedetector import SmokeDetector
from sensors.temperaturesensor import TemperatureSensor

from actuators.firealert import FireAlert


class FireAlertController:
    def __init__(self, smokeDetector, temperatureSensor, fireAlert):
        self.smokeDetector = smokeDetector
        self.temperatureSensor = temperatureSensor
        self.firealert = fireAlert

    def main(self):
        smokeDetectorValue = self.smokeDetector.getValue()
        temperature = self.temperatureSensor.getValue()
        if (smokeDetectorValue is True or temperature >= 50):
            self.firealert.turnOn()
        else:
            self.firealert.turnOff()
