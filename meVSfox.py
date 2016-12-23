import arcade
from model import Pig,World,Bullet

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
        self.endgame = arcade.Sprite('images/black.png', scale=2)
        self.hunter_sprite = ModelSprite('images/hunter.png', scale=0.4, model=self.world.hunter)
        self.bullet_sprite = []
        self.pigs_sprites = []
        for pig in self.world.pigs:
            self.pigs_sprites.append(ModelSprite('images/pig.png', scale = 0.18, model=pig))

        self.foxs_sprites = []
        for fox in self.world.foxs:
            self.foxs_sprites.append(ModelSprite('images/fox.png', scale = 0.36, model=fox))

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_draw(self):
        self.bullet_sprite.clear()
        for i in range(len(self.world.bullets)):
            if self.world.status_bullet[i] == 1:
                self.bullet_sprite.append(ModelSprite("images/bullet.png", scale=0.02, model=self.world.bullets[i]))

        arcade.start_render()
        i = 0
        for sprite in self.pigs_sprites:
            if self.world.status_pig[i] == 1:
                sprite.draw()
            i += 1

        j = 0
        for sprite in self.foxs_sprites:
            if self.world.status_fox[j] == 1:
                sprite.draw()
            j += 1

        self.hunter_sprite.draw()
        for sprite in self.bullet_sprite:
            sprite.draw()

        arcade.draw_text(str(self.world.score),
                         self.width - 50, self.height - 30,
                         arcade.color.WHITE, 20)
        if self.world.heart == 0:
            self.endgame.draw()
            arcade.draw_text("END GAME", 200, 300, arcade.color.WHITE, 50)

    def animate(self, delta):
        if self.world.heart != 0:
            self.world.animate(delta)


if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
