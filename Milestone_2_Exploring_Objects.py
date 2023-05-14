"""Objective: Explore classes, instances of classes, and how methods can be
added to a class after it has been defined.
1. Create a version of the Price class
2. Create an instance of the class called item_price.
3. Use the dir() function and the .__dict__ attr to explore the instance and the
class.  What is the difference between dir() and .__dict__?
4. Create 2 standalone functions we will attach to our class.  For this to work,
each function needs to get an instance of Price as its first parameter.  
    4a. Create a function set_discount(item_price, percent_off) that adds
    a percent_off attribute to a Price object.
    4b. Next, create a get_discount_price(item_price) function that calculates
    the discount price using the price and percent_off attributes of the
    item_price object.
5. Attach both functions to the class to see if they work as instance methods
Price.set_discount = set_discount
6. If you add a function to an instance instead of a class, what happens? Does it
work at all?  How is its behavior different?


"""


class Price:
    def __init__(self, part_number, price):
        self.price = price
        self.part_number = part_number

    def get_price(self):
        return self.price


# 2 Create an instance of Price named item_class & item_class_add_function to use in Step 6
item_class = Price('A123', 1.23)
item_class_add_function = Price('C789', 7.89)


# 3 Use dir() and .__dict__ to explore the instance and the class
listA = dir(item_class)
listB = dir(Price)
print(f'The length of item_class is {len(listA)}')
print(f'The length of Price is {len(listB)}')
# 3a Find the difference between dir for item_class and price
print(
    f'The attributes only in item_class are {set(listA).symmetric_difference(set(listB))}')
print('All other elements beyond "price" and "class" are in the Price class')

# Conclusion: data attributes only exist after they are instantiated - not in the class
# 3b Find the difference between Price.__dict__ and item_class.__dict__
print(), print()
print(f'The output of item_class.__dict__ is {item_class.__dict__}')
print(), print()
print(f'The output of Price.__dict__ is {Price.__dict__}')
print(), print()
# 3b Conclusion:
# a. The output of the instance.__dict__ only includes the attribute name and value
# b. The output of the class.__dict__ includes the method and attribute names.
# c. The difference between dir and dict of instances is: dir only has method name
#     & instance name....instance.__dict__ has object name and values - no method info


# 4. Create 2 standalone functions that we will attach to the class

def set_discount(item_price, percent_off):
    item_price.percent_off = percent_off


def get_discount_price(item_price):
    return item_price.get_price() * (1 - item_price.percent_off)

# 5. Attach both functions to the class & see if they work as instance methods


Price.set_discount = set_discount
Price.get_discount_price = get_discount_price

#   5a. Do instances of the original class (item_class) work differently than
#   methods defined in step 1?
new_item_class = Price('B456', 4.56)

print(f'Can I get_price of item_class? {item_class.get_price()}')
print(f'Yes - first set the discount')
item_class.set_discount(0.1)
print(f'I then get this correct response - {item_class.get_discount_price()}')
print(), print()

#   Now try get_price and get_discount_price with a new instance of Price


print(f'Can I get_price of new_item_class? Yes. {new_item_class.get_price()}')

new_item_class.set_discount(0.1)
print(
    f'Can I get_discount_price of new_item_class? Yes. {new_item_class.get_discount_price()}')


#   5a Conclusion:  the monkey patch methods and attributes are only available in instances
#   created after the monkey patch was applied to the class.

#   6a. Can you add a function to an instance instead of a class?  Use item_class_add_function instance
# Let's add a tax to the price
def set_tax(PriceInstance, tax):
    PriceInstance.set_tax = tax


def get_taxed_price(PriceInstance):
    return PriceInstance.get_price() * (1 + PriceInstance.set_tax)


tax_item_class = Price('D987', 9.87)
tax_item_class.set_discount(0.1)
print(f'Price before tax {tax_item_class.get_price()}')
set_tax(tax_item_class, 0.2)
print(f'Price after tax is {get_taxed_price(tax_item_class)}')
print(), print()
# I can set_tax on tax_item_class...can I do so on item_class?
# no - this generates an AttributeError --> item_class.set_tax(0.2)
print(), print()
print(f'item_class does not have set_tax {dir(item_class)}')
#  Now add the set_discount and get_discount_price methods to that instance

# Conclusion - adding a function to an instance limits it to the instance.
# the function is not available in other instances.
