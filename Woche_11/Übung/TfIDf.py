"""
Fortgeschritten (Optional)
Um die Relevanz von Wörter innerhalb eines Satzes und innerhalb des gesamten Corpus an Wörtern zu bestimmen, kann die
sogenannte TF-IDF verwendet werden - die Term Frequency-Inverse Document Frequency. Die Informationen und Formeln
hier für sind auf den Slides zu finden. Die Relevanz eines Wortes steigt proportional zur Häufigkeit an,
wird jedoch durch die Gesamthäufigkeit im Corpus wieder verringert.

Nutzen Sie Ihre bereits bestehenden Methoden zur Document Frequency und Term Frequency, um eine Methode zur Berechnung
der TF-IDF zu implementieren.

TF(i) * IDF(i)

TF(i) = Freq(i,j) / L(j)
IDF(i) = N / f(i)

i = Term | j = Dokument | L(j) = Gesamtzahl aller Terme in Dokument j | Freq(i,j) = Häufigkeit des Terms i in Dokument j
N = Anzahl aller Dokumente | f(i) = Anzahl aller Dokumente in denen der Term i vorkommt
"""
from scipy.sparse import dok_matrix
from Distanzmetriken import similarity
import pandas as pd
from WordFrequency import word_count
from DocumentFrequency import document_frequency

def calculate_tf_idf(text_list):
    # Absolute Worthäufigkeiten

    #Relative term-frequency nehmen indem es durch die Summe der Reihe = #Wörte im Tweet geteilt wird

    #Absolute Document Frequence berechnen

    # Relative IDF berechnen

    # Neue Matrix erstellen für TF-IDF und über Items aus Word_Freq iterieren

    pass
