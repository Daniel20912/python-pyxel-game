import pyxel


class Mensagem:
    def __init__(self, text):
        self.text = text

    def draw(self, x, y, color):
        text_width = len(self.text) * 4
        x_position = x - text_width // 2
        pyxel.text(x_position, y, self.text, pyxel.COLOR_WHITE)
        pyxel.text(x_position, y + 1, self.text, color)
