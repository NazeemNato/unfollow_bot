#!/usr/bin/python3
import tweepy
from time import sleep
from keep_alive import keep_alive


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)
keep_alive()

for f in friends:
    try:
        if f not in followers:
            api.destroy_friendship(f)
            print("Unfollowed",f)
            sleep(25)
    except Exception as e:
        print(e)

print("finished")