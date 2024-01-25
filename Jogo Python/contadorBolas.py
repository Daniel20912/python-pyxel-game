import pyxel


class ContadorBolas:
    def __init__(self):
        self.counter = 0

    def incrementar_contador(self):
        try:
            if not isinstance(self.counter, int) or self.counter < 0:
                raise ValueError("O contador deve ser um número inteiro e positivo.")
        except ValueError as e:
            raise e

        self.counter += 1

    def get_contador(self):
        return self.counter

    def draw(self):
        try:
            if not isinstance(self.counter, int) or self.counter < 0:
                raise ValueError(
                    "O contador deve ser um número inteiro não negativo e positivo."
                )
        except ValueError as e:
            raise e

        counter_text = str(self.counter)
        text_width = len(counter_text) * 4
        pyxel.rect(150 - text_width // 2, 10, text_width, 7, pyxel.COLOR_BLACK)
        pyxel.text(150 - text_width // 2, 10, counter_text, pyxel.COLOR_WHITE)

        img_x = 140 - text_width // 2
        img_y = 9
        pyxel.blt(img_x, img_y, 1, 32, 0, 8, 8, pyxel.COLOR_BLACK)
