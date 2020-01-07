class Bus:
    def __init__(self, fuelTankSize, seats, fuelConsumption=0.5):
        self.fuelTankSize = fuelTankSize
        self.fuelLevel = 0
        self.fuelConsumption = fuelConsumption
        self.seats = seats
        self.occupiedSeats = 0

    def refuel(self, amount):
        self.fuelLevel = min(self.fuelTankSize, self.fuelLevel + max(0, amount))
        return self.fuelLevel

    def drive(self, distance):
        if self.fuelLevel < self.fuelConsumption * distance:
            raise ValueError('Distance is too far for current fuel level.')
        else:
            self.fuelLevel -= self.fuelConsumption * distance
            return self.fuelLevel

    def reserveSeats(self, numberOfSeatsToReserve=1):
        if(self.seats - self.occupiedSeats >= numberOfSeatsToReserve):
            self.occupiedSeats += numberOfSeatsToReserve
            return True
        else:
            raise ValueError('Number of seats to reserve is too high.')
