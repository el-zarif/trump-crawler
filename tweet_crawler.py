import tweepy  # https://github.com/tweepy/tweepy
import json

# Twitter API credentials
consumer_key = "WsWSjvylwBcvMsC0oz7oawEVT"
consumer_secret = "2cBiLkITZjgYQnfvI5Ut4aC2P89dzzCJxrdACGB7P1FUNtXawp"
access_key = "378566205-NtPivxyd3N2eUn3QDrhdw3G5mRBbBpTTXpy2bXKr"
access_secret = "ISvTkqzJFV8mIIARN6iMkiA6X2UXPXGQXBR3MPrshmgNe"


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this
    # method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # make initial request for most recent tweets (25 is the maximum allowed
    # count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=25)

    # transform the tweepy tweets into an array that will populate the csv
    outtweets = [tweet.text.encode("utf-8") for tweet in new_tweets]

    # write tweets to file
    with open('tweets.txt', 'wb') as f:
        for tweet in outtweets:
            f.write(tweet)
            f.write(str.encode('\n\n'))

if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("realDonaldTrump")
