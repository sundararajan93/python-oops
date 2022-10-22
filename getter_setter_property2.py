class BouncyBall:
    
    def __init__(self, price, size, brand):
        self._price = price 
        self._size = size 
        self._brand = brand
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float):
            self._price = new_price
        else:
            print("Invalid price!!!")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if isinstance(new_size, int) and 0 < new_size <= 10:
            self._size = new_size
        else:
            print("Invalid Size!!!")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand.isalpha():
            self._brand = new_brand
        else:
            print("Invalid Brand!!!")

my_toy = BouncyBall(3.89, 4, "Nike")

print("Price:",my_toy.price)
print("Size:",my_toy.size)
print("Brand:",my_toy.brand)

#Modification
my_toy.price = 8.2
my_toy.size = 7
my_toy.brand = "Adidas"

print("After modification")

print("Price:",my_toy.price)
print("Size:",my_toy.size)
print("Brand:",my_toy.brand)