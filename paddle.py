from pgzero.actor import Actor


class Paddle:
    def __init__(self, x, y, sprite, width):
        self.actor = Actor(sprite, (x, y))
        self.sprite = sprite
        self.width = width

    def draw(self):
        self.actor.draw()

    def update_left(self):
        if self.actor.x - 4 > 0 + self.width:
            self.actor.x = self.actor.x - 4

    def update_right(self):
        if self.actor.x + 4 < 640 - self.width:
            self.actor.x = self.actor.x + 4

    def long_paddle(self):
        self.sprite = "long_paddle.png"
