class Backpack:
    
    def __init__(self, color):
        self.items = []
        self.color = color

my_backpack = Backpack("Red")
your_backpack = Backpack("Black")

# Printing the color of both backpacks
print("Before modification")
print(my_backpack.color)
print(your_backpack.color)

# changing the color of my_backpack

my_backpack.color = "Green"

# Printing the color of both backpacks again
print("After modification")
print(my_backpack.color)
print(your_backpack.color) 