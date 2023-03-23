'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.
import tweepy
import time

# Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define the tweet content
tweet = "Learn Python today! #Python #Programming"

# Send a tweet every hour
while True:
    try:
        api.update_status(tweet)
        print("Tweeted: %s" % tweet)
        time.sleep(3600)  # wait for an hour before tweeting again
    except tweepy.TweepError as error:
        print("Error sending tweet: %s" % error)
