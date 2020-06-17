from guizero import App, Text, PushButton, Picture, TextBox, CheckBox, Box, ButtonGroup, info, ListBox
import json

app = App(title = "Pizza Place", bg="white")
welcomeBox = Box(app, layout="grid", border=2)
menuBox = Box(app, layout="grid", border=2)
totalPrice = []
cart = []

#clears selections on the gui
def clearAll():
    
    for i in customCheckboxes:
        if i.value == 1:
            i.value = 0
    
    #sizes
    if sizeChoice2.value == "Small":
        sizeChoice2.value = "NA"
    if sizeChoice2.value == "Medium":
        sizeChoice2.value = "NA"
    if sizeChoice2.value == "Large":
        sizeChoice2.value = "NA"
        
    
    if sizeChoice.value == "Small":
        sizeChoice.value = "NA"
    if sizeChoice.value == "Medium":
        sizeChoice.value = "NA"
    if sizeChoice.value == "Large":
        sizeChoice2.value = "NA"
        
    #pastas
    if pastaChoice.value == "Penne":
        pastaChoice.value = "NA"
    if pastaChoice.value == "Spaghetti":
        pastaChoice.value = "NA"
    if pastaChoice.value == "Rigatoni":
        pastaChoice.value = "NA"
    
  #sauce
    if sauceChoice.value == "Vodka":
        sauceChoice.value = "NA"
    if sauceChoice.value == "Marinara":
        sauceChoice.value = "NA"
    if sauceChoice.value == "Alfredo":
        sauceChoice.value = "NA"
          
    #specials
    if specialGroup.value == "Buffalo Chicken Pie":
        specialGroup.value = "NA"
    if specialGroup.value == "Barbecue Chicken Pie":
        specialGroup.value = "NA"
    if specialGroup.value == "Hawaiian Pie":
        specialGroup.value = "NA"
    if specialGroup.value == "Old Fashioned Pie":
        specialGroup.value = "NA"
    if specialGroup.value == "Meat Lover's Pie":
        specialGroup.value = "NA"
    if specialGroup.value == "White Pie":
        specialGroup.value = "NA"
    if specialGroup.value == "Chicken Bacon Ranch Pie":
        specialGroup.value = "NA"
    if specialGroup.value == "Supreme Pie":
        specialGroup.value = "NA"
    if specialGroup.value == "Veggie Pie":
        specialGroup.value = "NA"
    if specialGroup.value == "Margherita Pie":
        specialGroup.value = "NA"
            
            
    
    #sides 
    if sidesGroup.value == "Garlic Knots":
        sidesGroup.value = "NA"
    if sidesGroup.value == "Fries":
        sidesGroup.value = "NA"
    if sidesGroup.value == "Cheese Fries":
        sidesGroup.value = "NA"    
    if sidesGroup.value == "Meatballs (3)":
        sidesGroup.value = "NA"
    if sidesGroup.value == "Wings (6)":
        sidesGroup.value = "NA"
    if sidesGroup.value == "Mozzarella Sticks (6)":
        sidesGroup.value = "NA"
    


#adds selected toppings to the cart
def addtoppingsCart():
    
    toppingsChosen = []
    cart.append(sizeChoice.value)
    
    #appends selected checkboxes to list
    for i in customCheckboxes:
        if (i.value == 1):
           toppingsChosen.append(i.text)
           cart.append(i.text)
    
    
    print("Size + toppings: " + str(sizeChoice.value) + ", " + str(toppingsChosen)) #item list

    #info popup confirming items were added
    information = ""
    for i in toppingsChosen:
        if information == "":
            information = (str(i))
                
        else:
            information = information + ", " + str(i)
    info("Cart", sizeChoice.value + '\n' + (str(information)))

    
    #adds money for every topping added
           
    itemPrice=0.00 #price when nothing is selected
    for i in customCheckboxes:
        if i.value == 1:
            itemPrice=itemPrice+1.00

    
            
    
    
    #adding size price to total price of item
    if sizeChoice.value == "Small":
        itemPrice=itemPrice+6.50
        cartList.append(sizeChoice.value)

    if sizeChoice.value == "Medium":
        itemPrice=itemPrice+8.00
        cartList.append(sizeChoice.value)

    if sizeChoice.value == "Large":
        itemPrice=itemPrice+10.50
        cartList.append(sizeChoice.value)

    if sizeChoice2.value == "Small":
        itemPrice=itemPrice+6.50
        cartList.append(sizeChoice.value)

    if sizeChoice2.value == "Medium":
        itemPrice=itemPrice+8.00
        cartList.append(sizeChoice.value)

    if sizeChoice2.value == "Large":
        itemPrice=itemPrice+10.50
        cartList.append(sizeChoice.value)

    #prints items onto the gui
    cartList.append("\t" + str(toppingsChosen))
    cartList.append(" ")
    
    
    #adds item price to total price
    totalPrice.append(itemPrice)
    x=0
    for i in totalPrice:
        x=i+x
        
    #prints price on cart screen
    priceMessage = Text(cartBox, text= "", size=10, font="Times New Roman", color="black", align="top", grid=[0,0])
    priceMessage.value = "Total: $" + str(x) + "0"
       
    
    print("Item price: $" + str(itemPrice))
    print("Total price: $" + str(x))
    print("Items in cart: " + str(cart))
    
def addspecialsCart():
    specialsChosen = []
    
  #adds the special pizza size and size to cart  
    cart.append(sizeChoice2.value + " " + specialGroup.value)
    specialsChosen.append(specialGroup.value)
    
    
 #prints chosen stuff to terminal screen   
    print("Size + toppings: " + str(sizeChoice2.value) + ", " + str(specialsChosen)) #item list
  
    information = " "
    
  #info popup on spcial pie screens  
    for i in specialsChosen:
    
        if information == "":
            information = (str(i))
            
        else:
            information = information + ", " + str(i)
    info("Cart", sizeChoice2.value + (str(information)))
    itemPrice = 0.00
            
            
            
  #adds prices to total value and prints items in cart        
    if sizeChoice2.value == "Small":
         itemPrice=itemPrice+6.50
         cartList.append(sizeChoice2.value)
         
    if sizeChoice2.value == "Medium":
        itemPrice=itemPrice+8.00
        cartList.append(sizeChoice2.value)
    if sizeChoice2.value == "Large":
        itemPrice=itemPrice+10.50
        cartList.append(sizeChoice2.value)
        
    if specialGroup.value == "Buffalo Chicken Pie":
        itemPrice=itemPrice+5.00
        cartList.append(specialGroup.value)
        cartList.append(" ")
    if specialGroup.value == "Barbecue Chicken Pie":
        itemPrice=itemPrice+5.00
        cartList.append(specialGroup.value)
        cartList.append(" ")
    if specialGroup.value == "Hawaiian Pie":
        itemPrice=itemPrice+5.00
        cartList.append(specialGroup.value)
        cartList.append(" ")
    if specialGroup.value == "Old Fashioned Pie":
        itemPrice=itemPrice+5.00
        cartList.append(specialGroup.value)
        cartList.append(" ")
    if specialGroup.value == "Meat Lover's Pie":
        itemPrice=itemPrice+5.00
        cartList.append(specialGroup.value)
        cartList.append(" ")
    if specialGroup.value == "White Pie":
        itemPrice=itemPrice+5.00
        cartList.append(specialGroup.value)
        cartList.append(" ")
    if specialGroup.value == "Chicken Bacon Ranch Pie":
        itemPrice=itemPrice+5.00
        cartList.append(specialGroup.value)
        cartList.append(" ")
    if specialGroup.value == "Supreme Pie":
        itemPrice=itemPrice+5.00
        cartList.append(specialGroup.value)
        cartList.append(" ")
    if specialGroup.value == "Veggie Pie":
        itemPrice=itemPrice+5.00
        cartList.append(specialGroup.value)
        cartList.append(" ")
    if specialGroup.value == "Margherita Pie":
        itemPrice=itemPrice+5.00
        cartList.append(specialGroup.value)
        cartList.append(" ")
        
        
    
    
    
        
    #adds item price to total price
    totalPrice.append(itemPrice)
    x=0
    for i in totalPrice:
        x=i+x
        
        
    priceMessage = Text(cartBox, text= "", size=10, font="Times New Roman", color="black", align="top", grid=[0,0])

    priceMessage.value = "Total: $" + str(x) + "0"
    
    print("Item price: $" + str(itemPrice))
    print("Total price: $" + str(x))
    print("Items in cart: " + str(cart))
   
    #sides and pasta stuff sceen
   
def addsidesCart():
    
    sidesChosen = []
    pastaChosen = []
    sauceChosen = []
    
    cart.append(sidesGroup.value)
    cart.append(pastaChoice.value)
    cart.append(sauceChoice.value)
    
    pastaChosen.append(pastaChoice.value)
    sauceChosen.append(sauceChoice.value)
    sidesChosen.append(sidesGroup.value)
    #info popup
    information = ""
    for i in sidesChosen:
        if information == "":
            information = (str(i))

        
        else:
            information = information + ", " + str(i)
    info("Cart", "Added to cart")
    
    #adding toppings to total price of ITEM
    itemPrice=0.00 #price when nothing is selected
    
    #adds prices to total value        
    if sidesGroup.value == "Garlic Knots":
        itemPrice=itemPrice+2.50
        cartList.append(sidesGroup.value)
        cartList.append(" ")
    if sidesGroup.value == "Fries":
        cart.append(sidesGroup.value)
        cartList.append(" ")
        itemPrice=itemPrice +2.50
    if sidesGroup.value == "Cheese Fries":
        cartList.append(sidesGroup.value)
        cartList.append(" ")
        itemPrice=itemPrice+3.50        
    if sidesGroup.value == "Meatballs (3)":
        cartList.append(sidesGroup.value)
        cartList.append(" ")
        itemPrice=itemPrice+3.00
    if sidesGroup.value == "Wings (6)":
        cart.append(sidesGroup.value)
        cartList.append(" ")
        itemPrice=itemPrice+6.00
    if sidesGroup.value == "Mozzarella Sticks (6)":
        cartList.append(sidesGroup.value)
        cartList.append(" ")
        itemPrice=itemPrice+5.00
        
        
    if pastaChoice.value == "Penne":
        cartList.append(pastaChoice.value)
        itemPrice = itemPrice + 5.00
    if pastaChoice.value == "Spaghetti":
        cartList.append(pastaChoice.value)
        itemPrice = itemPrice + 5.00
    if pastaChoice.value == "Rigatoni":
        cartList.append(pastaChoice.value)
        itemPrice = itemPrice + 5.00

    if sauceChoice.value == "Vodka":
        cartList.append("\t Sauce: " + sauceChoice.value)
        cartList.append(" ")
        itemPrice = itemPrice + 5.00
    if sauceChoice.value == "Marinara":
        cartList.append("\t Sauce: " + sauceChoice.value)
        cartList.append(" ")
        itemPrice = itemPrice + 5.00
    if sauceChoice.value == "Alfredo":
        cartList.append("\t Sauce: " + sauceChoice.value)
        cartList.append(" ")
        itemPrice = itemPrice + 5.00
        
   #prints to terminal     

    for i in sidesChosen:
        if i in sidesChosen != "NA":
            print("Side: " + str(sidesChosen))
    for i in pastaChosen:
        if i in pastaChosen != "NA":
            print("Pasta: " + str(pastaChosen))
    for i in sauceChosen:
        if i in sauceChosen != "NA":
            print("Sauce: " + str(sauceChosen))#item list
    

    
    #adds item price to total price
    totalPrice.append(itemPrice)
    x=0
    for i in totalPrice:
        x=i+x
        
        
    priceMessage = Text(cartBox, text= "", size=10, font="Times New Roman", color="black", align="bottom", grid=[0,0])

    priceMessage.value = "Total: $" + str(x) + "0"
    
    print("Item price: $" + str(itemPrice))
    print("Total price: $" + str(x))
    print("Items in cart: " + str(cart))


    
    #shows/hides opening screen
def welcomeScreen():
    welcomeMessage.show()
    menuButton.show()
    buttonBox.show()
    cartBox.hide()
    toppingscartButton.hide()
    specialcartButton.hide()
    sidescartButton.hide()

#second screen shoes and hides
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

    toppingscartButton.hide()
    specialcartButton.hide()
    sidescartButton.hide()

#screen for customizing pizza, button group for size and checkboxes for toppings
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
    
    toppingscartButton.show()
    specialcartButton.hide()
    sidescartButton.hide()
    
    
    
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
    
    toppingscartButton.hide()
    specialcartButton.show()
    sidescartButton.hide()
    
def mealsScreen():
    menuMessage.hide()
    buttonsBox.hide()
    specialMessage.hide()
    customMessage.hide()
    
    
    customBox.hide()
    cartBox.hide()

    cartMessage.hide()
    pizzaGif.hide()
    
    
  
    mealsMessage.show()
    menuButton.show()
    msBox.show()
    pastaMessage.show()
    pastaChoice.show()
    specialBox.hide()
    
    toppingscartButton.hide()
    specialcartButton.hide()
    sidescartButton.show()
    
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
    
    toppingscartButton.hide()
    specialcartButton.hide()
    sidescartButton.hide()
    
    menuButton.show()
    cartMessage.show()
    cartBox.show()
    
       
    for i in cart:
        itemMessage.value = ""
        if i != "NA":
            itemMessage.value = str(itemMessage.value) + str("\n") + str(i)
            
    
    
    
    
# GUI  
    
    
    
buttonBox = Box(app, width="fill", align="bottom")
cartButton = PushButton(buttonBox, command=cartScreen, text="View Cart", align="right")
menuButton = PushButton(buttonBox, command=menuScreen, text="Menu", align="left")
toppingscartButton = PushButton(buttonBox, command=addtoppingsCart, text="Add to cart", align="right")
specialcartButton = PushButton(buttonBox, command=addspecialsCart, text="Add to cart", align="right")
sidescartButton = PushButton(buttonBox, command=addsidesCart, text="Add to cart", align="right")
toppingscartButton.hide()
specialcartButton.hide()
sidescartButton.hide()
clearButton = PushButton(buttonBox, command=clearAll, text="Clear Selections", align="right")
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
customBox = Box(app, border=1, grid=[1,0], align="top", layout = "grid") 
customBox.hide()

sizeBox = Box(customBox, border=0, grid=[0,1], align="top", layout = "grid", width = 100, height = 200)
sizeMessage = Text(sizeBox, text = "Size", size = 15, font="Times New Roman", color="black", align="top", grid=[1,0])
sizeChoice = ButtonGroup(sizeBox, options=["Small", "Medium", "Large", "NA"], selected="NA", horizontal=False, grid=[1,1], align="bottom")


toppingsBox = Box(customBox, border=0, grid=[5,1],align = "top", layout = "grid")

toppingsMessage = Text(toppingsBox, text = "Toppings", size = 15, font="Times New Roman", color="black", align="top", grid=[1,0])



#toppings checkboxes
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

pizzaBox = Box(specialBox, border=0, grid=[5,1],align = "top", layout = "grid")

sizeBox2 = Box(specialBox, border=0, grid=[0,1], align="top", layout = "grid", width = 100, height = 200)
sizeMessage2 = Text(sizeBox2, text = "Size", size = 15, font="Times New Roman", color="black", align="top", grid=[1,0])
sizeChoice2 = ButtonGroup(sizeBox2, options= ["Small", "Medium","Large", "NA"], selected="NA", horizontal=False, grid=[1,1], align="bottom")


specialGroup = ButtonGroup(pizzaBox, options = ["Buffalo Chicken Pie", "Barbecue Chicken Pie", "Hawaiian Pie", "Old Fashioned Pie", "Meat Lover's Pie", "White Pie", "Chicken Bacon Ranch Pie", "Supreme Pie", "Veggie Pie", "Margherita Pie", "NA"], selected = "NA", horizontal = False, grid = [1,1], align= "right")



#meals/sides
mealsMessage = Text(app, text="Meals/Sides", size=25, font="Times New Roman", color="black", align="top")
mealsMessage.hide()

msBox = Box(app, border=1, grid=[1,1], align="top", layout = "grid")
sidesBox = Box(msBox, border=0, grid=[1,0], align="top", layout = "grid")
mealsBox = Box(msBox, border=0, grid=[0,0], align="top", layout = "grid")

sidesMessage = Text(sidesBox, text = "Sides", size = 20, font="Times New Roman", color="black", align="top", grid=[0,0])

sidesGroup = ButtonGroup(sidesBox, options = [ "Garlic Knots", "Fries", "Cheese Fries", "Meatballs (3)", "Mozzarella Sticks (6)", "Wings (6)", "NA"], selected = "NA", horizontal = False, grid = [0,1], align = "right")



pastaBox = Box(mealsBox, border=0, grid=[0,1], align="top", layout = "grid")
pastaMessage = Text(mealsBox, text = "Pastas", size = 20, font="Times New Roman", color="black", align="top", grid=[0,0])
pastaMessage2 = Text(pastaBox, text = "Pasta Choice", size = 14, font="Times New Roman", color="black", align="top", grid=[0,0])
pastaChoice = ButtonGroup(pastaBox, options=["Penne", "Spaghetti", "Rigatoni",  "NA"],
selected="NA", horizontal=False, grid=[0,1], align="bottom")

msBox.hide()


sauceMessage = Text(pastaBox, text = "Sauce Choice", size = 14, font="Times New Roman", color="black", align="top", grid=[0,2])
sauceChoice = ButtonGroup(pastaBox, options=["Vodka", "Marinara", "Alfredo",  "NA"], selected="NA", horizontal=False, grid=[0,3], align="bottom")


#cart
cartMessage = Text(app, text="Cart", size=25, font="Times New Roman", color="black", align="top")
cartMessage.hide()
cartBox = Box(app, border=1, grid=[1,1],  align="top", layout = "grid")
cartBox.hide()
cartList = ListBox (cartBox, items = [], scrollbar = True, grid = [0,3], height = 250, width = 250)


#total price
itemMessage = Text(cartList, text = "", size = 10, font = "Times New Roman", color = "black", align = "top", grid=[0,1])
toppingsChosen = []
customCheckboxes = [cheeseCheck, sauceCheck, pepperoniCheck, sausageCheck, peppersCheck, hamCheck, baconCheck, pineappleCheck, mushroomCheck, onionCheck, garlicCheck, spinachCheck, chickenCheck, olivesCheck, anchoviesCheck]          



app.display()