from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from string import ascii_letters, digits

#Der Originator kann in unserem Fall das Heizungssystem sein
class HeatSystem():
    _state = None
    #Der einfachheit nehmen wir an es gibt nur dieses eine Attribut

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Heatsystem: Mein Startzustand ist: {self._state}")

    def change(self, state: str) -> None:
        #Umstellen der Heizung
        print("Heatsystem: Heizung wird umgestellt")
        self._state = state
        print(f"Heatsystem: Folgende Einstellung wurde vorgenommen: {self._state}")

    def save(self) -> ConcreteMemento:
        #Speichern der Einstellung in ein Memento --> wird vom Caretaker gebraucht
        return ConcreteMemento(self._state)

    def restore(self, memento: ConcreteMemento) -> None:
        #Hiermit lässt sich der Memento wiederherstellen
        self._state = memento.get_state()
        print(f"Heatsystem: Folgende Einstellung wurde wiederhergestellt: {self._state}")



class ConcreteMemento:
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        #Dies braucht der Originator um seinen alten Status wiederherzustellen
        return self._state

    def get_name(self) -> str:
       #nutzbar vom Caretaker für eine bessere Ansicht
        return f"{self._date} / ({self._state[0:9]}...)"
    
    def get_date(self) -> str:
        #nutzbar vom Caretaker für eine bessere Ansicht
        return self._date


class Caretaker():
    #Hier lässt sich die Historie der Veränderungen darstellen
    def __init__(self, originator: HeatSystem) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        #Hier speichert der Caretaker ein Memento vom Originator
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        #Der letzte Memento im Stack wird wiederhergestellt 
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        #Auflisten der Historie
        print("Caretaker: Hier sind alle deine Einstellungen:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = HeatSystem("Standard")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.change("Kalt draußen")

    caretaker.backup()
    originator.change("Urlaub")

    print()
    caretaker.show_history()

    print("\nIch will den alten Zustand zurück!\n")
    caretaker.undo()

    print("\nNoch einen weiter\n")
    caretaker.undo()