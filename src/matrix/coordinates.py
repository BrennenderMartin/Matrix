import pygame as pg
from src.matrix.playermatrix import PlayerMatrix
from src.matrix.obstacle import Obstacle
from src.matrix.data import (
    constants as c,
    colours as co
)


pg.init()

screen: pg.Surface = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_WIDTH))
screen: pg.Surface = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_WIDTH))
pg.display.set_caption("Koordinatensystem")
clock = pg.time.Clock()

p = PlayerMatrix([[2,1], [1,1]], 10)
e = PlayerMatrix([[-1, 0], [5,3]], 10)

o = Obstacle([[2,2], [2,0], [0,2]])

print(p.getFOVPoints())
print(o.getVerticies())
print(o.checkTwoPlayers(p, e))

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

    #EVENT HANDLER
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


    screen.fill(co.WHITE)

    pg.draw.line(screen, co.BLACK, (0, c.SCREEN_MID_HEIGHT), (c.SCREEN_WIDTH, c.SCREEN_MID_HEIGHT), 2)
    pg.draw.line(screen, co.BLACK, (c.SCREEN_MID_WIDTH, 0), (c.SCREEN_MID_WIDTH, c.SCREEN_HEIGHT), 2)

    pg.draw.line(screen, co.BG, p.getPosition(), e.getPosition(), 2) # type: ignore

    """
    for i in range(10):
        pg.draw.circle(screen, co.BG, p.getPosition(p.position + 0.1 * i * (e.position - p.position)), i * 1.5) # type: ignore
    """
    p.drawChar(screen, co.BLUE)
    e.drawChar(screen, co.PINK)
    o.draw(screen, co.KIWII)
    
    
    print(p.checkIfPointInFOV(e.position))
    print(not o.checkTwoPlayers(p, e)[0])
    #print(e.checkIfPointInFOV(p.position) and o.checkTwoPlayers(e, p)[0])
    print()
    """"""

    pg.display.flip()
    clock.tick(24)

pg.quit()
