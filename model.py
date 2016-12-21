import arcade.key
from random import randint

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.pig = Pig(self, 75, 75)

    def animate(self, delta):
        self.pig.animate(delta)

class Pig:
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.direction = Pig.DIR_VERTICAL
