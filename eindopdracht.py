import re

# HTML-bestand lezen
def extract_urls_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_string = file.read()

    # Patroon om URLs te extraheren uit <a> tags
    pattern = r'<a\s+[^>]*?href=(["\']?)(.*?)\1[^>]*?>'

    # Hier de expressie en wat het doet
    # <a\s+ zoekt naar de <a tags en de \s+ houdt rekening met een of meer spaties er tussen.
    # [^>]*?href= matcht alle tekst van de <a tot de href= [^>]*? zorgt ervoor dat dat niet doorloopt tot de laatste > aan het eind van de expressie.
    # (["\']?) matcht een aanhalingsteken ("" of '') als die er is na de href=
    # (.*?) matcht de URL, anders wordt dat natuurlijk niet getoond. Door de ? stopt het bij het volgende aanhalingsteken, spatie, of einde van de string.
    # \1 zorgt ervoor dat de sluitende aanhalingstekens hetzelfde zijn als de opende (als deze er zijn)
    # [^>]*?> matcht de rest van de <a tag tot de laatste > tag aan het einde van de zin.

    # Vind de matches
    matches = re.findall(pattern, html_string)

    # Extraheert de URL's
    urls = [match[1] for match in matches]

    return urls

# Print de gevonden URL's
file_path = 'eindopdracht.html'
urls = extract_urls_from_html(file_path)
for url in urls:
    print(url)
