import arcade.key
from random import randint, random

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.hunter = Hunter(self, 175, 75)
        self.status_pig = [1, 1, 1, 1, 1]
        self.pigs = []
        for i in range(5):
            pig = Pig(self, 75, 75 + i*100)
            self.pigs.append(pig)

        self.foxs = []
        for j in range(5):
            fox = Fox(self, 775 + j*300, 75 + j*100)
            self.foxs.append(fox)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.hunter.move_up()
        if key == arcade.key.DOWN:
            self.hunter.move_down()

    def animate(self, delta):
        for fox in self.foxs:
            fox.animate(delta)
            for i in range(len(self.pigs)):
                if fox.hit(self.pigs[i], 10):
                    self.status_pig[i] = 0
                    break

        # for i in range(5):
        #     print(str(i) + ' : ' + str(self.die_pig[i]))

class Pig(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class Fox(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

    def animate(self, delta):
        self.x -= 2

class Hunter(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

    def move_up(self):
        if self.y < 475:
            self.y += 100

    def move_down(self):
        if self.y > 75:
            self.y -= 100
