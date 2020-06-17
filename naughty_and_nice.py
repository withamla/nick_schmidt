{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 499,
   "metadata": {},
   "outputs": [],
   "source": [
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
   "execution_count": 500,
   "metadata": {},
   "outputs": [],
   "source": [
    "auth = tweepy.OAuthHandler(consumer_key, consumer_secret)\n",
    "auth.set_access_token(access_token, access_token_secret)\n",
    "api = tweepy.API(auth)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 501,
   "metadata": {},
   "outputs": [],
   "source": [
    "pos_emojis = ['😙','❤','😍','💓','😗','☺','😊','😛','💕','😀','😃','😚']\n",
    "neg_emojis = ['☹','😕','😩','😒','😠','😐','😦','😣','😫','😖','😞','💔','😢','😟']\n",
    "\n",
    "all_emojis = pos_emojis + neg_emojis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 502,
   "metadata": {},
   "outputs": [],
   "source": [
    "tweets = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 503,
   "metadata": {},
   "outputs": [],
   "source": [
    "##TWITTER STREAM\n",
    "class MyStreamListener(tweepy.StreamListener):\n",
    "\n",
    "    def on_status(self, status):\n",
    "        tweets.append(status.text.rstrip())\n",
    "        if len(tweets) > 200:\n",
    "            myStream.disconnect()\n",
    "\n",
    "myStreamListener = MyStreamListener()\n",
    "myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)\n",
    "\n",
    "myStream.filter(track=all_emojis, languages=['en'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 504,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'RT @_SJPeace_: The Police in Mallorca, Spain making rounds around villages on lock down to do this 😭\\n\\nTo alleviate the anxiety of the peopl…'"
      ]
     },
     "execution_count": 504,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tweets[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 505,
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
   "execution_count": 506,
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
   "execution_count": 507,
   "metadata": {},
   "outputs": [],
   "source": [
    "def sort_tweets(tweets):\n",
    "    positive_tweets = [tweet for tweet in tweets if set(tweet)&set(pos_emojis)]\n",
    "    negative_tweets = [tweet for tweet in tweets if set(tweet)&set(neg_emojis)]\n",
    "    \n",
    "    positive_tweets = [re.sub(r'[^\\x00-\\x7F]+','', tweet) for tweet in positive_tweets]\n",
    "    negative_tweets = [re.sub(r'[^\\x00-\\x7F]+','', tweet) for tweet in negative_tweets]\n",
    "\n",
    "    return positive_tweets, negative_tweets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 508,
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
   "execution_count": 509,
   "metadata": {},
   "outputs": [],
   "source": [
    "def train_classifier(positive_tweets, negative_tweets):\n",
    "    positive_tweets = [(parse_tweets(tweet),'positive') for tweet in positive_tweets]\n",
    "    negative_tweets = [(parse_tweets(tweet),'negative') for tweet in negative_tweets]\n",
    "    fraction_pos =  round(len(positive_tweets) * 0.8)\n",
    "    fraction_neg =  round(len(negative_tweets) * 0.8)\n",
    "    \n",
    "    train_set = negative_tweets[:fraction_pos] + positive_tweets[:fraction_pos]\n",
    "    test_set =  negative_tweets[fraction_neg:] + positive_tweets[fraction_neg:]\n",
    "    classifier = NaiveBayesClassifier.train(train_set)\n",
    "    accuracy = nltk.classify.util.accuracy(classifier, test_set)\n",
    "    return classifier, accuracy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 510,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_naughty(classifier, accuracy, user):\n",
    "    user_tweets = api.user_timeline(screen_name = user ,count=200)\n",
    "    user_tweets = [tweet.text for tweet in user_tweets]\n",
    "    user_tweets = clean_tweets(user_tweets)\n",
    "    \n",
    "    rating = [classifier.classify(parse_tweets(tweet)) for tweet in user_tweets]\n",
    "    percent_naughty = rating.count('negative') / len(rating) \n",
    "\n",
    "    if percent_naughty > .5:\n",
    "        print(user, \"is\", percent_naughty * 100, \"percent NAUGHTY, with an accuracy of\", accuracy * 100)\n",
    "    else:\n",
    "        print(user, \"is\", 100 - (percent_naughty * 100), \"percent NICE, with an accuracy of\", accuracy * 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 512,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nniewitham is 60.20942408376963 percent NICE, with an accuracy of 84.78260869565217\n"
     ]
    }
   ],
   "source": [
    "#execution\n",
    "tweets = store_tweets('tweets.txt', tweets)\n",
    "tweets = clean_tweets(tweets)\n",
    "pos_tweets, neg_tweets = sort_tweets(tweets)\n",
    "\n",
    "classifier, accuracy = train_classifier(pos_tweets, neg_tweets)\n",
    "calculate_naughty(classifier, accuracy, 'nniewitham')"
   ]
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
