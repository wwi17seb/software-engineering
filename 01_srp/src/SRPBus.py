class Vehicle:
    def __init__(self, fuelTankSize, fuelConsumption=0.5):
        self.fuelLevel = 0
        self.fuelTankSize = fuelTankSize
        self.fuelConsumption = fuelConsumption

    def refuel(self, amount):
        self.fuelLevel = min(self.fuelTankSize, self.fuelLevel + max(0, amount))
        return self.fuelLevel

    def drive(self, distance):
        if self.fuelLevel < self.fuelConsumption * distance:
            raise ValueError('Distance is too far for current fuel level.')
        else:
            self.fuelLevel -= self.fuelConsumption * distance
            return self.fuelLevel


class SRPBus:
    def __init__(self, seats, fuelTankSize, fuelConsumption=0.5):
        self.seats = seats
        self.occupiedSeats = 0

        self.vehicle = Vehicle(fuelTankSize, fuelConsumption)

    def reserveSeats(self, numberOfSeatsToReserve=1):
        if(self.seats - self.occupiedSeats >= numberOfSeatsToReserve):
            self.occupiedSeats += numberOfSeatsToReserve
            return True
        else:
            raise ValueError('Number of seats to reserve is too high.')
