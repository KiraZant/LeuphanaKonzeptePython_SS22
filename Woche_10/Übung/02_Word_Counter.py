"""
Zählen Sie die häufigst benutzten Wörter über alle tweets hinweg. Plotten Sie diese erneut als Barplot und nutzen dann
das WordCloud Package um eine sogenannte WordCloud zu plotten, in dem die häufigsten Wörter visualisiert werden.

Für einige der Schritte müssen Sie die Form/ den Datentyp der Tweets verändern. Probieren Sie aus, lesen Sie die
error-codes und googlen Sie wenn nötig welche Schritte sinnvoll sind.

"""

from wordcloud import WordCloud

# a) Laden Sie einen der mit Clean_Tweets.py gesäuberten Datensätze mit dem Namensanhang '_Cleaned.csv'

# b) Nutzen Sie das gelernte aus Aufgabe 1 und übertragen Sie alle Wörter in eine flat-Liste
# (hier sind ggf. weitere Schritte notwendig)

# c) Schreiben Sie eine Funktion, welche die Häufigkeit der einzelnen
# Wörter zählt und den nachfolgenden Bar Plot mit der Häufigkeit der 15 meistgenutzten Wörter produziert.

def top_n_words(words, n=None):
    pass

# b) Erstellen Sie mithilfe des WordCloud packages eine WordCloud und plotten Sie diese.
# Tipp: Nutzen Sie zum plotten die wordcloud.to_array() Methode

# c) Wie Sie vermutlich sehen, sind die meistgenutzten Wörter in der WordCloud ganz andere als im Bar Plot. Der Grund
# hierfür ist der Default Parameter STOPWORDS. Lassen Sie den gleichen Code wie vorher laufen, aber geben den Parameter
# stopwords={''} in die WordCloud() ein. Worum könnte es sich bei Stopwords handeln?

