import re  

string = """<!DOCTYPE html><html><head><title>Mijn webpagina</title></head><body>
<h1>Mijn eerste kop</h1><p>Dit is een paragraaf.</p><h1>Mijn tweede kop</h1><p>Dit is nog een paragraaf.</p></body></html>"""


pattern = r"<h1>(.*?)</h1>"
# Het <h1> gedeelte zoekt naar de openingstags, dus de h1, omdat dit met deze symbolen aangegeven word <> matcht dit alleen maar de echte h1
# () is een "capturing group" alles wat hier tussen komt te staan leg je vast en word dus later gebruikt.
# .* betekent dat het alle tekens moet matchen binnen de h1 tag, de . is match elk teken 
# terwijl het * ervoor is om 0 of meer van hetzelfde patroon op te halen, omdat er natuurlijk meerdere h1 tags zijn.
# ? zorgt ervoor dat de expressie stopt bij het eerst mogelijke h1 tag. Als deze er niet zou staan zou de expressie de rest van de string blijven printen todat het bij de volgende h1 tag komt, dus dan krijg je ook "dit is een paragraaf" erin, dit hoort niet.
# dat is namelijk niet de opdracht.
# de </h1> werkt hetzelfde als de <h1>, maar zoekt dan de sluitingstekens van de h1.


matches = re.findall(pattern, string, flags=re.I)  # De vlag re.I maakt de zoekopdracht case-insensitive

print(matches)