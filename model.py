import arcade.key
from random import randint

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.pigs = []
        for i in range(5):
            pig = Pig(self, 75, 75 + i*100)
            self.pigs.append(pig)

        self.foxs = []
        for j in range(10):
            fox = Fox(self, 775 + j*300, 75 + j*100)
            self.foxs.append(fox)

    def animate(self, delta):
        for fox in self.foxs:
            fox.x -= 2

class Pig(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class Fox(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
