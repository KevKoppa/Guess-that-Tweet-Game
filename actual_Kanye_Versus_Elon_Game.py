'''
Comments after finishing project

Some problems I had were with removing tags from tweets and loading the first 3200 tweets of each user. When I first tried
to iterate through each tweet string to remove the '@' and the corresponding name afterwards, the program couldn't edit
the list of tweets properly and it got really messy. I realized another thing complicating this was that the number of
items in the list of tweets was capped at 200 because of the nature of .user_timeline() method. Consequently, tried using
a Cursor object to iterate through each twitter user's page but I couldn't manage to get 3200 tweets.
I left the number of tweets generated to 200 for the functionality of rest of the program and also left the tags in the
tweets.
One thing I found really fun was creating a way for the user to enter in two random usernames and play the game with
twitter users that aren't only Kanye and Elon. This part was fun since I was able to enter in my own username and guess
what I tweeted (it wasn't hard since I rarely tweet).
Overally, I enjoyed this project and can't wait to revisit it to expand its functionalities.
'''

import tweepy
import random 

# Twitter authorization keys declared
CONSUMER_KEY = "d0Ozs4wZfTfeNU1YtMSiCjvZu"
CONSUMER_SECRET = "Nc8BVMUakWGmtJepWkibPBqKRKaXaf1ULNWmTRRrI4lwg07QZH"
TWITTER_KEY = "1191156315273486337-ZVHv024VOz69JGMtMxXz16zMnvAglO"
TWITTER_SECRET = "e8cZb2spcDv27AOl0K3YAwsXVZoIOk981JQxotPosPBvd"

# Authorization to use Twitter's API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)
api = tweepy.API(auth)


# Prompt to begin game or enter in two different users
answer = input("Instructions:\nYou will be presented with a tweet that could be from two different twitter users.\n" +
                "The default two users for this game are Elon Musk and Kanye West.\n" +
                "Note that if a tweet is merely a link, then the tweet is a picture or it is a continuation of the tweet.\n" +
               "Are you ready to start the game? If yes, answer \'y.\' If you would like to play the game with two " +
               "different twitter users, click another key.\n")

# Begins game or doesn't depending on answer to last question
# different_users is a boolean and is whether or not user is entering in different user accounts
if answer == 'y':
    different_users = False
else:
    screen_name1 = input("Enter in the username of the first person (without '@'): ")
    screen_name2 = input("Enter in the username of the second person (without '@'): ")
    different_users = True


# Function Definition for taking in the account username of someone and returning a list of their tweets
def make_tweet_list(some_screen_name):
    # number of tweets tweeted by user
    num_of_user_tweets = api.get_user(screen_name=some_screen_name).statuses_count

    # creates list of at most first 200 tweets by user
    if (num_of_user_tweets < 200):
        list1 = api.user_timeline(screen_name=some_screen_name, count=num_of_user_tweets)
    else:
        list1 = api.user_timeline(screen_name=some_screen_name, count=200)

    # returns list of tweets made by user
    return list1


# Depending on whether the user wants to play with the default users, elon and kanye, or enter in their own,
# this if-block will create a list of each user's tweets
if different_users:
    # What would have been the list of elon tweets is the first username tweets
    elon_tweets = make_tweet_list(screen_name1)

    # What would have been the list of kanye tweets is the second username tweets
    kanye_tweets = make_tweet_list(screen_name2)

else:
    # list of Elon's tweets and Kanye's tweets
    elon_tweets = api.user_timeline(screen_name="elonmusk", count=200)
    kanye_tweets = api.user_timeline(screen_name="kanyewest", count=200)


# Create an interable list of tweets made by Elon
elon_list = []
for tweet in elon_tweets:
    elon_list.append(tweet.text)

# Create an interable list of tweets made by Kanye
kanye_list = []
for tweet in kanye_tweets:
    kanye_list.append(tweet.text)

# Variable for storing correct answer to question
correct_answer = ""

# Variables for storing score and number of attempts
attempts = 0
score = 0

# Variable for user to indicate whether they want to keep playing game
continue_game = True
while continue_game:
    # Randomly selecting the index number if selecting from elon list of tweets
    index_for_elon_list = random.randint(0, len(elon_list) - 1)

    # Randomly selecting the index if selecting from kanye list of tweets
    index_for_kanye_list = random.randint(0, len(kanye_list) - 1)
    rand_num = random.randint(0, 1)


    # Using random numbers to print a random tweet from either Kanye or Elon
    if rand_num == 0:
        print(elon_list[index_for_elon_list])

        # Depending on whether the player entered in their own two users or used the default ones, the correct
        # answer will be different.
        if different_users:
            correct_answer = screen_name1
        else:
            correct_answer = "elonmusk"
    else:
        print(kanye_list[index_for_kanye_list])
        # Depending on whether the player entered in their own two users or used the default ones, the correct
        # answer will be different.
        if different_users:
            correct_answer = screen_name2
        else:
            correct_answer = "kanyewest"


    guess = input("Who do you think tweeted the following tweet? Enter in the correct username. ")
    if guess == correct_answer:
        print("Congratulations! That is correct.")
        score += 1
        attempts += 1
    else:
        print("Sorry. That is incorrect.")
        attempts += 1

    # print score and accuracy upon completing question
    print("score: " + str(score))
    print("Accuracy: " + str(score) + "/" + str(attempts))

    # Ask user if they want to continue game
    continue_game = input("Type \'y\' to continue to next question. Type anything else to discontinue game. ") == 'y'

# Once out of while loop, continue_game = False and game has ended.
print("Thank you for playing!")






    



