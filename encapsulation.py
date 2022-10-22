class Car:

    def __init__(self, brand, year, color):
        self.brand = brand
        self.__year = year
        self.color = color

my_car = Car("Jaguar", 2020, "White")

print(my_car.__year)

# print(my_car._Car__year)