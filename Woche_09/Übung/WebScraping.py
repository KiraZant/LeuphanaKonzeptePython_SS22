"""
Aufgabenstellung: Nutzen Sie die vorgestellten Methoden des Web Scrapings, um die Anzahl der Zwischenüberschriften in
verschiedenen Wikipedia Artikeln miteinander zu vergleichen. Unterscheiden Sie dabei nach den verschiedenen Ebenen der
Überschriften und speichern Sie Ihre Ergebnisse in einem geeigneten DataFrame ab.

Wikipedia Artikel: Data Science, Python (Programmiersprache), Machine Learning, ...
Hinweis: Recherchieren Sie, welchen Tag Überschriften in HTML haben und wie sich verschiedene Ebenen unterscheiden.
"""
# Pakete importieren
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Lösung:
# Links zu Artikeln in Dictionary speichern
articles = {'Data Science': 'https://de.wikipedia.org/wiki/Data_Science',
            'Python': 'https://de.wikipedia.org/wiki/Python_(Programmiersprache)',
            'Machine Learning': 'https://de.wikipedia.org/wiki/Maschinelles_Lernen'}

# DataFrame für Ergebnisse erstellen
results = pd.DataFrame(index=['h1', 'h2', 'h3', 'h4'], columns=articles.keys())

# Schleife über Artikel erstellen
for article, link in articles.items():
    # HTML Code der Wikipedia Seite ziehen und in BeautifulSoup Objekt umwandeln
    page = requests.get(url=link)
    soup = BeautifulSoup(page.text, 'html.parser')
    # Über verschiedene Überschriften iterieren und im Code danach suchen
    for header_type in results.index:
        header = soup.find_all(header_type)
        # Anzahl in den DataFrame eintragen
        results.at[header_type, article] = len(header)

# Ergebnisse ausgeben lassen
print(results)
