class EvidencePojistencu:
    def __init__(self):
        self.pojistenci = []

    def pridat_pojistence(self, pojistenec):
        self.pojistenci.append(pojistenec)
        print("\nPojištěnec byl úspěšně přidán.")

    def zobrazit_vsechny_pojistence(self):
        if not self.pojistenci:
            print("\nŽádní pojištěnci nebyli zaznamenáni.")
        else:
            for pojistenec in self.pojistenci:
                print(pojistenec)

    def vyhledat_pojistence(self, jmeno, prijmeni):
        nalezeni_pojistenci = [p for p in self.pojistenci if p.jmeno.lower() == jmeno.lower() and p.prijmeni.lower() == prijmeni.lower()]
        if nalezeni_pojistenci:
            for pojistenec in nalezeni_pojistenci:
                print(pojistenec)
        else:
            print(f"Pojištěnec {jmeno} {prijmeni} nebyl nalezen.")

