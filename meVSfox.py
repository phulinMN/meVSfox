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

        self.foxs_sprites = []
        for fox in self.world.foxs:
            self.foxs_sprites.append(ModelSprite('images/fox.png', scale = 0.5, model=fox))

    def on_draw(self):
        arcade.start_render()
        i = 0
        for sprite in self.pigs_sprites:
            if self.world.status_pig[i] == 1:
                sprite.draw()
            i += 1

        for sprite in self.foxs_sprites:
            sprite.draw()

    def animate(self, delta):
        self.world.animate(delta)

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
