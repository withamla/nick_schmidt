from guizero import App, Text, PushButton, Picture, TextBox, Box, info

app = App(title = "Insult Generator", bg="snow")

def welcomeScreen():
    titleText = Text(app, text = "Insult Generator", color="firebrick3", size=38, font="Free Mono", align="top")

def insultScreen():
    titleText = Text(app, text = "Insult Generator", color="firebrick3", size=38, font="Free Mono", align="top")
    welcomeBox.hide()
    insultButton.hide()
def cyoScreen():
    titleText = Text(app, text = "Insult Generator", color="firebrick3", size=38, font="Free Mono", align="top")
    welcomeBox.hide()
    insultButton.hide()


def insult():
    welcomeBox.hide()
    insultButton.hide()
    
    
    insultText = Text (insultBox, text = "You " + "___" " like a " + "___" + " ___"+ "!", size = 20, color="snow", font="Free Mono")
    app.bg = "firebrick3"
    titleText.text_color = "snow"
    
    moreInsults.show()
    moreInsults.text_color = "firebrick3"
    moreInsults.bg = "snow"
    
    createInsults.show()
    createInsults.text_color = "firebrick3"
    createInsults.bg = "snow"
    
def moreInsult ():
    insultBox.hide()
    
    
def cyo():
    insultBox.hide()
    welcomeBox.hide()
    
    
    cyoText = Text (app, text = "Create Your Own Insult", size = 20, color="snow", font="Free Mono")

    
    
    

welcomeBox = Box(app, border=0, align="top")

prisonmike = Picture(welcomeBox, image="prisonmike.gif", align="top")

#buttons
buttonBox = Box(app, width="fill", align="bottom")

insultButton = PushButton(buttonBox, text="Generate Insult", command=insult, align="bottom")
insultButton.text_size = 15
insultButton.font = "Free Mono"
insultButton.bg = "firebrick3"
insultButton.text_color = "snow"

moreInsults = PushButton(buttonBox, text="Get another insult", command= moreInsult, align="left")
moreInsults.text_size = 13
moreInsults.font = "Free Mono"
moreInsults.hide()

createInsults = PushButton(buttonBox, text="Create your own insults", command=cyo, align="right")
createInsults.text_size = 13
createInsults.font = "Free Mono"
createInsults.hide()

insultBox = Box(app, border = 1, align = "top")



    


                          
app.display()