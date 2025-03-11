import re  

string = """<!DOCTYPE html><html><head><title>Mijn webpagina</title></head><body>
<h1>Mijn eerste kop</h1><p>Dit is een paragraaf.</p><h1>Mijn tweede kop</h1><p>Dit is nog een paragraaf.</p></body></html>"""


pattern = r"<h1>.*?</h1>"


matches = re.findall(pattern, string, flags=re.I)  # De vlag re.I maakt de zoekopdracht case-insensitive

print(matches)