import re

def is_valid_hexadecimaal(hexadecimaal):
    # Reguliere expressie om een geldig hexadecimaal getal te valideren (inclusief kleine letters)
    patroon = r'^[0-9A-Fa-f]+$'
    
    # Controleer of de opgegeven string overeenkomt met het patroon
    if re.match(patroon, hexadecimaal):
     return True
    else:
     return False

# Voorbeeldgebruik:
hex_nummer1 = "1A2F"
hex_nummer2 = "G3B8"
hex_nummer3 = "13b8"

print(is_valid_hexadecimaal(hex_nummer1))  # Output: True
print(is_valid_hexadecimaal(hex_nummer2))  # Output: False
print(is_valid_hexadecimaal(hex_nummer3))  # Output: True
