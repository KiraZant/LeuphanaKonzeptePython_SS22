import re
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from textblob import TextBlob

retweets = r'@[A-Za-z0-9_]+'  # entfernt Twitter namen = alle Buchstaben- und Nummerreihenfolgen die nach einem @ kommen
hashtags = r'#[A-Za-z0-9]+'  # entfernt hashtags, da diese i.d.R. aufgrund fehlender Leerzeichen nicht auswertbar sind
http_web = r'https?://[^ ]+'  # entfernt Websites = alle Zeichen, die direkt nach http:// oder https:// kommen
www_web = r'www.[^ ]+'  # entfernt Websites die gleich mit www anfangen = alle Zeichen, die direkt auf www. folgen
nummern = '[^a-zA-Z ]'  # entfernt alles was nicht im alphabet oder ein Leerzeichen ist


def tweet_cleaner(text):
    text = BeautifulSoup(text, 'lxml').get_text()
    text = ' '.join(
        re.sub(retweets + '|' + hashtags + '|' + http_web + '|' + www_web + '|' + nummern, '', text).split())
    return text.lower()


# #Python Daten laden
dataset = pd.read_csv('../../Woche_09/Übung/TweetsPython.csv')
# Cleaning der tweets
dataset['text'] = dataset['text'].apply(func=tweet_cleaner)

# Polaritätsscore berechnen
dataset['Polarity'] = dataset['text'].apply(lambda t: TextBlob(t).sentiment.polarity)
dataset['word_count'] = dataset['text'].apply(lambda t: len(str(t).split()))
dataset['letter_count'] = dataset['text'].apply(len)

# Verteilung der Polaritätsscores plotten
fig, axs = plt.subplots()
fig.suptitle('Polarity Score Distribution', fontsize=16)
sns.histplot(dataset['Polarity'], ax=axs, binwidth=0.05)
plt.tight_layout()
plt.show()

# Anzahl Character plotten
fig, axs = plt.subplots(nrows=2)
fig.suptitle('Content Length Distribution')
sns.histplot(dataset['word_count'], binwidth=2, ax=axs[0])
axs[0].set(title='Word Count')
sns.histplot(dataset['letter_count'], binwidth=5, ax=axs[1])
axs[1].set(title='Letter Count')
plt.tight_layout()
plt.show()
