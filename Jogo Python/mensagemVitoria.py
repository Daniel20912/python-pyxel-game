from mensagem import Mensagem
import pyxel


class MensagemVitoria(Mensagem):
    def __init__(self):
        super().__init__("You Win!")

    def draw(self, x, y):
        super().draw(x, y, pyxel.COLOR_GREEN)
