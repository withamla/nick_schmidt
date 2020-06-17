from guizero import App, Text, PushButton, ButtonGroup, Picture, TextBox, Slider, Combo, CheckBox
import time

password = "pizza"
app = App(title = "Pizza Place")



    
def welcomescreen():
    password = "pizza"
    welcomemessage = Text(app, text="Welcome to the Pizza Place!", size=25, font="Times New Roman", color="black")
    passwordbox = TextBox(app, width = 30)
    passwordentered = str(passwordbox.value)
    enterpassword = PushButton(app, command=menuscreen, text="ENTER PASSWORD")
    
def menuscreen():
    welcomemessage.hide()
    passwordbox.hide()
    enterpassword.hide()
    menutext = Text(app, text="Menu", size=25, font="Times New Roman", color="black")

    
def errorscreen():
    welcomemessage.hide()
    passwordbox.hide()
    enterpassword.hide()
    errormessage = Text(app, text="Invalid Input", size=25, font="Times New Roman", color="black")
    time.sleep(3)
    welcomescreen()

def checkpassword():
    passwordentered = str(passwordbox.value)
    if passwordentered == password:
        menuscreen()
    elif passwordentered != password:
        errorscreen()
        
        
        
welcomescreen()

    
    

#change_screens_Menu = PushButton(app, command=menuscreen, text="Menu")
#change_screens_Welcome.hide()
# if y == 2: #customize screen
# if y == 3: #cart
# if y == 4: #order placed

app.display()