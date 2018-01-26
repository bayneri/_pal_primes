import json
import tweepy, time, sys

file = open("palindromic_primes.txt", "r")
data_file = file.read()
data = data_file.split(',')

CONSUMER_KEY = '***'
CONSUMER_SECRET = '***'
ACCESS_TOKEN = '***'
ACCESS_TOKEN_SECRET = '***'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

last_tweet = api.user_timeline(screen_name = '_pal_primes',count=1)[0].text
next_index = data.index(last_tweet) + 1
twit = data[next_index]
api.update_status(twit)