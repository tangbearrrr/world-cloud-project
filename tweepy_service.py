import tweepy
from config import settings

auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_token_secret)


def search():

    # get tweet from twiiter api
    api = tweepy.API(auth)
    public_tweets = api.search_tweets(q="manu", count=2)
    print(public_tweets)

    # analyze world cloud

    return {
        "status": "000",
        "message": "success"
    }