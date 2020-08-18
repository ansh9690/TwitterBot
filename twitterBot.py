import tweepy
import time

api_key = ''
api_secret_key = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(api_key, api_secret_key)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# print(user.name)
# print(user.location)

# Post a tweet
# api.update_status("Hello, I am Anshu Prakash")

# list of all followers
# for follower in tweepy.Cursor(api.followers).items():
#     print(follower.name)

# follow the users
# api.create_friendship("_thesid01")

a = input("Enter - hasgtag or username..?"+"\n")
if a == "hashtag":
    q = input('Enter hashtag to like : ')
    search = '#'+q
    numberOftweets = int(input('Enter number of tweets to like : '))
    for tweets in tweepy.Cursor(api.search, search, rpp=100).items(numberOftweets):
        try:
            print("Liked tweets")
            tweets.favorite()
            api.create_friendship(screen_name=tweets.author.screen_name)
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
else:
    username = input("Enter username to like tweets : ")
    tweets = api.user_timeline(screen_name=username)
    for tweets in tweets:
        try:
            print("Liked tweets")
            tweets.favorite()
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
