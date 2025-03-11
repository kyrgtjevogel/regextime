import re

def vervang_dubbele_spaties(tekst):
    # Zoek naar twee of meer spaties en vervang ze door een enkele spatie
    return re.sub(r'\s{2,}', ' ', tekst)

def main():
    # Voorbeeldteksten
    tekst1 = "Dit is een correcte tekst."
    tekst2 = "Dit  is   een  tekst   met   dubbele spaties."
    tekst3 = "Dit     is   een tekst    met    zes spaties achter elkaar."
    
    # Vervang dubbele spaties in elke tekst
    print(tekst1)
    print("Aangepaste tekst 1:", vervang_dubbele_spaties(tekst1))
    print()
    
    print(tekst2)
    print("Aangepaste tekst 2:", vervang_dubbele_spaties(tekst2))
    print()
    
    print(tekst3)
    print("Aangepaste tekst 3:", vervang_dubbele_spaties(tekst3))

if __name__ == "__main__":
    main()
