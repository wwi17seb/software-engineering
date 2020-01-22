from sensors.smokedetector import SmokeDetector
from sensors.temperaturesensor import TemperatureSensor

from actuators.firealert import FireAlert


class FireAlertController:
    def __init__(self, smokeDetector, temperatureSensor, fireAlert):
        self.smokeDetector = smokeDetector
        self.smokeDetector.attach(self) # observe smoke detector
        self.temperatureSensor = temperatureSensor
        self.temperatureSensor.attach(self) # observe temperature sensor
        self.firealert = fireAlert

    def update(self, sensor, value):
        self.main()

    def main(self):
        smokeDetectorValue = self.smokeDetector.getValue()
        temperature = self.temperatureSensor.getValue()
        if (smokeDetectorValue is True or
                (type(temperature) == int and temperature >= 50)):
            self.firealert.turnOn()
        else:
            self.firealert.turnOff()
