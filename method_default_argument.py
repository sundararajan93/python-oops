class Player:

    def __init__(self, name, posx, posy, negx, negy):
        self.name = name
        self.posx = posx
        self.posy = posy
            
    def position(self):
        print(self.name, self.posx, self.posy)

    def move_up(self, steps=5):
        if isinstance(steps, int):
            self.posy += steps
        
    def move_down(self, steps=5):
        if isinstance(steps, int):
            self.posy -= steps

    def move_left(self, steps=5):
        if isinstance(steps, int):
            self.posx -= steps

    def move_right(self, steps=5):
        if isinstance(steps, int):
            self.posx += steps

# Create a player with initial position

player_one = Player("Sundar", 20, 40, 70, 35)

player_one.position()

player_one.move_right()
player_one.position()

player_one.move_left()
player_one.position()

player_one.move_up()
player_one.position()

player_one.move_down()
player_one.position()

