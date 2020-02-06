# Smarthome Projekt
## Gruppe4

# Präsentation and Dokumentation

- Solid Prinzip
  - Liskov Substitution Principle ([Slides](./1_Pr%C3%A4sentationen/LSP.pdf) | Source Code in der Powerpoint)
- Smart Home ([Source Code](./2_Smarthome_Python/project) | [UML Diagramm](./UML/UML_SmartHome_Gruppe4.png))
- Design Patterns
  - Prototype Pattern ([Slides](./1_Pr%C3%A4sentationen/Prototype%20Design%20Pattern/Prototype%20Design%20Pattern.pdf) | [Source Code](./1_Pr%C3%A4sentationen/Prototype%20Design%20Pattern/Prototype.py))
  - Bridge Pattern ([Slides](./1_Pr%C3%A4sentationen/Bridge%20Pattern/Bridge%20Pattern.pdf) | [Source Code](./1_Pr%C3%A4sentationen/Bridge%20Pattern))
  - Template Method Pattern ([Slides](./1_Pr%C3%A4sentationen/Template%20Method%20Pattern/Template%20Method%20Pattern.pdf)| [Source Code](./1_Pr%C3%A4sentationen/Template%20Method%20Pattern/code_sample1.py))
  - Memento Pattern ([Slides](./1_Pr%C3%A4sentationen/Memento/_Memento.pdf) | [Source Code](./1_Pr%C3%A4sentationen/Memento/Memento.py))
- Präsentation "Making Architecture Matter" ([Slides](./1_Pr%C3%A4sentationen/Making%20Architecture%20Matter.pptx.pdf))

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
* findet hier keine Verwendung, da für unseren Anwendungsfall ersteinmal nicht durchführbar

### CCP (Common Closure Principle)
* zusammengehörige Klassen befinden sich in einzelnen Packages (z.b. Sensoren im Sensor Package oder die smarten Geräte (Heizung, Lampen, etc.) befinden sich im SmartDevices Package)

### CRP (Common Reuse Principle)
* findet hier keine Verwendung, da für unseren Anwendungsfall ersteinmal nicht durchführbarfindet keine Anwendung

### ADP (Acyclic Dependencies Principle) -> siehe Package-Metrik
* Anhand der Package Metrik lässt sich erkennen, dass keine Zyklen zwischen den Packages besteht

### SDP (Stable Dependencies Principle)
* Unsere Packets hängen nur von Packets höherer Stabilität ab (Instabilität nimmt zu)

### SAP (Stable Abstractions Principle)
* Die instabilen Packages enthalten bei uns keine Abstrackten Klassen.

![Paketstruktur mit Metriken](2_Smarthome_Python/packetmetriken.png)


# Design Patterns
## Creational patterns
* hier hat sich für unser Beispiel kein Pattern geeignet

## Structural patterns
*  hier hat sich für unser Beispiel kein Pattern geeignet

## Behavioral patterns
* Observer --> wurde genutzt um ein "heatingobservable" zu erstellen. Gibt weiter sobald die Zieltemperatur erreicht ist.
* Template Method --> Die abstrakte IConstroller Klasse bietet die Template Method (z.b. powerOn()) welche von den konkreten Controllern genutzt/implementiert wird
