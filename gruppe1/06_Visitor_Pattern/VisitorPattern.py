import abc

"""ABSTRAKTES ELEMENT"""
class Hausbewohner(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def accept(self, visitor):
        pass


"""KONKRETES ELEMENT"""
class Vater(Hausbewohner):

    def accept(self, visitor):
        visitor.visit_vater(self)

"""KONKRETES ELEMENT"""
class Sohn(Hausbewohner):

    def accept(self, visitor):
        visitor.visit_sohn(self)

"""VISITOR"""
class VisitorAlexa(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def visit_vater(self, Vater):
        pass

    @abc.abstractmethod
    def visit_sohn(self, Sohn):
        pass


"""CONCRETE VISITOR"""
class VisitorAlexaMusik(VisitorAlexa):

    def visit_vater(self, Vater):
        print("Spiele Songs aus den 80ern...")

    def visit_sohn(self, Sohn):
        print("Spiele Deutschrap...")


"""CONCRETE VISITOR"""
class VisitorAlexaBestellen(VisitorAlexa):

    def visit_vater(self, Vater):
        print("Bestelle Warenkorb mit Amazon Account von: Vater.")

    def visit_sohn(self, Sohn):
        print("Bestelle Warenkorb mit Amazon Account von: Sohn.")


def main():
    visitorAlexaMusik = VisitorAlexaMusik()
    visitorAlexaBestellen = VisitorAlexaBestellen()

    vater = Vater()
    sohn = Sohn()

    print()
    print("Musik Visitor bei Vater:")
    vater.accept(visitorAlexaMusik)

    print()
    print("Musik Visitor bei Sohn:")
    sohn.accept(visitorAlexaMusik)

    print()
    print("Bestellen Visitor bei Vater:")
    vater.accept(visitorAlexaBestellen)

    print()
    print("Bestellen Visitor bei Sohn:")
    sohn.accept(visitorAlexaBestellen)



if __name__ == "__main__":
    main()