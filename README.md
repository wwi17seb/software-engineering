# Smarthome Projekt
This repository is made to implement some classes for a simple smarthome system.

# SOLID - Prinzipien
### SRP (Single Responsibility Principle)
* konkrete Klassen haben nur eine spezielle Aufgabe z.B. heatingcontroller steuert einzig und allein die Heizung. Prinzip erfüllt.
### OCP (Open Closed Principle)
* Implementierung der Klassen von abstrakt zu immer spezifischer ist gegeben. Damit ist das Prinzip erfüllt.
### LSP (Liskov Substitution Principle)
* jede Subklasse besitzt alle Methoden der zugehörigen Superklasse damit ist das LSP erfüllt.
### ISP (Interface Segregation Principle)
* Um dieses Prinzip zu erfüllen wurde das itarget Interface erstellt. Dies wird benötigt, da der Licht Lichtsensor keinen Zielwert benötigt
### DIP (Dependency Inversion Principle)
* durch smarthome als input für Konstruktor wird möglicherweise gegen DIP verstoßen, hier im Kontext jedoch zu missachten, da raum nicht unabhängig vom Smarthome existieren sollte

# RCC & ASS - Prinzipien
### REP (Release Reuse Equivalency Principle)
* TODO

### CCP (Common Closure Principle)
* TODO

### CRP (Common Reuse Principle)
* TODO

### ADP (Acyclic Dependencies Principle)
* Anhand der Package Metrik lässt sich erkennen, dass keine Zyklen zwischen den Packages besteht

### SDP (Stable Dependencies Principle)
* TODO

### SAP (Stable Abstractions Principle)
* TODO


# Design Patterns
## Creational patterns
* hier hat sich für unser Beispiel kein Pattern geeignet

## Structural patterns
* 

## Behavioral patterns
* Observer --> wurde genutzt um ein "heatingobservable" zu erstellen. Gibt weiter sobald die Zieltemperatur erreicht ist.
* Template Method --> Der Controller ist hierbei der abstrakte "worker" und alle spezifischen Controller greifen auf ihn zu.
