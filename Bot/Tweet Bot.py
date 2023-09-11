import tweepy
import time

# Define your Twitter API keys and access tokens
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define the hashtag you want to search for
hashtag = '#YourHashtag'

while True:
    try:
        # Search for tweets containing the hashtag
        tweets = api.search(q=hashtag, count=10)

        for tweet in tweets:
            # Check if the tweet has not been liked already
            if not tweet.favorited:
                # Like the tweet
                api.create_favorite(tweet.id)
                print(f"Liked tweet by @{tweet.user.screen_name}: {tweet.text}")

        # Wait for some time before checking again (e.g., every 15 minutes)
        time.sleep(900)  # 900 seconds = 15 minutes
    except tweepy.TweepError as e:
        print(f"An error occurred: {e}")

# This script will run indefinitely, checking for new tweets with the specified hashtag and liking them.
