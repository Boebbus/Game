from __future__ import annotations
from abc import abstractmethod, ABC

class ATM:
    def __init__(self):
        self.kontostand = 1000
        self.zustand = None

    def karte_einstecken(self):
        if (self.zustand != None):
            self.zustand.karte_einstecken(self)

    def karte_rausnehmen(self):
        if (self.zustand != None):
            self.zustand.karte_rausnehmen(self)

    def zeige_kontostand(self):
        if (self.zustand != None):
            self.zustand.zeige_kontostand(self)

    def pin_verifikation_erfolgreich(self):
        if (self.zustand != None):
            self.zustand.pin_verifikation_erfolgreich(self)        

    def geld_abheben(self, betrag):
        if (self.zustand != None):
            self.zustand.geld_abheben(self, betrag)

    def aendere_zustand(self, neuerZustand: ATMZustand):
        if (self.zustand != None):
            self.zustand.exit()
        self.zustand = neuerZustand
        self.zustand.enter()


class ATMZustand(ABC):
    def karte_einstecken(self):
        pass

    def karte_rausnehmen(self):
        pass

    def geld_abheben(self):
        pass

    def pin_verifikation_erfolgreich(self):
        pass

    def zeige_kontostand(self):
        pass

    def enter(self):
        pass

    def exit(self):
        pass


class keineKarte(ATMZustand):
    def karte_einstecken(self, atm: ATM):
        # Zustandsänderung
        atm.aendere_zustand(hatKarte())

    def karte_rausnehmen(self, atm: ATM):
        print("Error: Ich habe keine Karte")

class hatKarte(ATMZustand):
    def enter(self):
        print("Karte wird gelesen.")

    def karte_einstecken(self):
        print("Ich habe schon eine Karte")

    def karte_rausnehmen(self, atm: ATM):
        atm.aendere_zustand(keineKarte())

    def pin_verifikation_erfolgreich(self, atm: ATM):
        atm.aendere_zustand(hatKarteUndPin())

    def zeige_kontostand(self, atm: ATM):
        print("Sie haben sich noch nicht verifiziert")

    def geld_abheben(self, atm: ATM, betrag: int):
        print("Sie haben sich noch nicht verifiziert")

class hatKarteUndPin(ATMZustand):
    def karte_einstecken():
        print("Ich habe schon eine Karte")

    def karte_rausnehmen(self, atm: ATM):
        atm.aendere_zustand(keineKarte())
    
    def zeige_kontostand(self, atm: ATM):
        print(f"Mein Kontostand ist: {atm.kontostand:.2f} Euro")

    def geld_abheben(self, atm: ATM, betrag: int):
        atm.kontostand = atm.kontostand - betrag
        print(f"{betrag} Euro erfolgreich abgehoben.")       
        print(f"Mein Kontostand ist: {atm.kontostand:.2f} Euro")

atm = ATM()
atm.aendere_zustand(keineKarte())
atm.karte_rausnehmen()
atm.karte_einstecken()
atm.geld_abheben(200)
atm.pin_verifikation_erfolgreich()
atm.geld_abheben(200)
atm.karte_rausnehmen()