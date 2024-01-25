import pyxel


class Mouse:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self):
        self.x = pyxel.mouse_x
        self.y = pyxel.mouse_y

    def draw(self):
        pyxel.blt(self.x, self.y, 2, 0, 0, 8, 8, pyxel.COLOR_BLACK)

