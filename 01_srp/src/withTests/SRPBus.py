class Vehicle:
    def __init__(self, fuelTankSize, fuelConsumption=0.5):
        self.fuelLevel = 0
        self.fuelTankSize = fuelTankSize
        self.fuelConsumption = fuelConsumption

    def refuel(self, amount):
        """ test fuel level with normal values
        >>> testVehicle = Vehicle(100)
        >>> testVehicle.refuel(10)
        10
        >>> testVehicle.refuel(20)
        30

        test fuel level with values too high
        >>> testVehicle.refuel(80)
        100
        """
        self.fuelLevel = min(self.fuelTankSize, self.fuelLevel + max(0, amount))
        return self.fuelLevel

    def drive(self, distance):
        """ test fuel level after distance driven
        >>> testVehicle = Vehicle(100)
        >>> testVehicle.refuel(10)
        10
        >>> testVehicle.drive(10)
        5.0
        >>> testVehicle.drive(10)
        0.0
        >>> testVehicle.drive(10)
        Traceback (most recent call last):
            ...
        ValueError: Distance is too far for current fuel level.
        """
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
        """ test reservation of seats
        >>> testSRPBus = SRPBus(100, 100)
        >>> testSRPBus.reserveSeats(10)
        True
        >>> testSRPBus.reserveSeats(10)
        True
        >>> testSRPBus.reserveSeats(100)
        Traceback (most recent call last):
            ...
        ValueError: Number of seats to reserve is too high.
        """
        if(self.seats - self.occupiedSeats >= numberOfSeatsToReserve):
            self.occupiedSeats += numberOfSeatsToReserve
            return True
        else:
            raise ValueError('Number of seats to reserve is too high.')


def main():
    import doctest
    doctest.testmod()
    print('Doctests abgeschlossen.')


if __name__ == "__main__":
    main()
