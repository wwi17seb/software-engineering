# software-engineering
# Gruppe 3


## Präsentation and Dokumentation

- Solid Prinzip
  - Interface Segregation Principle ([Slides](./01_SOLID-Prinzipien/SOLID-Prinzipien_ISP.pdf) | Source Code in der Powerpoint)
- Smart Home ([Source Code](./02_SmartHome/smarthome-python) |UML-Diagramm [Designphase](./02_SmartHome/UML-SmartHome.pdf) und  [Implementation](./02_SmartHome/smarthome-python/UML%20smarthome.pdf))
- Design Patterns
  - Factory Method ([Slides](./03_design_patterns/builder/presentations/builder.pdf) | [Source Code](./03_DesignPattern_FactoryMethod/Codebeispiel_FactoryMethod.py))
  - Decorator ([Slides](./05_DesignPattern_Decorator/Design_Pattern_Decorator.pdf) | [Source Code](./05_DesignPattern_Decorator/decorator.py))
  - Observer ([Slides](./06_DesignPattern_Observer/DesignPattern_Observer.pdf))
  - Chain of Responsibility ([Slides](./07_DesignPattern_ChainOfResponsibility/DesignPattern_ChainOfResponsibility.pdf) | [Source Code](./07_DesignPattern_ChainOfResponsibility/Codebeispiel_ChainOfResponsibility.py))
- Reverse Presentation ([Slides](./04_Making_architecture_Matter_Martin_Fowler/Making_Architecture_Matter.pdf))

## SOLID Prinzipien

### 1. Single-Responsibility-Prinzip (SRP)
- Beschreibung: Jede Klasse oder jedes Modul solltein einem Programm nur für einen einzigen Teil der Funktionalität dieses Programms verantwortlich sein 
- Vorstellung: Gruppe 2
- Verwendung: Erfüllt, besonders in Klasse raum.py (Gemäß SRP hat diese Klasse nur die Verantwortung die Raumfunktionalität zu realisieren) und Klasse netzwerk.py (Gemäß SRP hat diese Klasse nur die Verantwortung die Netzwerkfunktionalität zu realisieren) (Die aufgeführten Klassen sind Beispiele dafür, dass sie nur eine bestimmte Aufgabe absolvieren: Raum- und Netzwerkfunktionalität)

### 2. Open Closed Principle (ORP)
- Beschreibung: Erweiterbarkeit von bestehender Software
- Vorstellung: Gruppe 5
- Verwendung: Erfüllt, da fast alle Klassen erweitert und spezifiziert wurden

### 3. Loskov Substitution Principle (LSP)
- Beschreibung: Objekte einer Oberklasse durch Objekte ihrer Unterklassen ersetzt werden können, ohne die Anwendung zu zerstören
- Vorstellung: Gruppe 4
- Verwendung: Erfüllt (Beispiele: Klassen feuermelder.py, bewegungssensor.py temperatursensor.py leiten von der Oberklasse sensor.py ab; lautsprecher.pyheizung.py und heizung.py leiten von der Oberklasse geräte.py ab)

### 4. Interface Segregation Principle (ISP)
- Beschreibung: Zu große Schnittstellen werden in mehrere Schnittstellen aufgeteilt, falls implementierende Klassen unnötige Methoden haben müssen
- Vorstellung: Gruppe 3 ([unsere Slides](./01_SOLID-Prinzipien/SOLID-Prinzipien_ISP.pdf))
- Verwendung: Erstellung von Interfaces (siehe beispielsweise klasse gegenstand.py; Kennzeichnung mit abc siehe Code)


### 5. Dependency Inversion Principle (DIP)
- Beschreibung: Abhängigkeit von Modulen. Module höherer Ebenen sollten nicht von Modulen niedrigerer Ebenen abhängen
- Vorstellung: Gruppe 1
- Verwendung: Erfüllt, da Oberklassen definiert wurden und Unterklassen daraus ableiten und nicht andersrum (Siehe Beispiele in Prinzip 3)

## RCC & ASS- Prinzipien

### Release Reuse Equivalency Principle (REP)
- Beschreibung: Das Granulat der Wiederverwendung ist das Granulat der Freisetzung. Nur Komponenten, die durch ein Verfolgungssystem freigegeben werden, können effektiv wiederverwendet werden
- Verwendung: Nicht durchgeführt, da es nicht möglich war

### Common Closure Principle (CCP)
- Beschreibung: Die Klassen in einem Paket sollten gemeinsam gegen die gleichen Arten von Änderungen geschlossen werden. Eine Änderung, die ein Paket betrifft, wirkt sich auf alle Klassen in diesem Paket aus. Gemeinsames Schließen" bedeutet also eigentlich, gegen die gleichen Arten von Änderungen geschlossen zu werden
- Verwendung: Erfüllt, da die zusammengehörigen Klassen in sogennante Pakete zusammengefasst werden (z.B. PAket für Sensor, Paket für Geräte, etc.)

### Common Reuse Principle (CRP)
- Beschreibung: Beschäftigt sich mit der Verwendung von Klassen. Es besagt, dass diejenigen Klassen, welche gemeinsam verwendet werden, auch gemeinsam zu einem Modul zusammengefasst werden sollten. Durch die Einhaltung dieses Prinzips wird eine Unterteilung der Software in fachlich bzw. technisch zusammengehörende Einheiten sichergestellt
- Verwendung: Nicht durchgeführt, da nicht möglich und umsetzbar

### Acyclic Dependencies Principle (ADP)
- Beschreibung: Die Abhängigkeiten zwischen Modulen müssen zyklenfrei sein  . D. h. wenn Klassen in einem Modul von anderen Klassen in einem anderen Modul beispielsweise durch Vererbungs- oder Relationsbeziehungen abhängen, dann dürfen keine Klassen des anderen Moduls direkt oder indirekt von Klassen des ersteren Moduls abhängen
- Verwendung: Erfüllt, da keine Zyklen  im Code vorhanden sind

### Stable Dependencies Principle (SDP)
- Beschreibung: Die Abhängigkeiten zwischen Modulen sollten in Richtung der größeren Stabilität der Module gerichtet sein. Ein Modul sollte also nur von Modulen abhängig sein, welche stabiler sind als es selbst
- Verwendung: Erfüllt aufgrund der Packagestruktur. (Klasse temperatursensor.py implementiert die abstrakte Klasse sensor.py, die stabiler ist)

### Stable Abstractions Principle (SAP)
- Beschreibung: Fordert, dass die Abstraktheit eines Moduls direkt proportional zu seiner Stabilität sein muss
- Verwendung: erfüllt, da aufgrund der Klassenhierarchie die abstrakten Klassen von den 


## Erzeugungsmuster


## Verhaltensmuster


## UML-Klassendiagramm für dasProjekt Smarthome
- Beschreibung: Ein Klassendiagramm ist ein Strukturdiagramm der Unified Modeling Language zur grafischen Darstellung von Klassen, Schnittstellen sowie deren Beziehungen. Eine Klasse ist in der Objektorientierung ein abstrakter Oberbegriff für die Beschreibung der gemeinsamen Struktur und des gemeinsamen Verhaltens von Objekten.
- Verwendung: [Klassendiagramm](./02_SmartHome/smarthome-python/UML%20smarthome.pdf)

## Doctest: Test für das Smarthome-Projekt

- Beschreibung: Doctest ist ein in der Standardbibliothek der Programmiersprache Python enthaltenes Modul, das die einfache Generierung von Tests auf der Grundlage der Ausgabe der Standard-Python-Interpreter-Shell ermöglicht, die durch Ausschneiden und Einfügen in Dokstrings erstellt wird-
- Die Klassen werden einzeln durch in Textdateien ausgelagerte Testskripte getestet (Testklasse: [tests.py](/02_SmartHome/smarthome-python/tests.py)). Alle Tests kann man im Terminal mit `python tests.py -v` starten (Hierbei werden alle Tests veranschaulicht, die im Rahmen des Projekts entworfen wurden)
