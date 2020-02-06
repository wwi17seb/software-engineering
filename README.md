Neben den hier aufgezählten Prinzipien sind die vorgestellten Prinzipien und Muster in den einzelnen unterordnern des Branches zu finden (bspw. 01_DIP). Hierzu wurden für die Vorträge einzelne Codebeispiele angelegt, welche nicht direkt mit dem SMART-Home Projekt in Verbindung stehen.

# Smarthome
## SOLID-Prinzipien

1. [SRP](https://github.com/WWI17SEB/software-engineering/tree/gruppe2/01_srp) (Single Responsibility Principle): Ein Klasse sollte eine Sache erledigen, und diese richtig.
- wurde von Gruppe 2 vorgestellt
- wurde im kompletten Code bei jeder Klasse verwendet

2. [OCP](https://github.com/WWI17SEB/software-engineering/tree/gruppe5/Code_Open-Closed-Principle) (Open Closed Principle): Software sollte erweiterbar sein, aber trotzdem geschlossen bleiben.
- wurde von Gruppe 5 vorgestellt
- wurde im kompletten Code bei jeder Klasse verwendet

3. [LSP](https://github.com/WWI17SEB/software-engineering/tree/gruppe4/1_Pr%C3%A4sentationen) (Loskov Substitution Principle): Unterklasse muss komplette Funktionalität der Oberklasse bedienen.
- wurde von Gruppe 4 vorgestellt
- wurde im Code verwendet (z.B. Oberklasse Sensor - Abgeleitete Klasse Temperatursensor)

4. [ISP](https://github.com/WWI17SEB/software-engineering/tree/gruppe3/01_SOLID-Prinzipien) (Interface Segregation Principle): Objekt kann mehrere Interfaces bedienen. Interfaces sollen Aufgaben erledigen und diese richtig.
- wurde von Gruppe 3 vorgestellt
- wurde im Code verwendet (Interfaces wurden für einen speziellen Fall designed)

5. [DIP](https://github.com/WWI17SEB/software-engineering/tree/gruppe1/01_DIP) (Dependency Inversion Principle): Klasse definiert Interface zur Kommunikation.
- wurde von Gruppe 1 vorgestellt(verwendet von sensor.py um die Schnittstelle der speziellen Sensoren zu definieren)

## RCC & ASS-Prinzipien
1. REP (Release Reuse Equivalency Principle)
- kann nicht verwendet werden, ist auf das spezielle Smarthome-System angepasst
- einzelne Komponenten sind nicht verwendbar ohne Anpassungen an diesen, um die Komponente in ein anderes System zu implementieren

2. CCP (Common Closure Principle)
- wurde im Code verwendet
- zusammengehörige Klassen sind in entsprechende Pakete gepackt

3. CRP (Common Reuse Principle)
- wurde im Code nicht verwendet
- nur Teile aus einem Paket werden aufgerufen

4. ADP (Acyclic Dependencies Principle)
- wurde im Code nicht verwendet
- es kann Zyklen geben (s. CLI)

5. SDP (Stable Dependencies Principle)
- wurde im Code verwendet (z.B. Temperatursensor implementiert die Sensor-Klasse --> Sensor-Klasse implementiert AbstractDevice-Klasse --> AbstractDevice-Klasse implementiert nichts)
- Pakete sollten nur von Paketen abhängen, welche stabiler sind als sie selbst

6. SAP (Stable Abstractions Principle)
- wurde im Code verwendet
- je stabiler eine Klasse, desto abstrakter sind diese (z.B. AbstractDevice-Klasse)

## Entwurfsmuster
### Erzeugungsmuster
1. Singleton
- wurde von Gruppe 5 vorgestellt
- wurde im Code verwendet (z.B. House)

### Verhaltensmuster
1. [Command](https://github.com/WWI17SEB/software-engineering/tree/gruppe1/04_Proxy_und_Command)
- wurde von Gruppe 1 vorgestellt
- wurde im Code verwendet um Routinen für die Devices zu erstellen

2. [Observer](https://github.com/WWI17SEB/software-engineering/tree/gruppe3/06_DesignPattern_Observer)
- wurde von Gruppe 3 vorgestellt
- wurde verwendet um Änderungen der Sensoren zu betrachten
- --> Sensor schickt Updates an registrierte Geräte

![Alt text](03_SmartHome/design/Metriken.svg)

## Klassendiagramm

![Alt text](03_SmartHome/design/UML_Diagramm_SmartHome.svg)

## Tests für das SMART HOME

Die Tests wurden mit Hilfe von doctest entwickelt. Damit diese funktionieren, ist es wichtig, dass [03_SmartHome/src](03_SmartHome/src) als Source-Verzeichnis im Python-Path angegeben wird, da sonst die imports der Abhängigen module nicht funktioniert und der Test Fehler aufwirft.

Weiterhin wurde eine Klasse [test.py](03_SmartHome/src/test.py) angelegt, welche die funktionalitäten des SMART-Homes darstellen soll. Sie arbeitet also nicht als Test sondern dient lediglich demonstrativen Zwecken.

## CLI
Das SMART-Home wurde als Command-Line-Anwendung geschrieben. Sie ist Nutzbar, wenn die [app.py](03_SmartHome/src/app.py) Datei im SMART-Home src Ordner ausgeführt wird. Eine Speicherung der eingebenen Daten erfolgt nicht. 
