import tweepy
from config import settings

auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)



def search(keyword):

    # get tweet from twiiter api
    tweets = tweepy.Cursor(api.search_tweets, q=keyword + "-filter:retweets").items(settings.items_limit)
    for tweet in tweets:
        print(tweet.text)

    return {
        "status": "000",
        "message": "success"
    }