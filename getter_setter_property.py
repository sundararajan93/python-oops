class BouncyBall:
    
    def __init__(self, price, size, brand):
        self._price = price 
        self._size = size 
        self._brand = brand
    
    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if isinstance(new_price, float):
            self._price = new_price
        else:
            print("Invalid price!!!")

    price = property(get_price, set_price)

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if isinstance(new_size, int) and 0 < new_size <= 10:
            self._size = new_size
        else:
            print("Invalid Size!!!")

    size = property(get_size, set_size)

    def get_brand(self):
        return self._brand

    def set_brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand.isalpha():
            self._brand = new_brand
        else:
            print("Invalid Brand!!!")

    brand = property(get_brand, set_brand)

my_toy = BouncyBall(3.89, 4, "Nike")

print("Price:",my_toy.price)
print("Size:",my_toy.size)
print("Brand:",my_toy.brand)

#Modification
my_toy.price = 8
my_toy.size = 7.1
my_toy.brand = "Adidas"

print("After modification")

print("Price:",my_toy.price)
print("Size:",my_toy.size)
print("Brand:",my_toy.brand)