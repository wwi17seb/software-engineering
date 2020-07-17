class Bus:
    def __init__(self, fuelTankSize, seats, fuelConsumption=0.5):
        self.fuelTankSize = fuelTankSize
        self.fuelLevel = 0
        self.fuelConsumption = fuelConsumption
        self.seats = seats
        self.occupiedSeats = 0

    def refuel(self, amount):
        """ test fuel level with normal values
        >>> testBus = Bus(100, 10)
        >>> testBus.refuel(10)
        10
        >>> testBus.refuel(20)
        30

        test fuel level with values too high
        >>> testBus.refuel(80)
        100
        """
        self.fuelLevel = min(self.fuelTankSize, self.fuelLevel + max(0, amount))
        return self.fuelLevel

    def drive(self, distance):
        """ test fuel level after distance driven
        >>> testBus = Bus(100, 10)
        >>> testBus.refuel(10)
        10
        >>> testBus.drive(10)
        5.0
        >>> testBus.drive(10)
        0.0
        >>> testBus.drive(10)
        Traceback (most recent call last):
            ...
        ValueError: Distance is too far for current fuel level.
        """
        if self.fuelLevel < self.fuelConsumption * distance:
            raise ValueError('Distance is too far for current fuel level.')
        else:
            self.fuelLevel -= self.fuelConsumption * distance
            return self.fuelLevel

    def reserveSeats(self, numberOfSeatsToReserve=1):
        """ test reservation of seats
        >>> testBus = Bus(100, 100)
        >>> testBus.reserveSeats(10)
        True
        >>> testBus.reserveSeats(10)
        True
        >>> testBus.reserveSeats(100)
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
