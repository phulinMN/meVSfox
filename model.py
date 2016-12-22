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
        self.speed = 1
        self.width = width
        self.height = height
        self.score = 0
        self.hunter = Hunter(self, 175, 75)
        self.status_pig = [1, 1, 1, 1, 1]
        self.status_fox = []
        self.status_bullet = []
        self.bullets = []
        self.pigs = []

        for i in range(5):
            pig = Pig(self, 75, 75 + i*100)
            self.pigs.append(pig)

        self.foxs = []
        for j in range(5):
            fox = Fox(self, 775 + j*300, 75 + j*100)
            self.status_fox.append(1)
            self.foxs.append(fox)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.hunter.move_up()
        if key == arcade.key.DOWN:
            self.hunter.move_down()
        if key == arcade.key.SPACE:
            self.bullet = Bullet(self, self.hunter.x + 100, self.hunter.y)
            self.status_bullet.append(1)
            self.bullets.append(self.bullet)

    def animate(self, delta):
        n = 0
        for fox in self.foxs:
            fox.animate(delta, self.speed)
            for i in range(len(self.pigs)):
                if fox.hit(self.pigs[i], 1) and self.status_fox[i] == 1:
                    self.status_pig[i] = 0
                    self.score -= 1
                    break

            for j in range(len(self.bullets)):
                self.bullets[j].animate(delta)
                if fox.case() == self.bullets[j].case() and self.status_fox[n] == 1:
                    if self.bullets[j].hit(fox, 10):
                        self.status_bullet[j] = 0
                        self.status_fox[n] = 0
                        self.score += 1
                        break
                    if self.bullets[j].x > 800:
                        self.status_bullet[j] = 0
            if fox.x < 0:
                self.status_fox[n] = 1
                fox.x = 800
            n += 1
        # self.speed += 1

class Pig(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)

class Fox(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)

    def case(self):
        if self.y == 75:
            n = 0
        if self.y == 175:
            n = 1
        if self.y == 175:
            n = 2
        if self.y == 275:
            n = 3
        if self.y == 375:
            n = 4

    def animate(self, delta, speed):
        self.x -= 2 + speed

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
        self.x += 2

    def case(self):
        if self.y == 75:
            n = 0
        if self.y == 175:
            n = 1
        if self.y == 175:
            n = 2
        if self.y == 275:
            n = 3
        if self.y == 375:
            n = 4
