from decimal import BasicContext
from re import U


class Bacteria:
    
    def __init__(self, x, y, size, shape, weakness):
        self.x = x
        self.y = y
        self.size = size
        self.shape = shape
        self.weakness = weakness

# Create 3 instances

bacilli = Bacteria(150, 200, 3, "rod", "UV Radiation")
cocci = Bacteria(589, 10, 10, "sphere", "Heat")
spirilli = Bacteria(43, 800, "spiral", "disinfectant")

