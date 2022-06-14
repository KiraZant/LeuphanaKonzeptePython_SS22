# Übung Woche 11

## Aufgabe 0 - Worthäufigkeit
Bei der Verarbeitung von Texten spielt die Häufigkeit der einzelnen Wörter eine wichtige Rolle. Daher wird die
sogenannte Bag-of-Words (BoW) genutzt, um die Häufigkeiten der Wörter innerhalb von Einheiten zu zählen. Nutzen Sie 
die Schritte auf den Vorlesungsfolien um BoW Features für einen twitter Datensatz zu generieren.

a) Schreiben Sie eine Funktion word_index(), die eine Liste von Wörtern als Parameter erwartet und ein Dictionary erstellt,
dass jedem Wort (key) einen Index zuweist. Groß- und Kleinschreibung soll dabei keine Rolle spielen ('a' und 'A' haben nur
einen index).

Beispiel (Reihenfolge ist irrelevant):
word_index("A rose is a rose".split()) -> {'rose': 0, 'a': 1, 'is': 2}

b. Erstellen Sie die Funktion word_count(), die eine Liste an Texten erwartet (in Form von Wörtern innerhalb einer 
Liste) und die folgenden beiden Werte zurückgibt:
- Das Vokabular/Wörterbuch, das jedes Wort einem Index zuordnet (wie von der obigen Funktion `word_index` berechnet)
- Eine Sparse Matrix, die zählt, wie oft jedes Wort in jedem Text vorkommt. Die Matrix sollte MxN groß sein, wobei M 
die Anzahl der Texte und N die Länge des Vokabulars (d.h. die Gesamtzahl der eindeutigen Wörter) ist.

Tipp: Nutzen Sie das Beispiel für eine dok_matrix aus der Dokumentation um sie zu initiieren und zu befüllen. 
Hierfür kann ein for-loop mehr Sinn ergeben, als eine Comprehension. 
(dok_matrix: https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.dok_matrix.html)

c) Anwendung: Um die Ähnlichkeit von Sätzen zu bestimmen, kann die Anzahl der sich überlappenden Wörter bestimmt werden.
Importieren und nutzen Sie die bereits vorgeschrieben Funktionen similarity aus Distanzmetriken.py um eine 
NxN Matrix zu erhalten in der die Ähnlichkeiten zwischen Tweets berechnet werden. Schauen Sie sich die 5 ähnlichsten 
tweets für den tweet mit dem Index 37 ('defining the problem in your data science project can lead to success') an.
Was fällt Ihnen auf?

## Aufgabe 1 - Document Frequency


Die Document Frequency gibt an, in wie vielen Dokumenten bzw. Sätzen ein bestimmter Term bzw. ein bestimmtes Wort
enthalten ist. Sie gibt darüber Aufschluss, welche Wörter in wie vielen Sätzen genutzt werden. Schreiben Sie eine
Funktion, die eine Liste von Sätzen/Tweets in Form von einzelnen Wörtern und das Vokabel-Dictionary aus WordFrequency.py 
als Eingabe erwartet und daraus die absolute Dokument Frequency für alle Wörter bestimmt.

## Aufgabe 2 (OPTIONAL) - TF-IDF 

Um die Relevanz von Wörter innerhalb eines Satzes und innerhalb des gesamten Corpus an Wörtern zu bestimmen, kann die
sogenannte TF-IDF verwendet werden - die Term Frequency-Inverse Document Frequency. Die Informationen und Formeln
hier für sind auf den Slides zu finden. Die Relevanz eines Wortes steigt proportional zur Häufigkeit an,
wird jedoch durch die Gesamthäufigkeit im Corpus wieder verringert.

Nutzen Sie Ihre bereits bestehenden Methoden zur Document Frequency und Term Frequency, um eine Methode zur Berechnung
der TF-IDF zu implementieren.
