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

item_list = orderEntry()

order = Dominos(item_list[0], item_list[1])
print(order)

total = 0
total = total + order.get_price()

print(f"Your total is ${total}")

while True:
    order_again = input("Would you like to order something else? [yes/no]")
    while order_again not in {'yes', 'no'}:
		print("Invalid entry. Please try again.")
		order_again = input("Would you like to order something else? [yes/no]")
    if order_again == 'yes':
        item_list = orderEntry()
        order = Dominos(item_list[0], item_list[1])
        total = total + order.get_price()
        print(order)
        format(total, '.2f')
        print(f"Your total is ${total}")
    else:
		format(total, '.2f') # some cases the program stopped rounding for whatever reason so I added one in the end just in case
        print(f"Your final total is ${total}")
        break