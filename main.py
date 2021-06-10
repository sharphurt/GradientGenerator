from os import mkdir
from os.path import isdir, exists

import RandomColors
from LinearGradientGenerator import LinearGradientGenerator
from QualityPredictor import QualityPredictor
import pygame as pg


def pil_image_to_surface(pil_image):
    return pg.image.fromstring(
        pil_image.tobytes(), pil_image.size, pil_image.mode).convert()


WIDTH = 360
HEIGHT = 480
FPS = 120
running = True

pg.font.init()

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption(f'Gradient Generator')

quality_predictor = QualityPredictor()
colors = []
is_saved = False
history = []

arial_font_bold = pg.font.SysFont('Arial', 16, bold=True)
arial_font_large = pg.font.SysFont('Arial', 16)
arial_font_small = pg.font.SysFont('Arial', 14)


def select_color():
    is_beautiful = False
    color_pair = None
    while not is_beautiful:
        color_pair = RandomColors.colors(2)
        is_beautiful = quality_predictor.predict(color_pair[0], color_pair[1])

    return color_pair


def check_if_saved():
    return isdir('output') and exists(f'output/{colors[0]}_{colors[1]}.png')


def save_to_file():
    global is_saved
    if not isdir('output'):
        mkdir('output')
    pg.image.save(screen, f'output/{colors[0]}_{colors[1]}.png')
    is_saved = True
    draw_saved()


def draw_gradient():
    screen.blit(
        pg.transform.scale(pil_image_to_surface(LinearGradientGenerator((100, 100)).generate(colors)), (WIDTH, HEIGHT)),
        (0, 0))
    pg.display.flip()


def draw_UI():
    pg.draw.rect(screen, (255, 255, 255), (0, HEIGHT - 60, WIDTH, 60))

    pg.draw.circle(screen, colors[1], (30, HEIGHT - 30), 15)
    pg.draw.circle(screen, colors[0], (180, HEIGHT - 30), 15)

    help_text_1 = arial_font_small.render('Space - next gradient', True, (0, 0, 0))
    help_text_2 = arial_font_small.render('Backspace - previous gradient', True, (0, 0, 0))
    help_text_3 = arial_font_small.render('Enter - save gradient', True, (0, 0, 0))

    screen.blit(help_text_1, (10, 10))
    screen.blit(help_text_2, (10, 25))
    screen.blit(help_text_3, (10, 40))

    color_code_1 = arial_font_large.render(f'{colors[1]}', True, (0, 0, 0))
    color_code_2 = arial_font_large.render(f'{colors[0]}', True, (0, 0, 0))

    screen.blit(color_code_1, (60, HEIGHT - 35))
    screen.blit(color_code_2, (210, HEIGHT - 35))
    pg.display.flip()


def draw_saved():
    text = arial_font_bold.render(f'Saved', True, (0, 0, 0))
    screen.blit(text, (300, HEIGHT - 35))
    pg.display.flip()


def update_gradient(previous=False):
    global is_saved, colors
    if previous and len(history) <= 1:
        return

    if not previous:
        history.append(colors)

    colors = history.pop() if previous else select_color()
    draw_gradient()
    draw_UI()

    is_saved = check_if_saved()
    if is_saved:
        draw_saved()


update_gradient()

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                update_gradient()
            if event.key == pg.K_BACKSPACE:
                update_gradient(previous=True)
            if event.key == pg.K_RETURN and not is_saved:
                save_to_file()
pg.quit()
