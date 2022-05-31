import tweepy as tw
import pandas as pd
from tqdm import tqdm

# Um diesen Code laufen zu lassen benötigen Sie einen Twitter Developer Account. Hierfür folgen Sie den (vielen)
# Schritten hier https://developer.twitter.com/en/products/twitter-api

# Geben Sie danach den erhaltene Key und Access Token ein
my_api_key = ''
my_api_secret = ''

# Authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Legen Sie fest wonach Sie suchen
search_query = '#Python -filter:retweets'
# tweets laden
tweets = tw.Cursor(api.search_tweets, q=search_query, lang='en').items(500)

# Liste erstellen
tweets_copy = []
for tweet in tweets:
    tweets_copy.append(tweet)

print('Total Tweets fetched:', len(tweets_copy))

# DataFrame initialisieren
tweets_df = pd.DataFrame()

# Tweets in DDF abspeichern
for tweet in tqdm(tweets_copy):
    hashtags = []
    try:
        for hashtag in tweet.entities['hashtags']:
            hashtags.append(hashtag['text'])
        text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
    except:
        text = ''
    tweets_df = tweets_df.append(pd.DataFrame({'user_name': tweet.user.name,
                                               'user_location': tweet.user.location,
                                               'user_description': tweet.user.description,
                                               'user_verified': tweet.user.verified,
                                               'date': tweet.created_at,
                                               'text': text,
                                               'hashtags': [hashtags if hashtags else None],
                                               'source': tweet.source
                                               }))
    tweets_df = tweets_df.reset_index(drop=True)

# Anschauen
print(tweets_df.head())

# Abspeichern
tweets_df.to_csv('TweetsPython.csv', index=False)
