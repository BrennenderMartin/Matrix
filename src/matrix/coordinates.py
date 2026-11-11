import pygame as pg
from src.matrix.data import (
    constants as c
)
from src.matrix.playermatrix import PlayerMatrix

pg.init()

screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_WIDTH))
pg.display.set_caption("Koordinatensystem")
clock = pg.time.Clock()

p = PlayerMatrix([[0, 1], [-2, -2]], 30)
e = PlayerMatrix([[-1, 0], [3, 3]], 25)

running: bool = True
key_is_down: bool = False
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

    elif key[pg.K_j] == True:
        e.move((-.1, 0))
    elif key[pg.K_l] == True:
        e.move((.1, 0))
    elif key[pg.K_i] == True:
        e.move((0, .1))
    elif key[pg.K_k] == True:
        e.move((0, -.1))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and not key_is_down:
                key_is_down = True
                print("CHARGE!!")  # Executes once
            
            elif event.key == pg.K_q and not p.kleft:
                p.rotate(15, [True, False])
                print("Turnign left")
            elif event.key == pg.K_e and not p.kright:
                p.rotate(-15, [False, True])
                print("Turnign right")

            elif event.key == pg.K_u and not e.kleft:
                e.rotate(15, [True, False])
                print("Turnign left")
            elif event.key == pg.K_o and not e.kright:
                e.rotate(-15, [False, True])
                print("Turnign right")

        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                key_is_down = False
                print("HOLD!!!")  # Executes on release
            
            elif event.key == pg.K_q:
                p.kleft = False
            elif event.key == pg.K_e:
                p.kright = False

            elif event.key == pg.K_u:
                e.kleft = False
            elif event.key == pg.K_o:
                e.kright = False


    screen.fill(c.WHITE)

    pg.draw.line(screen, c.BLACK, (0, c.SCREEN_MID_HEIGHT), (c.SCREEN_WIDTH, c.SCREEN_MID_HEIGHT), 2)
    pg.draw.line(screen, c.BLACK, (c.SCREEN_MID_WIDTH, 0), (c.SCREEN_MID_WIDTH, c.SCREEN_HEIGHT), 2)

    p.drawChar(screen, c.BLUE) # type: ignore
    e.drawChar(screen, c.PINK) # type: ignore

    print(p.checkIfPointInFOV(e.position))
    print(e.checkIfPointInFOV(p.position))
    print()

    pg.display.flip()
    clock.tick(24)

pg.quit()
