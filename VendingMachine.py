# =======================================================
# |     Cap'n Crunch Super Vending Machine Simulator    |
# |-----------------------------------------------------|
# |  ⭐️⭐️⭐️⭐️⭐️ Zagat reviewed, A++ rating from the BBB,  |   
# |      winner of every single JD Power Award          |
# |                                                     |
# | "revolutionary, life changing" -The New York Times  |
# | "my mom uses it all the time"  -Jimmy from IHOP     |
# | "no, you can't have a refund"  -The Vending Machine |
# =======================================================


# ______________ VARIABLES 'N SHIT ______________________

#idk man, i just work here
query = ""

#as empty as the history books in <insert country here>
history_list = []

#inventory, outventory, whatever, it's all the same
inventory_list = []

#started from the bottom now we're... still at the bottom
global machine_balance
machine_balance = 0.00

#welcome to your first class students, today we're going to learn about capitalism
#get it? because it's a vending machine? and it's a class? and it's a joke?
class item:
    def __init__(self, name, quantity: int, price: float, id: int):
        self.name = name
        self.quantity = int(quantity)
        self.price = float(price)
        self.id = int(id)


# __________________ FUNCTIONS ___________________________

def balance():
    print("Balance: $", "%0.2f" % machine_balance, "\n\n")
    
def history():
    print("History: \n\n")
    for i in history_list:
        print(i)
    print("\n\n")
    
def inventory():
    print("Inventory: \n\n")
    for i in inventory_list:
        print(i.name + " (x" + str(i.quantity) + "), id: " + str(i.id) + "\n")
    print("\n\n")

#addItem doesn't do any input validation so things can go wrong:
    #negative quanitities are possible
    #it doesn't check if an item already exists, so you can have multiple items with the same name
        #even if they have the same name, they might have different ids or prices
        #or maybe they're just the same item but you're cheap and just trying to get a discount
        #I'm a vending machine, Jim, not a detective - I don't judge.
def addItem(name, quantity, price):
    inventory_list.append(item(name, quantity, price.strip("$"), len(inventory_list)))

def buyItem(name, dollars, quarters, dimes, nickels, pennies):
    #converts the money to a float
    money = float(dollars) * 1.00 + float(quarters) * 0.25 + float(dimes) * 0.10 + float(nickels) * 0.05 + float(pennies) * 0.01
    
    #finds the item in the inventory
    for i in inventory_list:
        if i.name == name:
            if money > i.price:
                #checks if the item is in stock
                if i.quantity > 0:
                    #removes the item from the inventory
                    i.quantity -= 1
                    
                    #removes the money from the machine
                    global machine_balance
                    machine_balance -= i.price
                    
                    print("Transaction successful!\n")
                else:
                    print("Item out of stock.\n\n")
            else:
               print("Not enough money, please insert more money.\n\n")


# _________________ MAIN FUNCTION ________________________

print("===============================")
print("Welcome to the vending machine!\n")

while True:
    #get command and save it to history
    query = input("Please enter a command ('help' for list): ")
    history_list.append(query)
    
    # print("query: " + query + "\n")
    #evaluate command and execute function
    if(query == 'help'):
        print("Commands:\n")
        print("balance - displays the current balance")
        print("inventory - displays the current inventory")
        print("add item <str> <int> $<float> - adds an item to the inventory")
        print("buy item <str> {5} <int> - buys an item from the inventory")
        print("help - displays this menu")
        print("exit - exits the program")
    elif(query == 'balance'):
        balance()
    elif(query == 'history'):
        history()
    elif(query == 'inventory'):
        inventory()
    elif(query.startswith("add item")):
        addItem(query.split(' ')[2], query.split(' ')[3], query.split(' ')[4])
    elif(query.startswith("buy item")):  #TODO needs full input validation, shouldn't just 'start with'
        buyItem(query.split(' ')[2], query.split(' ')[3], query.split(' ')[4], query.split(' ')[5], query.split(' ')[6], query.split(' ')[7])
    elif(query == 'exit'):
        break