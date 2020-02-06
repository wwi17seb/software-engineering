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
1. Single-Responsibility-Prinzip:
- Beschreibung: Jede Klasse oder jedes Modul solltein einem Programm nur für einen einzigen Teil der Funktionalität dieses Programms verantwortlich sein 
- Vorstellung: Gruppe 2
- Verwendung: Durchgängig, besonder in Klasse raum.py (Gemäß SRP hat diese Klasse nur die Verantwortung die Raumfunktionalität zu realisieren) und Klasse netzwerk.py (Gemäß SRP hat diese Klasse nur die Verantwortung die Netzwerkfunktionalität zu realisieren)
