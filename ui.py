from pojistenec import Pojistenec

class UzivatelskeRozhrani:
    def __init__(self, evidence):
        self.evidence = evidence

    def nacti_text(self, prompt):
        while True:
            text = input(prompt).strip()
            if text:
                return text
            else:
                print("Toto pole nesmí být prázdné.")

    def nacti_vek(self):
        while True:
            try:
                vek = int(input("Zadejte věk: "))
                if vek > 0:
                    return vek
                else:
                    print("Věk musí být kladné číslo.")
            except ValueError:
                print("Zadejte platný věk.")

    def nacti_telefon(self):
        return input("Zadejte telefonní číslo: ")

    def pridat_pojistence(self):
        jmeno = self.nacti_text("Zadejte jméno: ")
        prijmeni = self.nacti_text("Zadejte příjmení: ")
        vek = self.nacti_vek()
        telefon = self.nacti_telefon()

        novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.evidence.pridat_pojistence(novy_pojistenec)

    def zobrazit_pojistence(self):
        self.evidence.zobrazit_vsechny_pojistence()

    def vyhledat_pojistence(self):
        jmeno = self.nacti_text("Zadejte jméno: ")
        prijmeni = self.nacti_text("Zadejte příjmení: ")
        self.evidence.vyhledat_pojistence(jmeno, prijmeni)

    def menu(self):
        while True:
            print("\nVyberte si požadovanou akci:")
            print("1 - Přidat nového pojištěnce")
            print("2 - Zobrazit seznam pojištěnců")
            print("3 - Vyhledat pojištěnce")
            print("4 - Ukončit aplikaci")

            volba = input()

            if volba == "1":
                self.pridat_pojistence()
            elif volba == "2":
                self.zobrazit_pojistence()
            elif volba == "3":
                self.vyhledat_pojistence()
            elif volba == "4":
                print("Aplikace je ukončena.")
                break
            else:
                print("Neplatná volba. Zkuste to znovu.")
