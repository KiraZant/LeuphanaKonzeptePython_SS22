"""
Die Document Frequency gibt an, in wie vielen Dokumenten bzw. Sätzen ein bestimmter Term bzw. ein bestimmtes Wort
enthalten ist. Sie gibt darüber Aufschluss, welche Wörter in wie vielen Sätzen genutzt werden. Schreiben Sie eine
Funktion, die eine Liste von Sätzen/Tweets in Form von einzelnen Wörtern und das Vokabel-Dictionary aus WordFrequency.py
als Eingabe erwartet und daraus die absolute Dokument Frequency für alle Wörter bestimmt.
"""
import pandas as pd
from WordFrequency import word_count

def document_frequency(text_list, vocab):
    # Über Wortliste iterieren und prüfen in wie vielen Sätzen Wort vorhanden ist
    document_freq = {}
    for w in vocab.keys():
        document_freq[w] = sum([w in (text.split()) for text in text_list])
    return document_freq

dataset = pd.read_csv('/Users/kirstenzantvoort/PycharmProjects/LeuphanaKonzeptePython_SS22_InClass/Woche_10/Übung/TweetsPython_Cleaned.csv')
dataset['text'] = dataset['text'] .astype('str')
vocab, M = word_count(dataset['text'])
document_freq = document_frequency(dataset['text'], vocab)