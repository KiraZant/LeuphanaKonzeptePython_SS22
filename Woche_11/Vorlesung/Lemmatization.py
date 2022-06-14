import pandas as pd
from nltk.stem import WordNetLemmatizer

# Verfügbare Modelle/Corpora auswählen
#import nltk
#nltk.download()

# Daten laden
dataset = pd.read_csv('/Users/kirstenzantvoort/PycharmProjects/LeuphanaKonzeptePython_SS22_InClass/Woche_10/Übung/TweetsPython_Cleaned.csv')
dataset['text'] = dataset['text'].astype('str')
# Liste aller Wörter
all_words = [i for j in dataset['text'] for i in j.split(' ')]

# Liste des Vokabulars
unique_words = list(set(all_words))

# Lemmatizer landen und anwenden
lemmatizer = WordNetLemmatizer()
lemmas = set([lemmatizer.lemmatize(word) for word in unique_words])

# Anzahl pro Schritt printen
print('Wörter insgesamt:', len(all_words))
print('Vokabular:', len(unique_words))
print('Anzahl Lemmas:', len(lemmas))