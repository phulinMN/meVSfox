import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.pigs = []
        i = 0
        for i in range(5):
            self.pigs.append(arcade.Sprite('images/pig.png', scale = 0.18))
            self.pigs[i].set_position(75, 75 + i*100)

        self.foxs = []
        j = 0
        for j in range(2):
            self.foxs.append(arcade.Sprite('images/fox.png', scale = 0.5))
            self.foxs[j].set_position(475 + j*300, 75 + j*100)

    def on_draw(self):
        arcade.start_render()
        for pig in self.pigs:
            pig.draw()

        for fox in self.foxs:
            fox.draw()


    def animate(self, delta):
        fox = self.foxs
        for fox in self.foxs:
            fox.set_position(fox.center_x - 2, fox.center_y)
        # fox[0].set_position(fox[0].center_x - 2, fox[0].center_y)
        # fox[1].set_position(fox[1].center_x - 2, fox[1].center_y)

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
