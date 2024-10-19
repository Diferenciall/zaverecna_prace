from ui import UzivatelskeRozhrani
from evidence import EvidencePojistencu

print("-----------------------------------\nEvidence pojištěnců\n-----------------------------------")

def main():
    evidence = EvidencePojistencu()
    uzivatelske_rozhrani = UzivatelskeRozhrani(evidence)
    uzivatelske_rozhrani.menu()

if __name__ == "__main__":
    main()
