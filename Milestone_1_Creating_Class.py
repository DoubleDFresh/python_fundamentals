"""Objective: Create a class from components using the type() function.
1. Create my own version of the Price class.  Ensure the get_price() method works.
2. Create (2) functions [function__init__ & function_get_price] that take the same
    parameters as the methods in the Price class.
3. Create a dict (namespace) with 2 keys, "__init__" & "get_price", with the values
    being the names (no params, parens, or quotes) of the functions created in step 2.
4. Create a class with type() --> Price2 = type('Price2', (), namespace)
    a. 1st param is the class name which should match the name on left side of the =.
    b. 2nd param (), is the list of superclasses
    c. 3rd param namespace is the dict we created in step 3
5. Test to see if there are any diffs btw the 1st class defined & the class created using type()
"""


class Price:
    def __init__(self, part_number, price):
        self.price = price
        self.part_number = part_number

    def get_price(self):
        return self.price


def function__init__(self, part_number, price):
    self.price = price
    self.part_number = part_number


def function_get_price(self):
    return self.price


namespace = {"__init__": function__init__, "get_price": function_get_price}

Price2 = type('Price2', (), namespace)

# Create a Price object named item
item = Price(123, 4.56)

# Create a Price2 object named new item
new_item = Price2(123, 4.56)

# Test to see if there is a diff between item and new_item
# Test1: are item and new_item instances of their objects?
print(type(item))
print(type(new_item))

# Test2: are both prices the same (same results from method)
print()
print()
print('Do both prices match from the 2 objects?')
print(item.get_price() == new_item.get_price())


# Test3:confirm both are objects
print()
print()
print('Test 3 - are both objects?')
print(item)
print(new_item)
