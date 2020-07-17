from items.actuators.heating import Heating
from items.sensors.temperaturesensor import TemperatureSensor
from controllers.controller import Controller


class HeatingController(Controller):
    def __init__(self, temperatureSensor, heating,
                    desiredTemperature=21, acceptableDiff=1):
        self.temperatureSensor = temperatureSensor
        self.temperatureSensor.attach(self) # observe temperature sensor

        self.heating = heating

        self.desiredTemperature = desiredTemperature
        self.acceptableDiff = acceptableDiff

    def setDesiredTemperature(self, desiredTemperature):
        self.desiredTemperature = desiredTemperature

    def setAcceptableDiff(self, acceptableDiff):
        self.acceptableDiff = acceptableDiff

    def update(self, sensor, value):
        self.main()

    def main(self):
        # TODO: decreasing/increasing based on time since last change
        temperature = self.temperatureSensor.getValue()
        if (type(temperature) != int):
            pass
        elif (temperature < self.desiredTemperature - self.acceptableDiff):
            self.heating.increaseLevel()
        elif (temperature > self.desiredTemperature + self.acceptableDiff):
            self.heating.decreaseLevel()
