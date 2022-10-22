class Juice:

    price = 50

    def __init__(self, name, with_ice):
        self.name = name
        self.with_ice = with_ice

my_juice = Juice('Apple', True)
your_juice = Juice('Watermelon', False)

print(my_juice.price)
print(your_juice.price)

Juice.price = 65

print(my_juice.price)
print(your_juice.price)