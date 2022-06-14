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
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import dok_matrix
from Distanzmetriken import similarity
import pandas as pd
from WordFrequency import word_count
from DocumentFrequency import document_frequency

dataset = pd.read_csv('/Users/kirstenzantvoort/PycharmProjects/LeuphanaKonzeptePython_SS22_InClass/Woche_10/Übung/TweetsPython_Cleaned.csv')
dataset['text'] = dataset['text'] .astype('str')


def calculate_tf_idf(text_list):
    # Absolute Worthäufigkeiten
    vocab, word_freq = word_count(text_list)
    #Relative term-frequency nehmen indem es durch die Summe der Reihe = #Wörte im Tweet geteilt wird
    tf = word_freq/word_freq.sum(axis=1)

    #Absolute Document Frequence berechnen
    doc_freq = document_frequency(text_list, vocab)
    # Relative IDF berechnen
    idf = {term: ((len(text_list)/count)) for term, count in doc_freq.items()}

    # Neue Matrix erstellen für TF-IDF und über Items aus Word_Freq iterieren
    tf_idf = dok_matrix(word_freq.shape)
    inverse_vocab = {v: k for k, v in vocab.items()}

    #?
    for j, i in tf.keys():
        tf_idf[j, i] = tf[j, i] * idf[inverse_vocab[i]]
    return tf_idf, vocab

#Anwendung: Wiederholen Sie den Schritt c) aus der WordFrequency Aufgabe auf dem TF-IDF Daten
dataset = pd.read_csv('/Users/kirstenzantvoort/PycharmProjects/LeuphanaKonzeptePython_SS22_InClass/Woche_10/Übung/TweetsPython_Cleaned.csv')
dataset['text'] = dataset['text'] .astype('str')
vocab, M = word_count(dataset['text'])

S = similarity(M)
S = pd.DataFrame(S.todense())

indexs = S[37].sort_values(ascending=False).iloc[:6].index
print([text for text in dataset['text'][indexs]])