import re
from bs4 import BeautifulSoup
import pandas as pd

tweets = pd.read_csv('../../09_Datenquellen/Übung/TweetsML.csv')
print(tweets.head(10))

print([text for text in tweets['text'].head(15)])

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


tweets['text'] = tweets['text'].apply(func=tweet_cleaner)
print([text for text in tweets['text'].head(15)])

tweets.to_csv('TweetsML_Cleaned.csv', index=False)
