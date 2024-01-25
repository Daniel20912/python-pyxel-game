import pyxel
from mouse import Mouse
from contadorBolas import ContadorBolas
from contagemRegressiva import ContagemRegressiva
from mensagemVitoria import MensagemVitoria
from mensagemGameOver import MensagemGameOver
import random
import math


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("assets/map.pyxres")
        self.mouse = Mouse()
        self.contadorBolas = ContadorBolas()
        self.contagemRegressiva = ContagemRegressiva(10 * 30)
        self.mensagemVitoria = MensagemVitoria()
        self.mensagemGameOver = MensagemGameOver()
        self.bola_x = [0, 0, 0]
        self.bola_y = [
            random.randint(10, 110),
            random.randint(10, 110),
            random.randint(10, 110),
        ]
        self.velocidade_bola = [
            random.randint(1, 3),
            random.randint(1, 3),
            random.randint(1, 3),
        ]
        self.bola_clicada = [False, False, False]
        self.ball_time_clicada = [0, 0, 0]
        self.time = 0
        self.game_over = False
        self.vitoria = False
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.game_over and not self.vitoria:
            self.time += 1
            self.contagemRegressiva.decrementar()
            self.mouse.update()
            if (
                self.contagemRegressiva.is_zero()
                and self.contadorBolas.get_contador() < 10
            ):
                self.game_over = True
            elif self.contadorBolas.get_contador() >= 10:
                self.vitoria = True
            for i in range(3):
                if not self.bola_clicada[i]:
                    self.bola_x[i] += self.velocidade_bola[i]
                    if self.bola_x[i] > 160:
                        self.bola_x[i] = 0
                        self.bola_y[i] = random.randint(10, 110)
                        self.velocidade_bola[i] = random.randint(1, 3)
                    if (
                        abs(self.mouse.x - self.bola_x[i]) < 8
                        and abs(self.mouse.y - self.bola_y[i]) < 8
                        and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
                    ):
                        self.bola_clicada[i] = True
                        self.ball_time_clicada[i] = self.time
                        self.contadorBolas.incrementar_contador()
                        pyxel.play(1, 9)
                elif self.time - self.ball_time_clicada[i] > 2 * 30:
                    self.bola_clicada[i] = False
                    self.bola_x[i] = 0
                    self.bola_y[i] = random.randint(10, 110)
                    self.velocidade_bola[i] = random.randint(1, 3)

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 160, 120)
        for i in range(3):
            if not self.bola_clicada[i]:
                y = self.bola_y[i] + 5 * math.sin(self.time / 10.0)
                frame = (self.time // 10) % 2
                pyxel.blt(self.bola_x[i], y, 1, frame * 8, 0, 8, 8, pyxel.COLOR_BLACK)
            else:
                pyxel.blt(
                    self.bola_x[i], self.bola_y[i], 1, 16, 0, 8, 8, pyxel.COLOR_BLACK
                )
        self.mouse.draw()
        self.contadorBolas.draw()
        self.contagemRegressiva.draw()
        if self.game_over:
            self.mensagemGameOver.draw(pyxel.width // 2, 60)
        elif self.vitoria:
            self.mensagemVitoria.draw(pyxel.width // 2, 60)


if __name__ == "__main__":
    App()
