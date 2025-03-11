import re

# Expressies en teksten
expressies = [
    (r'[0-9]*', '06 - 1234 1234'),
    (r'[0-9]+', '06 - 1234 1234'),
    (r'[0-9]+$', '06 - 1234 1234'),
    (r'max.*', 'Maximale temperatuur is 12 graden'),
    (r'[max]', 'x-men'),
    (r'[k-mK-M]', 'Dit is een voorbeeld'),
    (r'^[k-mK-M].*', 'Matig je alcohol gebruik!'),
    (r'^[k-mK-M].*', 'Gaat de KLM failliet?'),
    (r'^[a-kA-K]+.*', 'De kakkerlak kakt'),
    (r'^[k-mK-M]+.*', 'De kakkerlak kakt erg veel')
]

# Functie om expressies te testen
def test_expressions():
    for i, (expressie, tekst) in enumerate(expressies, start=1):
        match = re.match(expressie, tekst)
        result = "Match" if match else "Geen match"
        
        # Resultaten tonen
        print(f"Expressie {i}: {expressie}")
        print(f"Tekst: {tekst}")
        print(f"Resultaat: {result}")
        print("-" * 50)

# Test alle expressies
test_expressions()
