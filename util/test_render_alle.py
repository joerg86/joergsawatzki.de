from jinja2 import Template

# Template laden
with open('../templates/alle_packlisten.html.j2', 'r') as f:
    template_str = f.read()

# Test-Daten
data = {
    'packlisten': [
        {
            'name': 'Packliste Corfu Trail',
            'slug': 'corfu-trail',
            'icon': '🏔️',
            'beschreibung': 'Meine erste mehrtägige Wanderung – 9 Tage auf Korfu',
            'hero_bild': '/images/corfu-trail-hero.jpg'
        },
        {
            'name': 'Packliste Radreise Sommer',
            'slug': 'radreise-sommer',
            'icon': '🚴',
            'beschreibung': 'Packliste für Radreisen im Sommer bzw. in der Übergangszeit',
            'hero_bild': '/images/radreise-sommer-hero.jpg'
        },
        {
            'name': 'Packliste Radreise Winter',
            'slug': 'radreise-winter',
            'icon': '⛄',
            'beschreibung': 'Aktuelle Packliste für Radreisen im Winter',
            'hero_bild': '/images/radreise-winter-hero.jpg'
        },
        {
            'name': 'Packliste Tageswanderung',
            'slug': 'tageswanderung',
            'icon': '🥾',
            'beschreibung': 'Meine aktuelle Packliste für Tageswanderungen',
            'hero_bild': '/images/tageswanderung-hero.jpg'
        }
    ]
}

# Rendern
template = Template(template_str)
html = template.render(**data)

# Speichern
with open('test-output.html', 'w') as f:
    f.write(html)

print("✅ Gerendert nach test-output.html")