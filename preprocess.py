import re
import pandas as pd
import contractions

def remove_emoji(s):
    emoji_pattern = re.compile(
          '['
          u'\U0001F600-\U0001F64F'  # emoticons
          u'\U0001F300-\U0001F5FF'  # symbols & pictographs
          u'\U0001F680-\U0001F6FF'  # transport & map symbols
          u'\U0001F1E0-\U0001F1FF'  # flags (iOS)
          u'\U00002702-\U000027B0'
          u'\U000024C2-\U0001F251'
          ']+',
          flags=re.UNICODE)
    return emoji_pattern.sub(r'', s)

# remove URL from the tweets
def remove_URL(s):
    url = re.compile(r'https?://\S+|www\.||pic.twitter.com\S+')
    return url.sub(r'', s)

# to remove any special characters and extra space
def normalizeString(s): 
    s = re.sub("@[A-Za-z0-9]+","",s)
    s = s.replace('&amp', '')
    s = remove_emoji(s)
    s = contractions.fix(s)
    s = remove_URL(s)
    s = s.replace("'s", 's')
    s = re.sub(r"[^a-zA-Z0-9.,? ]+", r" ", s)
    s = s.strip()
    
    return s

# cleaning tweets in the dataset
def preprocessing(data):

    tweet_text = data['tweet'].str.lower() # convert the tweets into lower case
    tweet_text = tweet_text.tolist() # create a list of tweets

    for i in range(len(tweet_text)):

        tweet_text[i] = str(tweet_text[i])
        tweet_text[i] = ' '.join(tweet_text[i].split('\n'))
        tweet_text[i] = ' '.join(normalizeString(str).strip() for str in tweet_text[i].split())

    data['tweet_text'] = tweet_text

    return data
