import pyxel


class ContagemRegressiva:
    def __init__(self, initial_value):
        if not isinstance(initial_value, int) or initial_value < 0:
            raise ValueError(
                "O valor inicial da contagem regressiva deve ser um número inteiro e positivo."
            )
        self.value = initial_value

    def decrementar(self):
        self.value -= 1

    def get_valor(self):
        return self.value

    def is_zero(self):
        return self.value <= 0

    def draw(self):
        countdown_text = str(self.value // 30)
        countdown_width = len(countdown_text) * 4
        pyxel.rect(10 - countdown_width // 2, 10, countdown_width, 7, pyxel.COLOR_BLACK)
        pyxel.text(10 - countdown_width // 2, 10, countdown_text, pyxel.COLOR_WHITE)

        img_x = 16 - countdown_width // 2
        img_y = 9
        pyxel.blt(img_x, img_y, 1, 24, 0, 8, 8, pyxel.COLOR_BLACK)
