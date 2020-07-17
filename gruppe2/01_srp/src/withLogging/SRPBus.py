import logging

# create logger with 'log_everything'
logger = logging.getLogger('log_everything')
logger.setLevel(logging.DEBUG)
# create file handler
fh = logging.FileHandler('spam.log')
# log even debug messages
fh.setLevel(logging.DEBUG)
# create console handler
ch = logging.StreamHandler()
# log even debug messages
ch.setLevel(logging.DEBUG)
# create and set formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


class Vehicle:
    def __init__(self, fuelTankSize, fuelConsumption=0.5):
        self.fuelLevel = 0
        self.fuelTankSize = fuelTankSize
        self.fuelConsumption = fuelConsumption

        logger.info('created an instance of vehicle with the values: fuelLevel: ' + str(self.fuelLevel) + ', fuelTankSize: ' + str(self.fuelTankSize) +
                    ' and fuelConsumption: ' + str(self.fuelConsumption) + '.')

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

        logger.info('refueled vehicle. amount: ' + str(min(self.fuelTankSize - self.fuelLevel, max(0, amount))) + '.')

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
            logger.warning('could not travel distance. distance was ' + str(distance) + ' while max. was ' + str(self.fuelLevel / self.fuelConsumption) + '.')

            raise ValueError('Distance is too far for current fuel level.')
        else:
            logger.info('drove distance of ' + str(distance) + '.')

            self.fuelLevel -= self.fuelConsumption * distance
            return self.fuelLevel


class SRPBus:
    def __init__(self, seats, fuelTankSize, fuelConsumption=0.5):
        self.seats = seats
        self.occupiedSeats = 0

        self.vehicle = Vehicle(fuelTankSize, fuelConsumption)

        logger.info('created an instance of SRPBus with the values: seats: ' + str(self.seats) + ' and occupiedSeats: ' + str(self.occupiedSeats) + '.')

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
            logger.info('reserved ' + str(numberOfSeatsToReserve) + ' seats.')

            self.occupiedSeats += numberOfSeatsToReserve
            return True
        else:
            logger.warning(
                'could not travel reserve seats. number of seats to reserve was ' + str(numberOfSeatsToReserve) + ' while max. available seats were ' +
                str(self.seats - self.occupiedSeats) + '.')

            raise ValueError('Number of seats to reserve is too high.')


def main():
    import doctest
    doctest.testmod()
    print('Doctests finished.')


if __name__ == "__main__":
    main()
