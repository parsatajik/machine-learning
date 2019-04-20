import tweepy
from textblob import TextBlob

consumer_key = 'KK3URV21FbKqZRqnI2bS0chm6'
consumer_secret = 'ogNagsUdhgOHJXTCxBBHtKlvdDTw8sy7tr3i4N7h9ej9XX5bse'

access_token = '4013254152-Dqqv0CipxEQde9CdSsHfleTRVJH31SDCD180Y2d'
access_token_secret = 'QJZ1X3t2cOnYAymxVdDSnpOF2yvGnWATPjCTOMQVb44i9'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

with open('Twitter_Sentiment_Analysis/tweets.csv', 'w', newline='') as file:
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		if analysis.sentiment.polarity > 0.01:
			file.write('Positive, ')
		else:
			file.write('Negative, ')
		file.write(tweet.text)
		file.write('\n')