import re
# Kyran Koehler
def validate_phone_number(phone_number):
    pattern = r"^06\d{8}$"
    if re.match(pattern, phone_number):
        return True
    return False

# Voorbeeldgebruik:
phone_number = input("Voer een 06-nummer in: ")
if validate_phone_number(phone_number):
    print("Het ingevoerde nummer is geldig.")
else:
    print("Het ingevoerde nummer is ongeldig.")