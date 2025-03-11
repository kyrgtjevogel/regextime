import re

def validate_tables_and_divs_in_file(filename):
    with open(filename, 'r') as file:
        html_text = file.read()

    # Zoek naar alle geopende tabel tags
    opening_table_tags = re.findall('<table>', html_text)
    closing_table_tags = re.findall('</table>', html_text)

    # Zoek naar alle geopende div tags
    opening_div_tags = re.findall('<div>', html_text)
    closing_div_tags = re.findall('</div>', html_text)

    # Controleer of het aantal geopende en gesloten tags hetzelfde is
    tables_valid = len(opening_table_tags) == len(closing_table_tags)
    divs_valid = len(opening_div_tags) == len(closing_div_tags)

    # Geef resultaat per bestand terug
    if tables_valid and divs_valid:
        return f"{filename}: Bestand is goed"
    else:
        return f"{filename}: Bestand is niet goed"

# Voorbeeld van hoe je de functie kunt gebruiken
print(validate_tables_and_divs_in_file('opdracht7.html')) 
print(validate_tables_and_divs_in_file('opdrachtnep7.html')) 
