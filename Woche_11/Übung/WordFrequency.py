"""
Bei der Verarbeitung von Texten spielt die Häufigkeit der einzelnen Wörter eine wichtige Rolle. Daher wird die
sogenannte Bag-of-Words (BoW) genutzt, um die Häufigkeit innerhalb von Einheiten zu bestimmen. Nutzen Sie die Schritte auf
den Vorlesungsfolien um BoW Features für einen twitter Datensatz zu generieren.
"""
"""
a) Schreiben Sie eine Funktion word_index(), die eine Liste von Wörtern als Parameter erwartet und ein Dictionary erstellt,
dass jedem Wort (key) einen Index zuweist. Groß- und Kleinschreibung soll dabei keine Rolle spielen ('a' und 'A' haben nur
einen index).

Beispiel (Reihenfolge ist irrelevant):
word_index("A rose is a rose".split()) -> {'rose': 0, 'a': 1, 'is': 2}
"""
from scipy.sparse import dok_matrix
import pandas as pd
from Distanzmetriken import cosine_similarity, similarity

def word_index(words):
    words = [word.lower() for word in words]
    return {i: j for i, j in zip(set(words), range(len(set(words))))}

"""
b. Erstellen Sie die Funktion word_count(), die eine Liste an Texten erwartet (in Form von Wörtern innerhalb einer 
Liste) und die folgenden beiden Werte zurückgibt:
- Das Vokabular/Wörterbuch, das jedes Wort einem Index zuordnet (wie von der obigen Funktion `word_index` berechnet)
- Eine Sparse Matrix, die zählt, wie oft jedes Wort in jedem Text vorkommt. Die Matrix sollte MxN groß sein, wobei M 
die Anzahl der Texte und N die Länge des Vokabulars (d.h. die Gesamtzahl der eindeutigen Wörter) ist.

Tipp: Nutzen Sie das Beispiel für eine dok_matrix aus der Dokumentation um sie zu initiieren und zu befüllen. 
Hierfür kann ein for-loop mehr Sinn ergeben, als eine Comprehension. 
(dok_matrix: https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.dok_matrix.html)
"""

def word_count(text_list):
    all_words = [word.lower() for text in text_list for word in text.split()]
    vocabulary = word_index(all_words)

    matrix = dok_matrix((len(text_list), len(vocabulary)), dtype='int32')

    for i in range(len(text_list)):
        for word in text_list[i].split(' '):
            j = vocabulary[word.lower()]
            matrix[i, j] += 1
    return vocabulary, matrix

"""
c) Anwendung: Um die Ähnlichkeit von Sätzen zu bestimmen, kann die Anzahl der sich überlappenden Wörter bestimmt werden.
Importieren und nutzen Sie die bereits vorgeschrieben Funktionen similarity aus Distanzmetriken.py um eine 
NxN Matrix zu erhalten in der die Ähnlichkeiten zwischen Tweets berechnet werden. Schauen Sie sich die 5 ähnlichsten 
tweets für den tweet mit dem Index 37 ('defining the problem in your data science project can lead to success') an.
Was fällt Ihnen auf?

"""
dataset = pd.read_csv('/Users/kirstenzantvoort/PycharmProjects/LeuphanaKonzeptePython_SS22_InClass/Woche_10/Übung/TweetsPython_Cleaned.csv')
dataset['text'] = dataset['text'] .astype('str')
vocab, M = word_count(dataset['text'])

S = similarity(M)
S = pd.DataFrame(S.todense())

indexs = S[37].sort_values(ascending=False).iloc[:6].index
print([text for text in dataset['text'][indexs]])
