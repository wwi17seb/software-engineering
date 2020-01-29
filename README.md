# software-engineering
## SOLID-Prinzipien
1. SRP (Single Responsibility Principle): Ein Klasse sollte eine Sache erledigen, und diese richtig.
- wurde von Gruppe 2 vorgestellt
- wurde im kompletten Code bei jeder Klasse verwendet

2. OCP (Open Closed Principle): Software sollte erweiterbar sein, aber trotzdem geschlossen bleiben.
- wurde von Gruppe 5 vorgestellt
- wurde im kompletten Code bei jeder Klasse verwendet

3. LSP (Loskov Substitution Principle): Unterklasse muss komplette Funktionalität der Oberklasse bedienen.
- wurde von Gruppe 4 vorgestellt
- wurde im Code verwendet (z.B. Oberklasse Sensor - Abgeleitete Klasse Temperatursensor)

4. ISP (Interface Segregation Principle): Objekt kann mehrere Interfaces bedienen. Interfaces sollen Aufgaben erledigen und diese richtig.
- wurde von Gruppe 3 vorgestellt
- wurde im Code verwendet (Interfaces wurden für einen speziellen Fall designed)

5. DIP (Dependency Inversion Principle): Klasse definiert Interface zur Kommunikation.
- wurde von Gruppe 1 vorgestellt
- ???

## RCC & ASS-Prinzipien
1. REP (Release Reuse Equivalency Principle)
- ???

2. CCP (Common Closure Principle)
- wurde im Code verwendet

3. CRP (Common Reuse Principle)
- wurde im Code nicht verwendet

4. ADP (Acyclic Dependencies Principle)
- wurde im Code nicht verwendet

5. SDP (Stable Dependencies Principle)
- wurde im Code verwendet (z.B. Temperatursensor implementiert die Sensor-Klasse ---> Sensor-Klasse implementiert AbstractDevice-Klasse --> AbstractDevice-Klasse implementiert nichts)

6. SAP (Stable Abstractions Principle)
- wurde im Code verwendet (z.B. AbstractDevice-Klasse)

## Entwurfsmuster
### Erzeugungsmuster
1. Abstract Factory
- wurde von Gruppe 1 vorgestellt

2. Builder
- wurde von Gruppe 2 vorgestellt

3. Factory Method
- wurde von Gruppe 3 vorgestellt

4. Prototype
- wurde von Gruppe 4 vorgestellt

5. Singleton
- wurde von Gruppe 5 vorgestellt
- wurde im Code verwendet (z.B. House)

### Strukturmuster
1. Bridge 
- wurde von Gruppe 4 vorgestellt

2. Decorator 
- wurde von Gruppe 3 vorgestellt

3. Flyweight
- wurde von Gruppe 2 vorgestellt

4. Proxy
- wurde von Gruppe 1 vorgestellt

### Verhaltensmuster
1. Chain of Responsibility
- wurde von Gruppe 3 vorgestellt

2. Command
- wurde von Gruppe 1 vorgestellt

3. Iterator
- wurde von Gruppe 2 vorgestellt

4. Memento
- wurde von Gruppe 4 vorgestellt

5. Observer
- wurde von Gruppe 3 vorgestellt

6. State
- wurde von Gruppe 2 vorgestellt

7. Template Method
- wurde von Gruppe 4 vorgestellt

8. Visitor
- wurde von Gruppe 1 vorgestellt
