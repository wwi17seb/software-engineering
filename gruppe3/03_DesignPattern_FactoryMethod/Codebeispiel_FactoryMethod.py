# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABC, abstractmethod


class GeraeteFactory(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        geraet = self.factory_method()

        result = f"{geraet.operation()}"

        return result


class BeleuchtungsFactory(GeraeteFactory):
    def factory_method(self) -> Beleuchtung:
        return Beleuchtung()


class HeizungsFactory(GeraeteFactory):
    def factory_method(self) -> Heizung:
        return Heizung()


class Geraet(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Beleuchtung(Geraet):
    def operation(self) -> str:
        return "Beleuchtung"


class Heizung(Geraet):
    def operation(self) -> str:
        return "Heizung"


def client_code(geraet: GeraeteFactory) -> None:
    print(f"Used Device: {geraet.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the BeleuchtungsFactory.")
    client_code(BeleuchtungsFactory())
    print("\n")

    print("App: Launched with the HeizungsFactory.")
    client_code(HeizungsFactory())
