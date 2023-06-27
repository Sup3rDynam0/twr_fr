from dotenv import load_dotenv
import os
import tweepy

load_dotenv()

consumer_key = os.environ.get("TWITTER_KEY")
consumer_secret = os.environ.get("TWITTER_SECRET_KEY")

API_Key = os.getenv('TWITTER_CLIENT')
API_Key_Secret = os.getenv("TWITTER_CLIENT_SECRET")

access_token = os.getenv("TWITTER_ACCESS")
access_token_secret = os.getenv("TWITTER_ACCESS_SECRET")

bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

def create_tweet(tweet):
    client = tweepy.Client(bearer_token,consumer_key,consumer_secret,access_token,access_token_secret)
    tweet = tweet
    client.get_me()
    client.create_tweet(text=tweet)