{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#imports\n",
    "\n",
    "##IMPORTS\n",
    "import tweepy\n",
    "import json\n",
    "import re\n",
    "import string\n",
    "from nltk.corpus import stopwords\n",
    "from nltk.tokenize import word_tokenize\n",
    "import nltk.classify.util\n",
    "from nltk.classify import NaiveBayesClassifier\n",
    "\n",
    "from auth import (\n",
    "    consumer_key,\n",
    "    consumer_secret,\n",
    "    access_token,\n",
    "    access_token_secret\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "auth = tweepy.OAuthHandler(consumer_key, consumer_secret)\n",
    "auth.set_access_token(access_token, access_token_secret)\n",
    "api = tweepy.API(auth)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "nickTrigger = ['#nickquote','😙','❤','😍','💓','😗','☺','😊','😛','💕','😀','😃','😚']\n",
    "schmidtTrigger = ['#schmidtquote','☹','😕','😩','😒','😠','😐','😦','😣','😫','😖','😞','💔','😢','😟']\n",
    "\n",
    "allTrigger = nickTrigger + schmidtTrigger"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "tweets = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "##TWITTER STREAM\n",
    "class MyStreamListener(tweepy.StreamListener): #collects tweets with the specific triggers\n",
    "\n",
    "    def on_status(self, status):\n",
    "        tweets.append(status.text.rstrip())\n",
    "        if len(tweets) > 200:\n",
    "            myStream.disconnect()\n",
    "\n",
    "myStreamListener = MyStreamListener()\n",
    "myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)\n",
    "\n",
    "myStream.filter(track=allTrigger, languages=['en'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'I think I wanna go to school 😫'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tweets[0] #prints first tweet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def store_tweets(file, tweets):\n",
    "    with open('tweets.txt', 'r') as f:\n",
    "        old_tweets = f.readlines()\n",
    "        if len(old_tweets) >= 0:\n",
    "            old_tweets = []\n",
    "    all_tweets = old_tweets + tweets\n",
    "    all_tweets = list(set(all_tweets))\n",
    "    all_tweets = [tweet.replace('\\n','')+\"\\n\" for tweet in all_tweets]\n",
    "    with open('tweets.txt', 'w') as f:\n",
    "        f.writelines(all_tweets)\n",
    "    \n",
    "    return all_tweets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_tweets(tweets):\n",
    "    tweets = [tweet.rstrip() for tweet in tweets]\n",
    "    tweets = [re.sub(r'RT @\\S+', '', tweet) for tweet in tweets]\n",
    "    tweets = [re.sub(r'@\\S+', '', tweet) for tweet in tweets]\n",
    "    tweets = [re.sub(r'http\\S+', '', tweet) for tweet in tweets]\n",
    "    \n",
    "    tweets = [tweet.translate({ord(char): ' ' for char in string.punctuation}) for tweet in tweets]\n",
    "  \n",
    "    return tweets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def sort_tweets(tweets):\n",
    "    nickTweets = [tweet for tweet in tweets if set(tweet)&set(nickTrigger)]\n",
    "    schmidtTweets = [tweet for tweet in tweets if set(tweet)&set(schmidtTrigger)]\n",
    "    \n",
    "    nickTweets = [re.sub(r'[^\\x00-\\x7F]+','', tweet) for tweet in nickTweets]\n",
    "    schmidtTweets = [re.sub(r'[^\\x00-\\x7F]+','', tweet) for tweet in schmidtTweets]\n",
    "\n",
    "    return nickTweets, schmidtTweets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "def parse_tweets(words):\n",
    "    words = words.lower()\n",
    "    words = word_tokenize(words)\n",
    "    words = [word for word in words if word not in stopwords.words(\"english\")]\n",
    "    word_dictionary = dict([(word, True) for word in words])\n",
    "    return word_dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def train_classifier(nickTweets, schmidtTweets):\n",
    "    nickTweets = [(parse_tweets(tweet),'positive') for tweet in nickTweets]\n",
    "    schmidtTweets = [(parse_tweets(tweet),'negative') for tweet in schmidtTweets]\n",
    "    fractionNick =  round(len(nickTweets) * 0.8)\n",
    "    fractionSchmidt =  round(len(schmidtTweets) * 0.8)\n",
    "    \n",
    "    train_set = schmidtTweets[:fractionNick] + nickTweets[:fractionNick]\n",
    "    test_set =  schmidtTweets[fractionSchmidt:] + nickTweets[fractionSchmidt:]\n",
    "    classifier = NaiveBayesClassifier.train(train_set)\n",
    "    accuracy = nltk.classify.util.accuracy(classifier, test_set)\n",
    "    return classifier, accuracy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_naughty(classifier, accuracy, user):\n",
    "    user_tweets = api.user_timeline(screen_name = user ,count=200)\n",
    "    user_tweets = [tweet.text for tweet in user_tweets]\n",
    "    user_tweets = clean_tweets(user_tweets)\n",
    "    \n",
    "    rating = [classifier.classify(parse_tweets(tweet)) for tweet in user_tweets]\n",
    "    percentSchmidt = rating.count('negative') / len(rating) \n",
    "\n",
    "    if percentSchmidt > .5:\n",
    "        print(user, \"is\", percentSchmidt * 100, \"percent more similar to Schmidt, with an accuracy of\", accuracy * 100)\n",
    "    else:\n",
    "        print(user, \"is\", 100 - (percentSchmidt * 100), \"percent more similar to Nick, with an accuracy of\", accuracy * 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nniewitham is 68.22916666666667 percent similar to Nick, with an accuracy of 92.1875\n"
     ]
    }
   ],
   "source": [
    "#execution\n",
    "tweets = store_tweets('tweets.txt', tweets)\n",
    "tweets = clean_tweets(tweets)\n",
    "nickTweets, schmidtTweets = sort_tweets(tweets)\n",
    "\n",
    "classifier, accuracy = train_classifier(nickTweets, schmidtTweets)\n",
    "calculate_naughty(classifier, accuracy, 'nniewitham')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
