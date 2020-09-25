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

user_id = 1191156315273486337

# get_user() takes in user's name or id and returns user information
user = api.get_user(user_id)
# screen_name is attribute of user that returns username and name is name of user
print("The twitter id " + str(user_id) + " belongs to the username: " + user.screen_name
      + " or to the person: " + user.name)

tweets = api.user_timeline(user_id = "44196397", count = 5)
for tweet in tweets:
    print(tweet.text)



