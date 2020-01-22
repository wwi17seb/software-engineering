from actuators.heating import Heating
from sensors.temperaturesensor import TemperatureSensor
from controllers.controller import Controller


class HeatingController(Controller):
    def __init__(self, temperatureSensor, heating, desiredTemperature=21):
        self.temperatureSensor = temperatureSensor
        self.temperatureSensor.attach(self) # observe temperature sensor

        self.heating = heating

        self.desiredTemperature = desiredTemperature

    def setDesiredTemperature(self, desiredTemperature):
        self.desiredTemperature = desiredTemperature

    def update(self, sensor, value):
        self.main()

    def main(self):
        temperature = self.temperatureSensor.getValue()
        if (type(temperature) != int):
            pass
        elif (temperature < self.desiredTemperature - 1):
            self.heating.increaseLevel()
        elif (temperature > self.desiredTemperature + 1):
            self.heating.decreaseLevel()
