from guizero import App, Box, Text, ButtonGroup, CheckBox, TextBox, PushButton, Combo #imports

import tweepy
import json
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from twython import Twython
from twython import TwythonStreamer
from auth import (
    consumer_key, 
    consumer_secret, 
    access_token, 
    access_token_secret
)

twitter = Twython(
    consumer_key, 
    consumer_secret, 
    access_token, 
    access_token_secret
)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets=[]
class MyStreamListener(tweepy.StreamListener):
     def on_status(self, status):
        tweets.append(status.text.rstrip())
        if len(tweets) > 200:
            myStream.disconnect()

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=["Advice"], languages=['en'])

pos_emojis = [chr(uni) for uni in [128537, 10084, 128525, 128147, 128535, 9786, 128522, 128539, 128149, 128512, 128515, 128538]]
neg_emojis = [chr(uni) for uni in [9785, 128533, 128553, 128530, 128544, 128528, 128550, 128547, 128555, 128534, 128542, 128148, 128546, 128543]]

all_emojis = pos_emojis + neg_emojis

def store_tweets(file,tweets):
    with open('tweets.txt','r') as f:
        old_tweets = f.readlines()
        
    all_tweets = tweets + old_tweets 
    all_tweets = list(set(all_tweets))
    all_tweets = [tweet.replace('\n','')+"\n" for tweet in all_tweets]

    with open('tweets.txt', 'w') as f:
        f.writelines(all_tweets)
    
    return all_tweets 

def clean_tweets(tweets):
    tweets = [tweet.rstrip() for tweet in tweets]
    tweets = [re.sub(r'@\S+','', tweet) for tweet in tweets]
    tweets = [re.sub(r'http\S+','', tweet) for tweet in tweets]
    tweets = [tweet.translate({ord(char): '' for char in string.punctuation}) for tweet in tweets]
   
    return tweets

def sort_tweets(tweets):
    positive_tweets = [tweet for tweet in tweets if set(tweet) & set(pos_emojis)]
    negative_tweets = [tweet for tweet in tweets if set(tweet) & set(neg_emojis)]
    positive_tweets = [re.sub(r'[^\x00-\x7F]+','', tweet) for tweet in positive_tweets]
    negative_tweets = [re.sub(r'[^\x00-\x7F]+','', tweet) for tweet in negative_tweets]
    
    return positive_tweets, negative_tweets

def parse_tweets(words):
    words = words.lower()
    words = word_tokenize(words)
    words = [word for word in words if word not in stopwords.words('english')]
    word_dictionary = dict([(word, True) for word in words])
    
    return word_dictionary

def train_classifier(positive_tweets, negative_tweets):
    positive_tweets = [(parse_tweets(tweet),'positive') for tweet in positive_tweets]
    negative_tweets = [(parse_tweets(tweet),'negative') for tweet in negative_tweets]
    fraction_pos =  round(len(positive_tweets) * 0.8)
    fraction_neg =  round(len(negative_tweets) * 0.8)

    train_set = negative_tweets[:fraction_pos] + positive_tweets[:fraction_pos]
    test_set =  negative_tweets[fraction_neg:] + positive_tweets[fraction_neg:]
    classifier = NaiveBayesClassifier.train(train_set)
    
    accuracy = nltk.classify.util.accuracy(classifier, test_set)
    return classifier, accuracy

def calculate_naughty(classifier, accuracy, user):
    user= str(user_text.value)
    user_tweets = api.user_timeline(screen_name = user ,count=200)
    user_tweets = [tweet.text for tweet in user_tweets]
    user_tweets = clean_tweets(user_tweets)
    
    rating = [classifier.classify(parse_tweets(tweet)) for tweet in user_tweets]
    percent_naughty = rating.count('negative') /len(rating)
        
    if percent_naughty > 0.5:
        print(user,'is', percent_naughty * 100, "percent NAUGHTY, with an accuracy of", accuracy * 100)
            #this is where we tweet at someone negativly
        print("“Wake up determined, go to bed satisfied.” -Dwayne “The Rock” Johnson")
    else:
        print(user,'is', 100 - (percent_naughty * 100) , "percent NICE, with an accuracy of", accuracy * 100)
            #this is where we tweet positivly
        print("“Whenever I’m about to do something, I think, ‘Would an idiot do that?’ And if they would, I would not do that thing.” -Dwight Schrute")

 #EXECUTE THE PROGRAM
#tweets = store_tweets('tweets.txt', tweets)
#tweets = clean_tweets(tweets)
#pos_tweets, neg_tweets = sort_tweets(tweets)
#classifier, accuracy = train_classifier(pos_tweets, neg_tweets)


app = App(title= "Twitter Bot")

bot_name = Text(app, text= "Inspirational Quote Bot", size=30, font="Comic Sans", color="cornflower blue", grid=[0,0], align="top")#bot name
bot_box = Box(app, border=1, layout="grid", grid=[0,5], height=170, width=400, align="top") #box containing the options

space_box3= Box (app, border=0, layout="grid", grid=[0,4], height=30, width= 500) #spacer

tweets_output_box= Box(app, border=1, layout="grid", grid=[0,1], height= 150, width=500) #box containing the output from tweets
create_tweets= Box(tweets_output_box, border=0, layout="grid", grid=[0,0], height=30, width=500, align="top")
tweet_output= Text(create_tweets, text="                               Recent Tweets                                                       ", size=13, font="Comic Sans", color="black", grid=[3,0], align="top")
create_tweets.bg="cornflower blue"

make_tweets_box= Box(tweets_output_box, border=1, layout="grid", grid=[0,1], height=40, width=499, align="top") #box to input tweets
tweet_textbox= TextBox(make_tweets_box, grid=[1,0], align="left", width=68, text="[Tweet something here]")
add2_box= Box(make_tweets_box, border=0, layout="grid", grid=[0,0], height= 37, width=100, align="right")
results_box= Box(tweets_output_box, border=1, layout="grid", grid=[0,3], height=90, width=650, align="top")
add_button= PushButton(add2_box, text="Add to CSV", grid=[0,0], height=1, width=10, align="top")
tweet_textbox.bg="white"
results_box.bg="white"
add_button.bg="lightgray"
make_tweets_box.bg="lightgray"


username_box = Box(bot_box, border=0, layout="grid", grid=[3,0], height=20, width=300,align="left")#box to type in twitter username
user_text = Text(username_box, text="michaela", size=12, font="Comic Sans", color="black", grid=[0,0], align="left")
users_name= TextBox(username_box, grid=[3,0], align="left")


mode_box = Box(bot_box, border=1, layout="grid", grid=[0,2], height=100, width=200, align="left")#mode box
mode_name = Text(mode_box, text="Which Mode?", grid=[0,0], size=13, font= "Comic Sans", align="top")
mode_choice = ButtonGroup(mode_box, options=[ ["Serious", "S"], ["Funny/Goofy", "K"],["Ai", "A"] ], selected="M", horizontal=False, grid=[0,1], align="left")

add_box = Box(bot_box, border=1, layout="grid",grid=[3,3], height=30, width=150, align="top")#add to CSV
add_tweet = CheckBox(add_box, text="Add Tweet to CSV", grid=[0,0], align="left")

space_box4= Box(app, border=0, layout="grid", grid=[0,4], height=30, width=500, align="top")#spacer

def run_program(tweets):
    print(str(users_name.value))
    user=(str(users_name.value))
    tweets = store_tweets('tweets.txt', tweets)
    tweets = clean_tweets(tweets)
    pos_tweets, neg_tweets = sort_tweets(tweets)
    classifier, accuracy = train_classifier(pos_tweets, neg_tweets)
    calculate_naughty(classifier, accuracy, user)
    
    

start_button= PushButton(app, text="Start", grid=[0,5], height=50, width=27, align="left", command=run_program(tweets))#stop and start buttons
start_button.bg="white smoke"


stop_button= PushButton(app, text="Stop", grid=[0,5], height=50, width=70, align="right")
stop_button.bg="white smoke"

delay_box= Box(bot_box, border=1, layout="grid", height= 60, width=205, grid=[3,2], align="top")#duration between tweets
delay_text= Text(delay_box, text="Delay in between tweets", grid=[0,0], size=12, font="Comic Sans", align="left")
time_options= Combo(delay_box, options=["1 minute","2 minutes","3 minutes","4 minutes","5 minutes","6 minutes","7 minutes","8 minutes","9 minutes","10 minutes"],grid=[0,1], align="top") 

#spacers
space_box1= Box(bot_box, border=0, layout="grid", grid=[0,3], height=15, width=150,align="left")
space_box2= Box(bot_box, border=0, layout="grid", grid=[0,1], height=15, width=150, align="top")

app.display()