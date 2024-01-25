from mensagem import Mensagem
import pyxel


class MensagemGameOver(Mensagem):
    def __init__(self):
        super().__init__("Game Over")

    def draw(self, x, y):
        super().draw(x, y, pyxel.COLOR_RED)
