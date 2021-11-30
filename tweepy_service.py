import tweepy
import pandas as pd
import re
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import uuid
from config import settings


auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

token = WordPunctTokenizer()
re_list = ['(https?://)?(www\.)?(\w+\.)?(\w+)(\.\w+)(/.+)?', '@[A-Za-z0-9_]+','#']
combined_re = re.compile( '|'.join( re_list) )
regex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)

stopwords = set(STOPWORDS)

def search(keyword):

    # get tweet from twiiter api
    tweets = tweepy.Cursor(api.search_tweets, q=keyword + "-filter:retweets").items(settings.items_limit)
    tweets_list = [[tweet.text] for tweet in tweets]
    df = pd.DataFrame(tweets_list,columns=['Text'])
    df.to_csv(settings.system_dir+'/test.csv', index = False, header=True)
    df = pd.read_csv(settings.system_dir+"test.csv")

    cleaned_tweets = []
    for i in range(0,100):
        if( (i+1)%10 == 0 ): 
            cleaned_tweets.append(cleaning_tweets((df.Text[i])))
    
    string = pd.Series(cleaned_tweets).str.cat(sep=' ')

    wordcloud = WordCloud(mode = "RGBA", background_color=None, width=1600, stopwords=stopwords,height=800,max_font_size=200,max_words=50,collocations=False).generate(string)
    plt.figure(figsize=(40,30))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(settings.system_dir+ keyword + '.png')

    return {
        "status": "000",
        "message": "success",
        "image": settings.system_dir + keyword  + '.png'
    }

def cleaning_tweets(t):
    del_amp = BeautifulSoup(t, 'lxml')
    del_amp_text = del_amp.get_text()
    del_link_mentions = re.sub(combined_re, '', del_amp_text)
    del_emoticons = re.sub(regex_pattern, '', del_link_mentions)
    lower_case = del_emoticons.lower()
    words = token.tokenize(lower_case)
    result_words = [x for x in words if len(x) > 2]
    return (" ".join(result_words)).strip()