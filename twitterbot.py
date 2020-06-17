from guizero import App, Text, PushButton, Picture, TextBox, ListBox, Box, info, CheckBox, ButtonGroup, Combo
import numpy as np
import pandas as pd
from twython import Twython
import random
import threading
import time

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



nickFile = "nick.txt"
nick = open("nick.txt" , "r")
schmidtFile = "schmidt.txt"
schmidt = open("schmidt.txt", "r")



#message = Text(App, text = '')#prints random from the list
nickList = []
schmidtList = []
tweetedList = []

#### COMMANDS

def tweetText():
    
    if modeChoice.value == "Nick Mode":
        if len(tweetatTextbox.value) >= 1:
            message = ("@" + tweetatTextbox.value + " " + random.choice(nickList))
        else:
            message = (random.choice(nickList))
        twitter.update_status(status=message)
        print("Tweeted: "+message)
        tweetListBox.append(message)
        
        
    if modeChoice.value == "Schmidt Mode":
        if len(tweetatTextbox.value) >= 1:
            message = ("@" + tweetatTextbox.value + " " + random.choice(schmidtList))
        else:
            message = (random.choice(schmidtList))
        twitter.update_status(status=message)
        print("Tweeted: " + message)
        tweetListBox.append(message)
        
   # if modeChoice.value == "AI Mode":
      #  nickorschmidt()
#def timerTweet():
    #if delayDropdown.value != "every 1 minute":
      #  t = threading.Timer(10.0, tweetText)
       # t.start()
        
  #  else:
    #    tweetText()
        
#def nickorschmidt():

def addNickTweet():
    if len(addTextTextbox.value) == 0:
        print("error")
        #info popup
    else:
        nick= open("nick.txt" , "a") #make it so we can append to file
        nick.write("\n" + addTextTextbox.value) #writes user input into text files
        nick.close() #closes file
        addTextTextbox.value = ""
        
def addSchmidtTweet():
    if len(addTextTextbox.value) == 0:
        print("error")
        #info popup
    else:
        schmidt= open("schmidt.txt" , "a") #make it so we can append to file
        schmidt.write("\n" + addTextTextbox.value) #writes user input into text files
        schmidt.close() #closes file
        addTextTextbox.value = ""
    
        
    
#### GUI
app = App(title = "Twitter Bot", bg="white", height=500, width=800)

titleText = Text(app, text = '"New Girl" Quote Bot', color="black", size = 20, font="Arial", align="top",)
buttonBox = Box(app, border=1, align="bottom", width="fill")
startButton = PushButton(buttonBox, text="Start", align="left", width="fill", command=tweetText)
stopButton = PushButton(buttonBox, text="Stop", align="right", width="fill")

boxBox = Box(app, border=0, align="top", width="fill")

leftBox = Box(boxBox, border=1, align="left", height="fill", width="fill")
tweetatBox = Box(leftBox, border=1, align="top", width="fill")
tweetatText = Text(tweetatBox, text="Tweet at @", color="black", size=12, font="Arial", align="left")
tweetatTextbox = TextBox(tweetatBox, align ="left", width=15)

modeBox = Box(leftBox, border=1, align="top", width="fill")
modeBox_note = Text(modeBox, text="Choose a mode:", color="black", size=12, font="Arial", align="top")
modeChoice = ButtonGroup(modeBox, options=["Nick Mode", "Schmidt Mode", "AI Mode"], horizontal=False,  align="left")

delayBox = Box(leftBox, border=1, align="top", width="fill")
delayBox_note = Text(delayBox, text="Tweet:", color="black", size=12, font="Arial", align="left")
delayDropdown = Combo(delayBox, align="left", options=["once", "every 1 minute", "every 2 minutes", "every 3 minutes", "every 4 minutes", "every 5 minutes", "every 6 minutes", "every 7 minutes", "every 8 minutes", "every 9 minutes", "every 10 minutes"])

addTextBox = Box(leftBox, border=1, align="top", width="fill")
addTextTextbox = TextBox(addTextBox, align ="left", width=40, height=10, multiline=True, scrollbar=True,text='Type tweet here with these formats: "Quote" - Nick **OR** "Quote" - Schmidt')
addNickTextButton = PushButton(addTextBox, text = 'Add tweet to "Nick" text file', align = "top", command=addNickTweet, width="fill")
addSchmidtTextButton = PushButton(addTextBox, text = 'Add tweet to "Schmidt" text file', align = "top", command=addSchmidtTweet, width="fill")

rightBox = Box(boxBox, border=2, align="left", height="fill", width="fill")

rightBox_title = Text(rightBox, text="Tweets Made", color="black", size=12, font="Arial", align="top")
tweetsBox = Box(rightBox, border=0, align="top", width="fill", height="fill")
tweetsBox_note = Text(tweetsBox, text="Tweets made go here", color="black", size=7, font="Arial", align="top")

tweetListBox = ListBox(tweetsBox, items=[], height="fill", width="fill", align="top", scrollbar="True")
#### Bot



x = 0
for i in nick: #our text file
    nickList.append(i)#appends one item from textfile to list
    x = x + 1 #creates the length of the list
x = x + 1
x = random.randint(0, len(nickList) - 1)
    
y = 0
for i in schmidt: #our text file
    schmidtList.append(i)#appends one item from textfile to list
    y = y + 1 #creates the length of the list
y = y+1
y = random.randint(0, len(schmidtList) - 1)



        


        
        
        









app.display()