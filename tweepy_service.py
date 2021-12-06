import tweepy
import pandas as pd
import re
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import uuid
from config import settings

# prepare propertie for connect to twitter api
auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# prepare WordPunctTokenizer for tokenize
token = WordPunctTokenizer()
# prepare list regx for filter word 
re_list = ['(https?://)?(www\.)?(\w+\.)?(\w+)(\.\w+)(/.+)?', '@[A-Za-z0-9_]+','#']
combined_re = re.compile( '|'.join( re_list) )
regex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
# prepare set STOPWORDS for filter ignore word(is , am , are , i , you , we , they)
stopwords = set(STOPWORDS)

def search(keyword):

    # get tweet from twiiter api
    tweets = tweepy.Cursor(api.search_tweets, q=keyword + "-filter:retweets",lang='en').items(settings.items_limit)
    tweets_list = [[tweet.text] for tweet in tweets]
    # get datafrom json_twitter
    df = pd.DataFrame(tweets_list,columns=['Text'])
    # export dataframe to csv
    df.to_csv(settings.system_dir+'/test.csv', index = False, header=True)
    df = pd.read_csv(settings.system_dir+"test.csv")
    print("cotent="+df.loc[1])
    cleaned_tweets = []
    # clean and Tokenize 
    for i in range(0,settings.items_limit):
            cleaned_tweets.append(cleaning_tweets((df.Text[i])))
    string = pd.Series(cleaned_tweets).str.cat(sep=' ')
    # create word cloud visualize
    wordcloud = WordCloud(mode = "RGBA", background_color=None, width=800, stopwords=stopwords,height=400,max_font_size=200,max_words=50,collocations=False).generate(string)
    # export wordcloud to png
    plt.figure(figsize=(10,4))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(settings.system_dir+ keyword + '.png',transparent=True)

    return {
        "status": "000",
        "message": "success",
        "image":  keyword  + '.png'
    }

def cleaning_tweets(t):
    # convert dataframe to xml
    del_amp = BeautifulSoup(t, 'lxml')
    # get word from xml
    del_amp_text = del_amp.get_text()
    # remove link and http path format
    del_link_mentions = re.sub(combined_re, '', del_amp_text)
    # remove emoticons and special character
    del_emoticons = re.sub(regex_pattern, '', del_link_mentions)
    # convert upper case character to lower case character
    lower_case = del_emoticons.lower()
    words = token.tokenize(lower_case)
    # select word is lenght more than 2 character
    result_words = [x for x in words if len(x) > 2]
    return (" ".join(result_words)).strip()