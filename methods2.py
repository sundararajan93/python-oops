class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Input is not valid item")

    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item)

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            print(f"{item} is removed")
            return 1
        else:
            print(f"{item} not in the backpack")
            return 0

    def has_item(self, item):
        return item in self._items

    def show_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)

# Creating Backpack
# saving the items to a variable
# printing the items
my_backpack = Backpack()
items = my_backpack.items
print(items)

#Adding an item to backpack and print items
my_backpack.add_item("Waterbottle")
print(items)

#Adding another item and print items
my_backpack.add_item("Books")
print(items)

#Checking if Backpack has Waterbottle
has_water = my_backpack.has_item("Waterbottle")
print(has_water)


# Un sorted list Using show_items
my_backpack.show_items()

# sorted list Using show_items
my_backpack.show_items(True)

#Removing the items from Backpack
# my_backpack.remove_item("Waterbottle")
# print(items)
# my_backpack.remove_item("Books")
# print(items)
# my_backpack.remove_item("Pencilbox")
# print(items)

#Creating the multiple items

my_backpack.add_multiple_items(["Lunch Box", "Pen", "Wallet"])
my_backpack.show_items(True)
