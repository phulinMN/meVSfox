import arcade.key
from random import randint

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y

class World(Model):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.pigs = []
        for i in range(5):
            pig = Pig(self, 75, 75 + i*100)
            self.pigs.append(pig)

        self.foxs = []
        for i in range(10):
            pig = Pig(self, 200, 200)
            self.pigs.append(pig)

class Pig(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

    #def animate(self, delta):

class Fox(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
