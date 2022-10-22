class Backpack:

    def __init__(self, color):
        self.items = []
        self.color = color


my_backpack = Backpack("Green")
print(my_backpack.items)
print(my_backpack.color)

my_backpack.items = ["Books", "Water bottle", "Pen"]

print(my_backpack.items)

my_backpack.items.append("LunchBox")

print(my_backpack.items)