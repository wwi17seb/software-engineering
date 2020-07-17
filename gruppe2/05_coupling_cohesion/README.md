# Coupling and Cohesion

## Coupling
The goal is to achieve low coupling between modules.
This means that a module which depends on another should only depend on the interface and not on some internal parts of the other module.

Bad Example:
Another class depends on the concrete implementation and changes data of another class/object directly.
```python
# car.py

class Car:
    def __init__(self):
        self.curSpeed = 0
    
    def accelerate(self):
        self.curSpeed += 1
    
    def brake(self):
        self.curSpeed -= 1
```

```python
# main.py
from car import Car

car = Car()
maxSpeed = 100

# accelerate to maximum speed
while(car.curSpeed < maxSpeed):
    car.accelerate()

# slow down to a standstill
while(car.curSpeed > 0):
    car.brake()

# reverse gear
while(abs(car.curSpeed) < maxSpeed//3):
    car.curSpeed -= 1

# brake abruptly
car.curSpeed = 0
```

Good Example:
Interface to write logs, just need to specify necessary parameters.
```python
# log.py
from datetime import datetime

STATUS_ERROR = "ERROR"
STATUS_INFO = "INFO"
class Logger:
    def __init__(self):
        self.formatStr = "{date}: {status} - {message}"
    
    def __writeLog(self, status, message):
        print(self.formatStr.format(date=datetime.now(),
                                    status=status,
                                    message=message))
    
    def writeErrorLog(self, message):
        self.__writeLog(STATUS_ERROR, message)
    
    def writeInfoLog(self, message):
        self.__writeLog(STATUS_INFO, message)
```
When this is used somewhere the implementation details can change (e.g. writing logs to file instead of console or change the format of logs) without clients need to know because they only depend on the interface.
Because of that it is easier to change something in future.
Only if the interface changes, clients need to be updated.

## Cohesion
The goal is to achieve a strong cohesion inside a module/package.
This regards the dependencies inside the module/package and says whether the parts fit together (or how well they do).

Bad Example:
Putting several different helper-functions inside a module without any similarities between them
```python
# helper.py

class Helper:
    @staticmethod
    def convertDegreesFahrenheitToCelsius(cls, degrees):
        pass

    @staticmethod
    def writeLogToFile(filename, logMessage):
        pass

    @staticmethod
    def reverseArray(array):
        pass

    @staticmethod
    def printTableToConsole(array):
        pass
```

Good Example:
Module with sensors which belong together because they are all sensors and share main parts (Logic Cohesion).
```python
# sensors.py

class Sensor:
    pass

class Sensor1(Sensor):
    pass

class Sensor2(Sensor):
    pass
```
