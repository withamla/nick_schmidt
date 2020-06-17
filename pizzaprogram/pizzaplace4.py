from guizero import App, Text, PushButton, ListBox, Picture, TextBox, Slider, Combo, CheckBox, Box, ButtonGroup, info
import time


app = App(title = "Pizza Place", bg="white")
welcomeBox = Box(app, layout="grid", border=2)
menuBox = Box(app, layout="grid", border=2)
totalPrice = []
toppingsChosen = []
cart = []

def addtocart():
    
    cart.append(sizeChoice.value)
    for i in customCheckboxes:
        if (i.value == 1):
            toppingsChosen.append(i.text)
            cart.append(i.text)
    
    
    if pepperoniCheck.value == 1:
        p=p+1.00
    if sauceCheck.value == 1:
        p=p+0.00
    if cheeseCheck.value == 1:
        p=p+0.00
    if baconCheck.value == 1:
        p=p+1.00
    if onionCheck.value == 1:
        p=p+1.00
    if mushroomCheck.value == 1:
        p=p+1.00
    if sausageCheck.value == 1:
        p=p+1.00
    if garlicCheck.value == 1:
        p=p+1.00
        
    if sizeChoice.value == "Small pizza":
        p=p + 8.50
    elif sizeChoice.value == "Medium pizza":
        p=p+10.00
    elif sizeChoice.value == "Large pizza":
        p=p+12.50
    if len(totalPrice) == 0:
        totalPrice.append(p)

    
    print(cart)
    print(p)
    print(totalPrice)


    for i in customCheckboxes:
        if (i.value == 1):
            p=p+1.00

information = ""
for i in toppingsChosen:
    if information == "":
        information = (str(i))
        cart.append(i)   
    else:
        information = information + ", " + str(i)
        info("Cart", sizeChoice.value + '\n' + (str(information)))
    print(sizeChoice.value)
    print(toppingsChosen)

small = 8.50
medium = 10.00
large = 13.50
sizes = [small, medium, large]

cheese = 0.00
sauce = 0.00
pepperoniCheck = 1.00
bacon = 1.00
sausage = 1.00
pineapple = 1.00
ham = 1.00
mushroom = 1.00
chicken = 1.00
spinach = 1.00
olives = 1.00
anchovies = 1.00
garlic = 1.00
onion = 1.00
toppings = [pepperoniCheck, cheese, sauce, bacon, sausage, pineapple, ham, mushroom, chicken, spinach, olives, anchovies, garlic, onion]
    
   


    

cbrPizza = 2.00
hawaiianPizza = 2.00
oldfashPizza = 2.00
meatloversPizza = 2.00
whitePizza = 2.00
buffchkPizza = 2.00
supremePizza = 2.00
veggiePizza = 2.00
margPizza = 2.00
bbqchkPizza = 2.00
specials = [cbrPizza, hawaiianPizza, oldfashPizza, meatloversPizza, whitePizza, buffchkPizza, supremePizza, veggiePizza, margPizza, bbqchkPizza]

garlicknots = 2.50
fries = 2.50
cheesefries = 3.50
meatballs = 3.00
mozzsticks = 4.50
wings = 6.00
sides = [garlicknots, fries, cheesefries, meatballs, mozzsticks, wings]


rigatoni = 10.00
spaghetti = 10.00
penne = 10.00
linguini = 10.00
fettuccini = 10.00
pastas = [rigatoni, spaghetti, penne, linguini, fettuccini]

marinara = 0.00
vodka = 0.00
alfredo = 0.00
sauces = [marinara, vodka, alfredo]

meals = [pastas, sauces]
            
menu = [toppings, specials, sides, meals]

def welcomeScreen():
    welcomeMessage.show()
    menuButton.show()
    buttonBox.show()
    cartBox.hide()
def menuScreen():
    welcomeMessage.hide()
    specialMessage.hide()
    customMessage.hide()
    mealsMessage.hide()
    cartMessage.hide()
    cartBox.hide()
    
    pizzaGif.hide()
    
    customBox.hide()
    
    specialBox.hide()
    msBox.hide()
    cartBox.hide()
    
    buttonsBox.show()
    menuMessage.show()
    
    menuButton.show()
    cartButton.show()

def customScreen():
    buttonsBox.hide()
    
    welcomeMessage.hide()
    menuMessage.hide()
    specialMessage.hide()
    mealsMessage.hide()
    cartMessage.hide()
    
    pizzaGif.hide()
    
    msBox.hide()
    specialBox.hide()
    cartBox.hide()

  
    customMessage.show()
    customBox.show()
    menuButton.show()
    cartButton.show()
    
    
    
    
    
def specialScreen():
    buttonsBox.hide()
    menuMessage.hide()
    cartMessage.hide()
    
    customMessage.hide()
    mealsMessage.hide()
    
    pizzaGif.hide()
    
    customBox.hide() 
    msBox.hide()
    cartBox.hide()

    pastaMessage.hide()

    specialMessage.show()
    specialBox.show()
    menuButton.show()
    cartButton.show()    
    
def mealsScreen():
    menuMessage.hide()
    buttonsBox.hide()
    specialMessage.hide()
    customMessage.hide()
    
    
    customBox.hide()
    cartBox.hide()

    cartMessage.hide()
    pizzaGif.hide()
    
    
    #pepperoniCheck.hide()
    
    
    
    #chooseToppings.hide()
    mealsMessage.show()
    menuButton.show()
    msBox.show()
    pastaMessage.show()
    pastaChoice.show()
    specialBox.hide()
    
def cartScreen():
    pizzaGif.hide()
    buttonsBox.hide()
    menuMessage.hide()
   
    specialMessage.hide()
    customMessage.hide()
    
    msBox.hide()
    customBox.hide()
    cartMessage.hide()
    welcomeMessage.hide()
    specialBox.hide()
    mealsMessage.hide()
    pastaChoice.hide()
    
    
    
    menuButton.show()
    cartMessage.show()
    cartBox.show()

    

    
buttonBox = Box(app, width="fill", align="bottom")
cartButton = PushButton(buttonBox, command=cartScreen, text="View Cart", align="right")
menuButton = PushButton(buttonBox, command=menuScreen, text="Menu", align="left")
addtocartButton = cartButton = PushButton(buttonBox, command=addtocart, text="Add to cart", align="right")

#welcome
welcomeMessage = Text(app, text="Welcome to the Pizza Place!", size=25, font="Times New Roman", color="black", align="top")
pizzaGif = Picture(app, image="homer.gif")

#menu
menuMessage = Text(app, text="Main Menu", size=25, font="Times New Roman", color="black", align="top")
menuMessage.hide()

buttonsBox = Box(app, border=1, grid=[0,1], align="top", layout = "grid")
buttonsBox.hide()

customButton = PushButton(buttonsBox, command=customScreen, text="Customize a Pizza", align="top", width="17", grid=[0,0])
specialButton= PushButton(buttonsBox, command=specialScreen, text="Specialty Pizza", align="top", width="17", grid=[0,1])
mealsButton= PushButton(buttonsBox, command=mealsScreen, text="Meals/Sides", align="top", width="17", grid=[0,2])
buttonsBox.hide()


#custom
customMessage = Text(app, text="Customize a Pizza", size=25, font="Times New Roman", color="black", align="top", grid=[0,0])
customMessage.hide()
customBox = Box(app, border=1, grid=[1,0], align="top", layout = "grid") #width="fill", #height="fill"
customBox.hide()

sizeBox = Box(customBox, border=0, grid=[0,1], align="top", layout = "grid", width = 100, height = 200)
sizeMessage = Text(sizeBox, text = "Size", size = 15, font="Times New Roman", color="black", align="top", grid=[1,0])
sizeChoice = ButtonGroup(sizeBox, options=[ ["Small", "Small pizza"], ["Medium", "Medium pizza"],["Large", "Large pizza"]], horizontal=False, grid=[1,1], align="bottom")


toppingsBox = Box(customBox, border=0, grid=[5,1],align = "top", layout = "grid")

toppingsMessage = Text(toppingsBox, text = "Toppings", size = 15, font="Times New Roman", color="black", align="top", grid=[1,0])




cheeseCheck = CheckBox(toppingsBox, text = "Cheese", grid=[0,1], align = "left")
sauceCheck = CheckBox(toppingsBox, text = "Sauce", grid=[0,2],align = "left")
pepperoniCheck = CheckBox(toppingsBox, text = "Pepperoni", grid=[0,3], align = "left")
sausageCheck = CheckBox(toppingsBox, text = "Sausage", grid=[0,4], align = "left")
peppersCheck = CheckBox(toppingsBox, text = "Peppers", grid=[0,5], align = "left")
hamCheck = CheckBox(toppingsBox, text = "Ham", grid=[1,1], align = "left")
baconCheck = CheckBox(toppingsBox, text = "Bacon", grid=[1,2], align = "left")
pineappleCheck = CheckBox(toppingsBox, text = "Pineapple", grid=[1,3], align = "left")
mushroomCheck = CheckBox(toppingsBox, text = "Mushrooms", grid=[1,4], align = "left")
onionCheck = CheckBox(toppingsBox, text = "Onions", grid=[1,5], align = "left")
garlicCheck = CheckBox(toppingsBox, text = "Garlic",grid=[2,1], align = "left")
spinachCheck = CheckBox(toppingsBox, text = "Spinach",grid=[2,2], align = "left")
chickenCheck = CheckBox(toppingsBox, text = "Chicken", grid=[2,3], align = "left")
olivesCheck = CheckBox(toppingsBox, text = "Olives", grid=[2,4],align = "left")
anchoviesCheck = CheckBox(toppingsBox, text = "Anchovies", grid=[2,5], align = "left")

#specials
specialMessage = Text(app, text="Specialty Pizzas", size=25, font="Times New Roman", color="black", align="top")
specialMessage.hide()
specialBox = Box(app, border=0, grid=[0,1], align="top", layout = "grid")
specialBox.hide()

pizzaBox = Box(specialBox, border=1, grid=[5,1],align = "top", layout = "grid")



buffchkCheck = CheckBox(pizzaBox, text = "Buffalo Chicken Pie" , grid=[0,1], align = "left")
bbqchkCheck = CheckBox(pizzaBox, text = "Barbecue Chicken Pie" , grid=[0,2], align = "left")
hawaiianCheck = CheckBox(pizzaBox, text = "Hawaiian Pie" , grid=[0,3], align = "left")
oldfashCheck = CheckBox(pizzaBox, text = "Old Fashioned Pie" , grid=[0,4], align = "left")
meatloveCheck = CheckBox(pizzaBox, text = "Meat Lover's Pie" , grid=[0,5], align = "left")
whiteCheck = CheckBox(pizzaBox, text = "White Pie" , grid=[1,1], align = "left")
cbrCheck = CheckBox(pizzaBox, text = "Chicken Bacon Ranch Pie" , grid=[1,2], align = "left")
supremeCheck = CheckBox(pizzaBox, text = "Supreme Pie" , grid=[1,3], align = "left")
vegCheck = CheckBox(pizzaBox, text = "Veggie Pie" , grid=[1,4], align = "left")
margCheck = CheckBox(pizzaBox, text = "Margherita Pie" , grid=[1,5], align = "left")

#meals/sides
mealsMessage = Text(app, text="Meals/Sides", size=25, font="Times New Roman", color="black", align="top")
mealsMessage.hide()

msBox = Box(app, border=1, grid=[1,1], align="top", layout = "grid")
sidesBox = Box(msBox, border=0, grid=[1,0], align="top", layout = "grid")
mealsBox = Box(msBox, border=0, grid=[0,0], align="top", layout = "grid")

sidesMessage = Text(sidesBox, text = "Sides", size = 20, font="Times New Roman", color="black", align="top", grid=[0,0])

knotsCheck = CheckBox(sidesBox, text = "Garlic Knots (6)\t\t\t$2.50", grid=[0,1], align = "left")
friesCheck = CheckBox(sidesBox, text = "Fries\t\t\t\t$2.50", grid=[0,2], align = "left")
cheesefriesCheck = CheckBox(sidesBox, text = "Cheese Fries\t\t\t$3.50", grid=[0,3], align = "left")
meatballsCheck = CheckBox(sidesBox, text = "Meatballs(3)\t\t\t$3.00", grid=[0,4], align = "left")
mozzCheck = CheckBox(sidesBox, text = "Mozzarella Sticks (6)\t\t$4.50", grid=[0,5], align = "left")
wingsCheck = CheckBox(sidesBox, text = "Wings (6)\t\t\t\t$6.00", grid=[0,6], align = "left")



pastaBox = Box(mealsBox, border=0, grid=[0,1], align="top", layout = "grid")
pastaMessage = Text(mealsBox, text = "Pastas", size = 20, font="Times New Roman", color="black", align="top", grid=[0,0])
pastaMessage2 = Text(pastaBox, text = "Pasta Choice", size = 14, font="Times New Roman", color="black", align="top", grid=[0,0])
pastaChoice = ButtonGroup(pastaBox, options=[ ["Penne", "P"], ["Spaghetti", "S"],["Rigatoni", "R"], ["Linguini", "L"], ["Fettuccine", "F"]],
selected="NA", horizontal=False, grid=[0,1], align="bottom")

msBox.hide()


sauceMessage = Text(pastaBox, text = "Sauce Choice", size = 14, font="Times New Roman", color="black", align="top", grid=[0,2])
sauceChoice = ButtonGroup(pastaBox, options=(["Vodka", "V"], ["Alfredo", "A"],["Marinara", "M"]), selected="NA", horizontal=False, grid=[0,3], align="bottom")
#cart
cartMessage = Text(app, text="Cart", size=25, font="Times New Roman", color="black", align="top")
cartMessage.hide()


cartBox = Box(app, border=1, grid=[1,1],  align="top", layout = "grid")
cartBox.hide()
toppingsChosen = []


customCheckboxes = [cheeseCheck, sauceCheck, pepperoniCheck, sausageCheck, peppersCheck, hamCheck, baconCheck, pineappleCheck, mushroomCheck, onionCheck, garlicCheck, spinachCheck, chickenCheck, olivesCheck, anchoviesCheck]          

