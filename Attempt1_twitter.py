import tweepy as tw
import pandas as pd

consumer_key= 'xlGRb5DfObVcynGkG6EEYPxLt'
consumer_secret= 'yJi2zljCWX3WGQ5PqBZgcbx2PzmGgiJiLc3sEJrRe0JSr1Imtj'
access_token= '358835618-ENGl4ELrdGgvKSyqddk8G0goIVu2Fqqc5SruoZeY'
access_token_secret= '2TRjvWCazut3i7tUcjFrRVpW1UTH95bY5KWt1lbx9S1RS'


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


search_words = "#Pray_for_Nesamani"
date_since = "2019-05-27"

tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

for tweet in tweets:
    print(tweet.created_at)
