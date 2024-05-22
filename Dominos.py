import collections

    pizza_rows = open(filePath, 'r')
    pizza_list = pizza_rows.readlines()
    pizza_dict = collections.defaultdict(dict)

    print("This is our menu:")

    for row in pizza_list[1:]: # evaluates all the lines with a variable called row (not including header line 0)
        vals = row.strip().lower().split()
        print(vals[0:3])
        if vals[0] in {'small', 'medium', 'large', 'xlarge'}:
            pizza_dict[vals[0]][vals[1]] = [vals[2], vals[3]]

    print()

    pizza_rows.close
    return pizza_dict

def getToppingDict(filePath):    # This function will ask the user what kind of pizza they want and using the dictionary above, return a list of 3 items being size, crust and price. This will be called many times.

    topping_dict = {}
    topping = open(filePath, 'r')
    topping_list = topping.readlines()

    print("These are our toppings:")
    print("-------------------------")

    for row in topping_list[1:]:
        vals = row.strip().lower().split(':')
        print(vals[0])
        topping_dict[vals[0]] = float(vals[1])

    print("-------------------------")
    print()

    topping.close
    return topping_dict

def orderEntry() ->list:

    size = input("What size would you like? [small/medium/large/xlarge]")
    while size not in {'small','medium','large','xlarge'}:
        print("Invalid entry. Please try again.")
        size = input("What size would you like? [small/medium/large/xlarge]")

    def crustEntrySmall():
        crust = input("What crust would you like?")
        while crust not in small_keys:
            print("Invalid entry. Please try again.")
            crust = input("What crust would you like?")
        return crust
    def crustEntryMedium():
        crust = input("What crust would you like?")
        while crust not in medium_keys:
            print("Invalid entry. Please try again.")
            crust = input("What crust would you like?")
        return crust
    def crustEntryLarge():
        crust = input("What crust would you like? [regular/thin/stuffed]")
        while crust not in large_keys:
            print("Invalid entry. Please try again.")
            crust = input("What crust would you like? [regular/thin/stuffed]")
        return crust
    def crustEntryXLarge():
        crust = input("What crust would you like?")
        while crust not in xlarge_keys:
            print("Invalid entry. Please try again.")
            crust = input("What crust would you like?")
        return crust

    if size == 'small':
        crust = crustEntrySmall()
    elif size == 'medium':
        crust = crustEntryMedium()
    elif size == 'large':
        crust = crustEntryLarge()
    else:
        crust = crustEntryXLarge()

    price = float(pizza_dict[size][crust][0])
    multiplier = float(pizza_dict[size][crust][1])
    
    topping_selected = input("Would you like some toppings on that pizza? [yes/no]")
    while topping_selected not in {'yes', 'no'}:
        print("Invalid entry. Please try again.")
        topping_selected = input("Would you like some toppings on that pizza? [yes/no]")
    if topping_selected == 'yes':
        toppings_selected = toppingEntry()
    else:
        pass

    return [size, crust, price, multiplier, toppings_selected]

def toppingEntry():    #
    toppings_selected = {}
    while True:
        for n in ['first', 'second', 'third', 'fourth', 'fifth']:
            topping_selected = whichTopping(n)
            if topping_selected == 'nevermind':
                break

            elif n == 'eight':    # Prevents user from being asked if they want another topping at the last instance of the loop.
                break
            elif topping_selected in toppings_selected:    # changes the value for a topping if such topping has already been selected once in the past.
                toppings_selected[topping_selected] = toppings_selected[topping_selected] + float(topping_dict[topping_selected])
                continueToppingEntry = input("Do you want another topping? [yes/no]")
                while continueToppingEntry not in {'yes', 'no'}:
                    print("Invalid entry. Please try again.")
                    continueToppingEntry = input("Do you want another topping? [yes/no]")
                if continueToppingEntry == 'yes':
                    continue
                else:
                    break
            else:
                toppings_selected[topping_selected] = float(topping_dict[topping_selected])
                continueToppingEntry = input("Do you want another topping? [yes/no]")
                while continueToppingEntry not in {'yes', 'no'}:
                    print("Invalid entry. Please try again.")
                    continueToppingEntry = input("Do you want another topping? [yes/no]")
                if continueToppingEntry == 'yes':
                    continue
                else:
                    break
        return toppings_selected

    def whichTopping(n):    #    n wil have value from 'frist', 'second'... 'fifth' for each time a customer orders a topping. This will return which topping the customer wants.
        whichTopping = input(f"What is the {n} topping you would like? ['topping'/nevermind]")
        while whichTopping not in topping_dict.keys():
            if whichTopping == 'nevermind':
                return 'nevermind'
            else:
                print("Invalid entry. Please try again.")
                whichTopping = input(f"What is the {n} topping you would like?")
        
    return whichTopping

def toppingTotal(toppings_selected: dict, topping_multiplier: float):    # returns what the customer pays based on the pizza size
    topping_total = 0
    for topping in toppings_selected.keys():
        topping_total = topping_total + topping_multiplier * toppings_selected[topping]
    return topping_total


class Tax:    # The class created here will calculate taxes. I have set the default taxRate to 0.13 which doesn't matter because it is called as a parameter anyway.
    def __init__(self, subtotal, taxRate = 0.13):
        self.subtotal = subtotal
        self.taxRate = taxRate
    def get_tax(self):    # This will return the sales tax of the pizza entered in orderEntry()
        salesTax = float(subtotal) * float(self.taxRate)
        return salesTax
    def get_total(self):    # This will return the after tax total of the pizza entered in orderEntry()
        total = float(subtotal) + float(subtotal) * float(self.taxRate)
        return total

# This section will ask the user where they keep the files needed for the program.
pizzaFile = input("Paste the file path for pizzas please.")
toppingFile = input("Paste the file path for toppings please."")
pizza_dict = getPizzaDict(pizzaFile)
topping_dict = getToppingDict(toppingFile)

# In this section, I'm pullig all the different crust types for each size
small_keys = pizza_dict['small'].keys()
medium_keys = pizza_dict['medium'].keys()
large_keys = pizza_dict['large'].keys()
xlarge_keys = pizza_dict['xlarge'].keys()

taxRate = input("What is the tax rate?")

# This section calls the main functions which some will call nested functions and do most of the work
order_entry = orderEntry()
pizza_total = order_entry[2]
pizza_multiplier = order_entry[3]
toppings_selected = order_entry[4]
topping_total = toppingTotal(toppings_selected, pizza_multiplier)

# Adds all the totals and roudns up to two decimals
subtotal = 0
subtotal = float(subtotal) + pizza_total + topping_total
subtotal = format(subtotal, '.2f')
print(f"Your subtotal is ${subtotal}")

# This will loop the ordering process for as many items as the customer wants. Subtotal is an accumulator value and taxes are done on that value once customer is done ordering new items.
while True:
    order_again = input("Would you like to order something else? [yes/no]")
    while order_again not in {'yes', 'no'}:
        print("Invalid entry. Please try again.")
        order_again = input("Would you like to order something else? [yes/no]")
    if order_again == 'yes':
        order_entry = orderEntry()
        pizza_total = order_entry[2]
        pizza_multiplier = order_entry[3]
        toppings_selected = order_entry[4]

        
        topping_total = toppingTotal(toppings_selected, pizza_multiplier)

        subtotal = float(subtotal)
        subtotal = subtotal + pizza_total + topping_total
        subtotal = format(subtotal, '.2f')
        print(f"Your subtotal is ${subtotal}")

    else:
        tax = Tax(subtotal, taxRate).get_tax()
        tax = format(tax, '.2f')
        total = Tax(subtotal).get_total()
        total = format(total, '.2f')
        print()
        print()
        print('-----------------')
        print(f"Subtotal: ${subtotal}")
        print(f"Sale tax: {tax}")
        print(f"Total: ${total}")
        print('-----------------')
        break
