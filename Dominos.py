class Dominos:
    
    def __init__(self, size, crust):
        self._s = size
        self._c = crust
        if size == 'small':
            self._p = 10.99
        elif self._s == 'medium':
            if self._c != 'pan':
                self._p = 12.99
            else:
                self._p = 13.99
        elif self._s == 'large':
            if self._c != 'stuffed':
                self._p = 14.99
            else:
                self._p = 15.99
        elif self._s == 'xlarge':
            self._p = 16.99
        else:
            return none
            
    def get_price(self):
        return self._p
    
    def __str__(self):
        return f"The price for {self._s} {self._c} pizza is ${self._p}."


def orderEntry():
    
    size = input("What size would you like? [small/medium/large/xlarge]")
    while size not in {'small','medium','large','xlarge'}:
        print("Invalid entry. Please try again.")
        size = input("What size would you like? [small/medium/large/xlarge]")
        
    if size == 'small':
        crust = crustEntrySmall()
    elif size == 'medium':
        crust = crustEntryMedium()
    elif size == 'large':
        crust = crustEntryLarge()
    else:
        crust = crustEntryXlarge()
        
    return [size, crust]
    
def crustEntrySmall():
    crust = input("What crust would you like? [regular/thin]")
    while crust not in {'regular','thin'}:
        print("Invalid entry. Please try again.")
        crust = input("What crust would you like? [regular/thin]")
    return crust
        
def crustEntryMedium():
    crust = input("What crust would you like? [regular/thin/pan]")
    while crust not in {'regular','thin','pan'}:
        print("Invalid entry. Please try again.")
        crust = input("What crust would you like? [regular/thin/pan]")
    return crust

def crustEntryLarge():
    crust = input("What crust would you like? [regular/thin/stuffed]")
    while crust not in {'regular','thin','stuffed'}:
        print("Invalid entry. Please try again.")
        crust = input("What crust would you like? [regular/thin/stuffed]")
    return crust

    
def crustEntryXlarge():
    crust = 'regular'
    return crust
    
def get_tax(subtotal: int):
    tax = 0.13 * subtotal
    return tax
def get_total(subtotal: int):
    return subtotal * 1.13

item_list = orderEntry()

order = Dominos(item_list[0], item_list[1])
print(order)

subtotal = 0
subtotal = format(subtotal + order.get_price(), '.2f')

print(f"Subtotal: ${subtotal}")

while True:
    order_again = input("Would you like to order something else? [yes/no]")
    while order_again not in {'yes', 'no'}:
        print("Invalid entry. Please try again.")
        order_again = input("Would you like to order something else? [yes/no]")
    if order_again == 'yes':
        item_list = orderEntry()
        order = Dominos(item_list[0], item_list[1])
        subtotal = float(subtotal) + order.get_price()
        print(order)
        format(subtotal, '.2f')
        print(f"Subtotal: ${subtotal}")
    else:
        tax = format(get_tax(subtotal), '.2f')
        total = format(get_total(subtotal), '.2f')
        print(f"Subtotal: ${subtotal}")
        print(f"Sale tax: {tax}")
        print(f"Total: ${total}")
        break
