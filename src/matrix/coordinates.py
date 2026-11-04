import pygame as pg
import src.matrix.var.constants as c
from src.matrix.playermatrix import PlayerMatrix

pg.init()


screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_WIDTH))
pg.display.set_caption("Koordinatensystem")
clock = pg.time.Clock()

p = PlayerMatrix([[1],[1]], [[1],[1]], 30)
e = PlayerMatrix([[-1],[0]], [[3],[3]], 25)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(c.BG)

    # Achsen einzeichnen (Ursprung oben links)
    pg.draw.line(screen, c.WHITE, (0, c.SCREEN_MID_HEIGHT), (c.SCREEN_WIDTH, c.SCREEN_MID_HEIGHT), 2)  # X-Achse
    pg.draw.line(screen, c.WHITE, (c.SCREEN_MID_WIDTH, 0), (c.SCREEN_MID_WIDTH, c.SCREEN_HEIGHT), 2)  # Y-Achse

    p.drawChar(screen, c.BLUE)
    e.drawChar(screen, c.PINK)

    pg.display.flip()
    clock.tick(60)

pg.quit()
