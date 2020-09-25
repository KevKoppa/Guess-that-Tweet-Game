# This code was purely to learn features in the tweepy API. This isn't a part of my game. The game is located in
# the file actual_Kanye_Versus_Elon_Game.py
import tweepy

# Twitter authorization keys declared
CONSUMER_KEY = "d0Ozs4wZfTfeNU1YtMSiCjvZu"
CONSUMER_SECRET = "Nc8BVMUakWGmtJepWkibPBqKRKaXaf1ULNWmTRRrI4lwg07QZH"
TWITTER_KEY = "1191156315273486337-ZVHv024VOz69JGMtMxXz16zMnvAglO"
TWITTER_SECRET = "e8cZb2spcDv27AOl0K3YAwsXVZoIOk981JQxotPosPBvd"

# Authorization to use Twitter's API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)
api = tweepy.API(auth)

# Iterate through a list of first 5 timeline tweets and print them out!
public_tweets = api.home_timeline(count = 5)
for tweet in public_tweets:
    print(tweet.user.screen_name)