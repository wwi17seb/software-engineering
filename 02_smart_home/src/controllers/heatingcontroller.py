from actuators.heating import Heating
from sensors.temperaturesensor import TemperatureSensor


class HeatingController:
    def __init__(self, temperatureSensor, heating):
        self.temperatureSensor = temperatureSensor
        self.heating = heating

    def main(self):
        temperature = self.temperatureSensor.getValue()
        if (type(temperature) != int):
            pass
        elif (temperature < 16):
            self.heating.setToMaxLevel()
        elif (temperature < 20):
            self.heating.increaseLevel()
        elif (temperature > 27):
            self.heating.turnOff()
        elif (temperature > 24):
            self.heating.decreaseLevel()
