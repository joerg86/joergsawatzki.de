from jinja2 import Template

# Template laden
with open('../templates/packliste.html.j2', 'r') as f:
    template_str = f.read()

# Test-Daten (beispielhaft für Corfu Trail)
data = {
    'packliste': {
        'name': 'Packliste Corfu Trail',
        'slug': 'corfu-trail',
        'icon': '🏔️',
        'beschreibung': 'Meine erste mehrtägige Wanderung – 9 Tage auf Korfu',
        'hero_bild': '/images/corfu-trail-hero.jpg'
    },
    'gesamtgewicht': '9.4',
    'anzahl_produkte': 45,
    'kategorien': {
        'Taschen & Rucksack': [
            {
                'name': 'Rucksack',
                'produktname': 'Osprey Atmos AG 65',
                'gewicht': 2100,
                'notizen': 'Perfekte Passform, sehr bequem auch bei langen Strecken',
                'kurzlink': 'https://gear.joergsawatzki.de/123',
                'anbieter': 'Bergfreunde'
            },
            {
                'name': 'Wasserdichte Packsäcke (2×)',
                'produktname': 'MNT10 Dry Bags',
                'gewicht': 96,
                'notizen': 'Für Kleidung und Einkäufe',
                'kurzlink': 'https://gear.joergsawatzki.de/44',
                'anbieter': 'Amazon'
            }
        ],
        'Zelten & Schlafen': [
            {
                'name': 'Schlafsack',
                'produktname': 'Cumulus Quilt 350',
                'gewicht': 580,
                'notizen': 'Ultraleichter Daunenschlafsack, Komfortbereich bis 5°C',
                'kurzlink': 'https://gear.joergsawatzki.de/18',
                'anbieter': 'Bergfreunde'
            },
            {
                'name': 'Isomatte',
                'produktname': 'Therm-a-Rest NeoAir Xlite',
                'gewicht': 350,
                'notizen': 'Sehr packbar, R-Wert 4.2',
                'kurzlink': 'https://gear.joergsawatzki.de/19',
                'anbieter': 'Bergfreunde'
            },
            {
                'name': 'Kopfkissen',
                'produktname': 'Sea to Summit Aeros Ultralight Pillow',
                'gewicht': 62,
                'notizen': 'Aufblasbar, ultraleicht',
                'kurzlink': 'https://gear.joergsawatzki.de/20',
                'anbieter': 'Amazon'
            }
        ],
        'Kochen': [
            {
                'name': 'Kochset',
                'produktname': 'Trangia UL 27',
                'gewicht': 755,
                'notizen': 'Spiritus-Kocher mit 2 Töpfen und Pfanne',
                'kurzlink': 'https://gear.joergsawatzki.de/30',
                'anbieter': 'Amazon'
            },
            {
                'name': 'Spork',
                'produktname': 'Titan-Spork',
                'gewicht': 19,
                'notizen': 'Löffel und Gabel in einem',
                'kurzlink': 'https://gear.joergsawatzki.de/21',
                'anbieter': 'Amazon'
            }
        ],
        'Kleidung': [
            {
                'name': 'Wanderschuhe',
                'produktname': 'Salomon X Ultra 4 GTX',
                'gewicht': None,
                'notizen': 'Wasserdicht, guter Grip',
                'kurzlink': 'https://gear.joergsawatzki.de/25',
                'anbieter': 'Bergfreunde'
            }
        ]
    }
}

# Rendern
template = Template(template_str)
html = template.render(**data)

# Speichern
with open('test-corfu-trail.html', 'w') as f:
    f.write(html)

print("✅ Gerendert nach test-corfu-trail.html")