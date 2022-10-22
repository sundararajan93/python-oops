class Circle:

    VALID_COLORS = ("Red", "Blue", "Green")

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Invalid radius passed!!!")
    
    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print("Invalid color passed!!!")
            
    color = property(get_color, set_color)

my_circle = Circle(10, "Red")

#Radius
print("circle radius: ", my_circle.radius)
my_circle.radius = 5
print("New radius: ", my_circle.radius)

#Color
my_circle.color = "Green"
print("New color: ", my_circle.color)
