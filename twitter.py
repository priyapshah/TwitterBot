import tweepy
import time
from keys import * 

auth = tweepy.OAuthHandler(apiKey,apiKeySecret)

auth.set_access_token(accessToken,accessTokenSecret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me();

searchKey = 'UPenn'
numTweets = 5

for tweet in tweepy.Cursor(api.search, searchKey).items(numTweets):
    try: 
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10) # Creates a time gap between posts
    except tweepy.TweepError as err: 
        print(err.reason)
    except StopIteration:
        break