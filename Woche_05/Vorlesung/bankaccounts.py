class Konto:

    def __init__(self, guthaben, name, iban):
        self.__kontostand = guthaben
        self.name = name
        self.iban = iban

    def einzahlen(self, betrag):
        self.__kontostand += betrag
        return 0

    def auszahlen(self, betrag):
        if self.__kontostand - betrag >= 0:
            self.__kontostand -= betrag
        else:
            print("Gewünschter Betrag überschreitet das Limit")

    def get_kontostand(self):
        return self.__kontostand



class Depotkonto(Konto):

    def __init__(self, aktien_liste, guthaben, name, iban):
        Konto.__init__(self, guthaben, name, iban)
        if type(aktien_liste) == list:
            self.aktien_liste = aktien_liste
        else:
            print("aktien_liste muss vom Typ Liste sein")

    def aktie_kaufen(self, preis, aktien_namen):
        self._Konto__kontostand -= preis
        self.aktien_liste.append(aktien_namen)

    def einzahlen(self, betrag, kosten=2):
        self._Konto__kontostand += betrag - 2


if __name__ == "__main__":
    acc1 = Konto(1, "Jonas", "DE1234")
    acc2 = Konto(100, "Michael", "DE9876")
    print(acc1.__dict__)
    wert = acc1.einzahlen(100)
    print(wert)
    acc3 = Depotkonto([], 0, "Jonas", "DE1234")
    acc3.einzahlen(100)
    print(acc3.get_kontostand())
    acc3.auszahlen(30)
    acc3.aktie_kaufen(5, "Tolles Unternehmen")
    print(acc3.aktien_liste)

