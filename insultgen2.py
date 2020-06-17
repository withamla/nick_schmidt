from guizero import App, Text, PushButton, Picture, TextBox, Box, info
import random

app = App(title = "Insult Generator", bg="snow")
nounFile = "noun.txt"
noun = open("noun.txt", "r")
adjectiveFile = "adjective.txt"
verbFile = "verb.txt"

def welcomeScreen():
    welcomeBox.show()
    buttonBox1.show()
    
    insultBox.hide()
    buttonBox2.hide()
    
    cyoBox.hide()
    buttonBox3.hide()

def insultScreen():
    welcomeBox.hide()
    buttonBox1.hide()
    
    insultBox.show()
    buttonBox2.show()
    if noun.mode == 'r':
        contents = noun.read()
        print(contents)
    #x = (random.randint(0, len(nounFile)-1))
    
def cyoScreen():
    welcomeBox.hide()
    buttonBox1.hide()
    insultBox.hide()
    buttonBox2.hide()
    
    cyoBox.show()
    buttonBox3.show()
    
    
#welcome screen
titleText = Text(app, text = "Insult Generator", color="firebrick3", size=38, font="Free Mono", align="top")

welcomeBox = Box(app, border=0, align="top")
buttonBox1 = Box(app, width="fill", align="bottom")

prisonmike = Picture(welcomeBox, image="prisonmike.gif", align="top")

insultButton = PushButton(buttonBox1, text="Generate Insult", command = insultScreen, align="bottom")
insultButton.text_size = 15
insultButton.font = "Free Mono"
insultButton.bg = "firebrick3"
insultButton.text_color = "snow"


    
#insult screen
insultBox = Box(app, border=0, align="top")
insultBox.hide()
buttonBox2 = Box(app, width="fill", align="bottom")
buttonBox2.hide()

backButton1 = PushButton(buttonBox2, text="<< Back", command=welcomeScreen, align = "left")
backButton1.text_size = 15
backButton1.font = "Free Mono"
backButton1.bg = "firebrick3"
backButton1.text_color = "snow"

cyoButton = PushButton(buttonBox2, text="Create your own", command=cyoScreen, align = "right")
cyoButton.text_size = 15
cyoButton.font = "Free Mono"
cyoButton.bg = "firebrick3"
cyoButton.text_color = "snow"



    
#cyo screen
cyoBox = Box(app, border=0, align="top")
cyoBox.hide()
buttonBox3 = Box(app, width="fill", align="bottom")
buttonBox3.hide()

backButton2 = PushButton(buttonBox3, text="<< Back", command=welcomeScreen, align = "left")
backButton2.text_size = 15
backButton2.font = "Free Mono"
backButton2.bg = "firebrick3"
backButton2.text_color = "snow"
