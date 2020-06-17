#imports

##IMPORTS
import tweepy
import json
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



nickTrigger = ['#nickquote']
schmidtTrigger = ['#schmidtquote']

allTrigger = nickTrigger + schmidtTrigger


tweets = []

##TWITTER STREAM
class MyStreamListener(tweepy.StreamListener): #collects tweets with the specific triggers

    def on_status(self, status):
        tweets.append(status.text.rstrip())
        if len(tweets) > 1:
            myStream.disconnect()

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=allTrigger, languages=['en'])

tweets[0] #prints first tweet

def store_tweets(file, tweets):
    with open('tweets.txt', 'r') as f:
        old_tweets = f.readlines()
        if len(old_tweets) >= 0:
            old_tweets = []
    all_tweets = old_tweets + tweets
    all_tweets = list(set(all_tweets))
    all_tweets = [tweet.replace('\n','')+"\n" for tweet in all_tweets]
    with open('tweets.txt', 'w') as f:
        f.writelines(all_tweets)
    
    return all_tweets

def clean_tweets(tweets):
    tweets = [tweet.rstrip() for tweet in tweets]
    tweets = [re.sub(r'RT @\S+', '', tweet) for tweet in tweets]
    tweets = [re.sub(r'@\S+', '', tweet) for tweet in tweets]
    tweets = [re.sub(r'http\S+', '', tweet) for tweet in tweets]
    
    tweets = [tweet.translate({ord(char): ' ' for char in string.punctuation}) for tweet in tweets]
  
    return tweets

def sort_tweets(tweets):
    nickTweets = [tweet for tweet in tweets if set(tweet)&set(nickTrigger)]
    schmidtTweets = [tweet for tweet in tweets if set(tweet)&set(schmidtTrigger)]
    
    nickTweets = [re.sub(r'[^\x00-\x7F]+','', tweet) for tweet in nickTweets]
    schmidtTweets = [re.sub(r'[^\x00-\x7F]+','', tweet) for tweet in schmidtTweets]

    return nickTweets, schmidtTweets

def parse_tweets(words):
    words = words.lower()
    words = word_tokenize(words)
    words = [word for word in words if word not in stopwords.words("english")]
    word_dictionary = dict([(word, True) for word in words])
    return word_dictionary

def train_classifier(nickTweets, schmidtTweets):
    nickTweets = [(parse_tweets(tweet),'positive') for tweet in nickTweets]
    schmidtTweets = [(parse_tweets(tweet),'negative') for tweet in schmidtTweets]
    fractionNick =  round(len(nickTweets) * 0.8)
    fractionSchmidt =  round(len(schmidtTweets) * 0.8)
    
    train_set = schmidtTweets[:fractionNick] + nickTweets[:fractionNick]
    test_set =  schmidtTweets[fractionSchmidt:] + nickTweets[fractionSchmidt:]
    classifier = NaiveBayesClassifier.train(train_set)
    accuracy = nltk.classify.util.accuracy(classifier, test_set)
    return classifier, accuracy

def calculate_naughty(classifier, accuracy, user):
    user_tweets = api.user_timeline(screen_name = user ,count=200)
    user_tweets = [tweet.text for tweet in user_tweets]
    user_tweets = clean_tweets(user_tweets)
    
    rating = [classifier.classify(parse_tweets(tweet)) for tweet in user_tweets]
    percentSchmidt = rating.count('negative') / len(rating) 

    if percentSchmidt > .5:
        print(user, "is", percentSchmidt * 100, "percent more similar to Schmidt, with an accuracy of", accuracy * 100)
    else:
        print(user, "is", 100 - (percentSchmidt * 100), "percent more similar to Nick, with an accuracy of", accuracy * 100)
        
        #execution
tweets = store_tweets('tweets.txt', tweets)
tweets = clean_tweets(tweets)
nickTweets, schmidtTweets = sort_tweets(tweets)

classifier, accuracy = train_classifier(nickTweets, schmidtTweets)
calculate_naughty(classifier, accuracy, 'nick_or_schmidt')