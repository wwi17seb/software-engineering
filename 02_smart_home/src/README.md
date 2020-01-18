# Smart Home

There are three main classes/objects: sensors, actuators and controllers.
A controller reads data of all sensors it needs and then controls the actuators.

All sensors and actuators have a name and are assigned to a room.
They get instanciated in the main class and can be controlled by the CLI.

Controllers are packaged by use cases, e.g. there is one for basic operations (lights, heating, ...), one for kitchen, security (alarms), ...

**TODO**:
There needs to be a decision how to handle actuators which are normally controlled by sensors but can also be controlled directly/manually (e.g. Voice Assitant, Smartphone App).
Example: Based on the temperature sensor (22°C) the controller would decide to set heating to level 2.
The heating is set to level 4 by Voice Assistant.
How should the controller handle this situation?

**TODO**: Should there be a class `Item` from which `Sensor` and `Actuator` can inherit?