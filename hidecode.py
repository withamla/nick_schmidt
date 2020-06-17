##Fowler's Example Hide/Display GUI
##November 2018

from guizero import App, Text, TextBox, PushButton, CheckBox, ButtonGroup

app = App(title="Tacos OR Mac & Cheese") #Create program and name it

welcome_Message = Text(app, text="Please order a Taco, or change screens for Mac & Cheese")

def tacoScreen():
    print("Changing GUI to Mac & Cheese")
    tacoA.hide()
    tacoAA.hide()
    tacoB.hide()
    tacoBB.hide()
    change_screens_Taco.hide()
    macA.show()
    macAA.show()
    macB.show()
    macBB.show()
    change_screens_Mac.show()
    welcome_Message.set("Please order Mac & Cheese, or change screens for a Taco")

def macScreen():
    print("Changing GUI to Tacos")
    macA.hide()
    macAA.hide()
    macB.hide()
    macBB.hide()
    change_screens_Mac.hide()
    tacoA.show()
    tacoAA.show()
    tacoB.show()
    tacoBB.show()
    change_screens_Taco.show()
    welcome_Message.set("Please order a Taco, or change screens for Mac & Cheese")



#welcome message, followed by GUI elements

tacoA = Text(app, text="Enter Taco Quantity")
tacoAA = TextBox(app)
tacoB = Text(app, text="Enter Taco Flavor")
tacoBB = TextBox(app)

macA = Text(app, text="Enter Mac Quantity")
macAA = TextBox(app)
macB = Text(app, text="Enter Mac Flavor")
macBB = TextBox(app)
macA.hide()
macAA.hide()
macB.hide()
macBB.hide()

change_screens_Taco = PushButton(app, command=tacoScreen, text="Mac & Cheese")
change_screens_Mac = PushButton(app, command=macScreen, text="Tacos")
change_screens_Mac.hide()
#button for roll

#display app!
app.display()

