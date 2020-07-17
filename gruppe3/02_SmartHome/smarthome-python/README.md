# smarthome
Python implementation for lecture https://github.com/WWI17SEB/software-engineering

Abgabe ist am Morgen des 7. Februar, d.h. ich werde Freitag Morgen Github „einfrieren“.
 
Legen Sie alle während der Vorlesungsreihe erstellten Präsentationen in Github (https://github.com/WWI17SEB/software-engineering/branches ) ab. Möglichst mit Hinweisen auf korrespondierenden Code im Smart Home Beispiel. Bei der Präsentation wird bewertet, ob sie alle wesentlichen Merkmale des Entwurfsmusters dargestellt haben.
 
Vervollständigen sie das SmartHome-Beispiel so, dass die vorhandenen Klassen&Module einen sinnvollen Zusammenhang ergeben. Es geht nicht darum, ein vollständig funktionsfähiges SmartHome-System zu erstellen. Es sollte aber auf Modulebene erkennbar sein, dass sie Architektur-Entscheidungen getroffen haben. D.h. beachten Sie beim Klassendesign die SOLID-Prinzipien (möglichst über Kommentare dokumentieren) und bei der Modul/Package-Struktur** die RCC & ASS Prinzipien. Auch dies dokumentieren (z.B. in einer "Kommentar"-Datei im entsprechenden Package). Es sollte nachvollziehbar sein, wie sie ihre Design-Entscheidungen getroffen haben.
 
Praktizieren Sie TDD, nutzen sie dazu den docstring-Mechanismus (wie KW 48 Folie 26 beschrieben) und erstellen sie Test-Funktionen. Wo möglich, wenden Sie auch die SDP/SAP-Metrik (KW 48 Folien 37 ff) an. Die gesamte Funktionalität sollte über diese Test-Funktionen nutzbar sein (wie das Gruppe 2 in der Vorlesung am 23. Januar gezeigt hat).
 
Stellen sie einen Bezug zu den in ihrer Gruppe bearbeiteten Design Patterns her, indem sie zwischen ihrem Code und ihren Präsentationen Verweise angeben und zur Veranschaulichung UML-Diagramme erstellen. Das gilt natürlich auch für verwendete Design Patterns, falls sie in einer anderen Gruppe vorgestellt wurden (Bsp. Gruppe 2 nutzt Command-Pattern - was von Gruppe 1 vorgestellt wurde). Erklären sie exemplarisch an Code-Beispielen die Aspekte Kopplung und Bindung.
 
** Module sind in Python Dateien (mit der Endung .py), die Code (Klassen, Funktionen) enthalten. Packages sind in Python Verzeichnisse, die mehrere Module (Dateien) enthalten können. Erkannt wird ein Verzeichnis als Package, falls es eine Datei \_\_init\_\_.py enthält (diese wird beim Laden des Package ausgeführt), siehe https://docs.python.org/3/tutorial/modules.html

