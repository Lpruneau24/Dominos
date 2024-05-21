def getPizzaDict (filePath):
    import collections

    pizza = open(filePath, 'r')
    pizza_list = pizza.readlines()
    pizza_dict = collections.defaultdict(dict)

    for row in pizza_list[1:]: #evaluates all the lines with a variable called row (not including header line 0)
        vals = row.strip().lower().split()
        print(vals)
        if vals[0] in {'small', 'medium', 'large', 'xlarge'}:
            pizza_dict[vals[0]][vals[1]] = vals[2]

    pizza.close
    return pizza_dict
def orderEntry():

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

    price = pizza_dict[size][crust]
        
    return [size, crust, price]

class Tax:
    def __init__(self, subtotal, taxRate = 0.13):
        self.subtotal = subtotal
        self.taxRate = taxRate
    def get_tax(self):
        salesTax = float(subtotal) * float(self.taxRate)
        return salesTax
    def get_total(self):
        total = float(subtotal) + float(subtotal) * float(self.taxRate)
        return total

pizzaFile = "D:\Leandre\Apps\GitHub\Repository\Dominos\Pizza.txt" # input("Paste the file path for pizzas please.")
pizza_dict = getPizzaDict(pizzaFile)

small_keys = pizza_dict['small'].keys()
medium_keys = pizza_dict['medium'].keys()
large_keys = pizza_dict['large'].keys()
xlarge_keys = pizza_dict['xlarge'].keys()

taxRate = 0.13 # input("What is the tax rate?")

item_list = orderEntry()

subtotal = 0
subtotal = subtotal + float(item_list[2])
print(f"Your subtotal is ${subtotal}")

while True:
    order_again = input("Would you like to order something else? [yes/no]")
    while order_again not in {'yes', 'no'}:
        print("Invalid entry. Please try again.")
        order_again = input("Would you like to order something else? [yes/no]")
    if order_again == 'yes':
        item_list = orderEntry()
        subtotal = float(subtotal) + float(item_list[2])
        subtotal = format(subtotal, '.2f')
        print(f"Subtotal: ${subtotal}")
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
