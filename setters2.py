class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Given radius is not a valid one!!!")

my_circle = Circle(3.15)
print("My Current Radius is", my_circle.get_radius())

my_circle.set_radius(4.89)
print("My new radius is", my_circle.get_radius())

