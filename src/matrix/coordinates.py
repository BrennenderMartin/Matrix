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
key_is_down: bool = False
kLeft: bool = False
kRight: bool = False
while running:
    key = pg.key.get_pressed()
    if key[pg.K_a] == True:
        p.move((-.1, 0))
    elif key[pg.K_d] == True:
        p.move((.1, 0))
    elif key[pg.K_w] == True:
        p.move((0, .1))
    elif key[pg.K_s] == True:
        p.move((0, -.1))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and not key_is_down:
                key_is_down = True
                print("CHARGE!!")  # Executes once
            elif event.key == pg.K_q and not kLeft: # type: ignore
                kLeft = True
                p.rotate(15)
                print(p.norm(p.rotation))
                print("Turnign left")
            elif event.key == pg.K_e and not kRight: # type: ignore
                kRight = True
                p.rotate(-15)
                print(p.norm(p.rotation))
                print("Turnign right")

        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                key_is_down = False
                print("HOLD!!!")  # Executes on release
            elif event.key == pg.K_q: # type: ignore
                kLeft = False
            elif event.key == pg.K_e: # type: ignore
                kRight = False


    screen.fill(c.WHITE)

    # Achsen einzeichnen (Ursprung oben links)
    pg.draw.line(screen, c.BLACK, (0, c.SCREEN_MID_HEIGHT), (c.SCREEN_WIDTH, c.SCREEN_MID_HEIGHT), 2)  # X-Achse
    pg.draw.line(screen, c.BLACK, (c.SCREEN_MID_WIDTH, 0), (c.SCREEN_MID_WIDTH, c.SCREEN_HEIGHT), 2)  # Y-Achse

    p.drawChar(screen, c.BLUE) # type: ignore
    e.drawChar(screen, c.PINK) # type: ignore

    pg.display.flip()
    clock.tick(60)

pg.quit()
