from LinearGradientGenerator import LinearGradientGenerator
from RandomColors import colors
import pygame as pg

import tensorflow


def pilImageToSurface(pil_image):
    return pg.image.fromstring(
        pil_image.tobytes(), pil_image.size, pil_image.mode).convert()


WIDTH = 360
HEIGHT = 480
FPS = 120
running = True


pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    gradientSurface = pilImageToSurface(LinearGradientGenerator((100, 100)).generate(colors(2)))
    screen.blit(gradientSurface, gradientSurface.get_rect(center=(WIDTH / 2, HEIGHT / 2)))
    pg.display.flip()

    pg.display.set_caption(f'Gradient Generator | FPS: {clock.get_fps()}')

pg.quit()
