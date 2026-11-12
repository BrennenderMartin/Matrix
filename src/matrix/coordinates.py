import pygame as pg
from src.matrix.data import (
    constants as c
)
from src.matrix.playermatrix import PlayerMatrix
from src.matrix.obstacle import Obstacle

pg.init()

screen: pg.Surface = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_WIDTH))
pg.display.set_caption("Koordinatensystem")
clock = pg.time.Clock()

p = PlayerMatrix([[0, 1], [-2, -2]], 10)
e = PlayerMatrix([[-1, 0], [3, 2]], 10)

o = Obstacle([[1, 1], [2, 1], [2, 2], [1, 2]])

print(p.getFOVPoints())
print(o.verticies)

running: bool = True
key_is_down: bool = False
while running:
    #running = False
    key = pg.key.get_pressed()
    if key[pg.K_a]:
        p.move((-.1, 0))
    elif key[pg.K_d]:
        p.move((.1, 0))
    elif key[pg.K_w]:
        p.move((0, .1))
    elif key[pg.K_s]:
        p.move((0, -.1))

    elif key[pg.K_j]:
        e.move((-.1, 0))
    elif key[pg.K_l]:
        e.move((.1, 0))
    elif key[pg.K_i]:
        e.move((0, .1))
    elif key[pg.K_k]:
        e.move((0, -.1))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and not key_is_down:
                key_is_down = True
                print("CHARGE!!")  # Executes once
            
            elif event.key == pg.K_q and not p.kleft:
                p.rotate(10, [True, False])
                print("Turnign left")
            elif event.key == pg.K_e and not p.kright:
                p.rotate(-10, [False, True])
                print("Turnign right")

            elif event.key == pg.K_u and not e.kleft:
                e.rotate(10, [True, False])
                print("Turnign left")
            elif event.key == pg.K_o and not e.kright:
                e.rotate(-10, [False, True])
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

    p.drawChar(screen, c.BLUE)
    e.drawChar(screen, c.PINK)
    o.draw(screen, c.KIWII)

    print(p.checkIfPointInFOV(e.position))
    print(e.checkIfPointInFOV(p.position))
    print()

    pg.display.flip()
    clock.tick(24)

pg.quit()
