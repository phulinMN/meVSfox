import arcade.key
import arcade
from random import randint, random
class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score = 0
        self.hunter = Hunter(self, 175, 75)
        self.status_pig = [1, 1, 1, 1, 1]
        self.status_fox = [1, 1, 1, 1, 1]
        self.bullets = []
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
        if key == arcade.key.SPACE:
            bullet = Bullet(self, self.hunter.x + 100, self.hunter.y)
            self.bullets.append(bullet)

    def animate(self, delta):
        n = 1
        for fox in self.foxs:
            fox.animate(delta)
            for i in range(len(self.pigs)):
                if fox.hit(self.pigs[i], 1) and self.status_fox[i] == 1:
                    self.status_pig[i] = 0
                    self.score -= 1
                    break

        for bullet in self.bullets:
            bullet.animate(delta)
            for i in range(len(self.foxs)):
                if bullet.hit(self.foxs[i], 10) and self.status_fox[i] == 1:
                    print(i)
                    self.status_fox[i] = 0
                    self.score += 1
                    break

class Pig(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)

class Fox(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)

    def random_location(self):
        self.x = randint(0, self.world.width - 1)
        self.y = randint(0, self.world.height - 1)

    def animate(self, delta):
        self.x -= 2

class Hunter(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)

    def move_up(self):
        if self.y < 475:
            self.y += 100

    def move_down(self):
        if self.y > 75:
            self.y -= 100


class Bullet(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)

    def animate(self, delta):
        self.x += 4
