# software-engineering
# Gruppe 3


## Präsentation and Dokumentation

- Solid Prinzip
  - Interface Segregation Principle ([Slides](./01_SOLID-Prinzipien/SOLID-Prinzipien_ISP.pdf) | Source Code in der Powerpoint)
- Smart Home ([Source Code](./02_SmartHome/smarthome-python) |[UML-Diagramm](./02_SmartHome/UML-SmartHome.pdf))
- Design Patterns
  - Factory Method ([Slides](./03_design_patterns/builder/presentations/builder.pdf) | [Source Code](./03_DesignPattern_FactoryMethod/Codebeispiel_FactoryMethod.py))
  - Decorator ([Slides](./05_DesignPattern_Decorator/Design_Pattern_Decorator.pdf) | [Source Code](./05_DesignPattern_Decorator/decorator.py))
  - Observer ([Slides](./06_DesignPattern_Observer/DesignPattern_Observer.pdf))
  - Chain of Responsibility ([Slides](./07_DesignPattern_ChainOfResponsibility/DesignPattern_ChainOfResponsibility.pdf) | [Source Code](./07_DesignPattern_ChainOfResponsibility/Codebeispiel_ChainOfResponsibility.py))
- Reverse Presentation ([Slides](./04_Making_architecture_Matter_Martin_Fowler/Making_Architecture_Matter.pdf))

## SOLID Prinzipien:

### 1. Single-Responsibility-Prinzip (SRP):
- Beschreibung: Jede Klasse oder jedes Modul solltein einem Programm nur für einen einzigen Teil der Funktionalität dieses Programms verantwortlich sein 
- Vorstellung: Gruppe 2
- Verwendung: Erfüllt, besonders in Klasse raum.py (Gemäß SRP hat diese Klasse nur die Verantwortung die Raumfunktionalität zu realisieren) und Klasse netzwerk.py (Gemäß SRP hat diese Klasse nur die Verantwortung die Netzwerkfunktionalität zu realisieren) (Die aufgeführten Klassen sind Beispiele dafür, dass sie nur eine bestimmte Aufgabe absolvieren: Raum- und Netzwerkfunktionalität)

### 2. Open Closed Principle (ORP): 
- Beschreibung: Erweiterbarkeit von bestehender Software
- Vorstellung: Gruppe 5
- Verwendung: Erfüllt, da fast alle Klassen erweitert und spezifiziert wurden

### 3. Loskov Substitution Principle (LSP):
- Beschreibung: Objekte einer Oberklasse durch Objekte ihrer Unterklassen ersetzt werden können, ohne die Anwendung zu zerstören
- Vorstellung: Gruppe 4
- Verwendung: Erfüllt (Beispiele: Klassen feuermelder.py, bewegungssensor.py temperatursensor.py leiten von der Oberklasse sensor.py ab; lautsprecher.pyheizung.py und heizung.py leiten von der Oberklasse geräte.py ab)

### 4. Interface Segregation Principle (ISP):
- Beschreibung: Zu große Schnittstellen werden in mehrere Schnittstellen aufgeteilt, falls implementierende Klassen unnötige Methoden haben müssen
- Vorstellung: Gruppe 4
- Verwendung: Erstellung von Interfaces (siehe beispielsweise klasse gegenstand.py; Kennzeichnung mit abc siehe Code)


### 5. Dependency Inversion Principle (DIP):
- Beschreibung: Abhängigkeit von Modulen. Module höherer Ebenen sollten nicht von Modulen niedrigerer Ebenen abhängen
- Vorstellung: Gruppe 1
- Verwendung: Erfüllt, da Oberklassen definiert wurden und Unterklassen daraus ableiten und nicht andersrum (Siehe Beispiele in Prinzip 3)





