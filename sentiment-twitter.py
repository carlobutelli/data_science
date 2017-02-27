import tweepy
from textblob import TextBlob

consumer_key = 'k7elowb0s28tejQJMhl5yfHbU'
consumer_secret = 'WeQCy7IPozT3pasnywr5cTolm3XhxLMIx6aU2VFm7UFjiAhTVb'

access_token = '2890651606-DGjqFWYk8I56HIxWtQOf6kTaKq0HGOupeS0xNeF'
access_token_secret = 'RUmD83ANCrLz3dE3eYbVum9nFXAmozy1Mxw4iym3OuxWE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create out api var to perform analysis
api = tweepy.API(auth)

# Store a list of tweets
public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
