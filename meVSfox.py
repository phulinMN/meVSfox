import arcade
from model import Pig,World

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(width, height)

        self.pigs_sprites = []
        for pig in self.world.pigs:
            self.pigs_sprites.append(ModelSprite('images/pig.png', scale = 0.18, model=pig))

        self.foxs = []
        j = 0
        for j in range(2):
            self.foxs.append(arcade.Sprite('images/fox.png', scale = 0.5))
            self.foxs[j].set_position(775 + j*300, 75 + j*100)


    def on_draw(self):
        arcade.start_render()
        for sprite in self.pigs_sprites:
            sprite.draw()
        # for pig in self.pigs:
        #     pig.draw()

        for fox in self.foxs:
            fox.draw()

    def animate(self, delta):
        fox = self.foxs
        for fox in self.foxs:
            fox.set_position(fox.center_x - 2, fox.center_y)

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
