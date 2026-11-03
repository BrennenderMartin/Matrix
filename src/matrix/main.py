import pygame
import math

pygame.init()

#define screen size
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rotating Objects")

#define colours
BG = pygame.Color("violetred4")
BLACK = pygame.Color("#F11188")

turret_original = pygame.image.load("./src/matrix/images/arrow.png").convert_alpha()
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

#frame rate
clock = pygame.time.Clock()
FPS = 60

#game loop
run = True
while run:

    clock.tick(FPS)

    #update background
    screen.fill(BG)

    #get mouse position
    pos = pygame.mouse.get_pos()

    #calculate turret angle
    x_dist = pos[0] - x
    y_dist = -(pos[1] - y)#-ve because pygame y coordinates increase down the screen
    angle = math.degrees(math.atan2(y_dist, x_dist))

    #rotate turret
    turret = pygame.transform.rotate(turret_original, angle - 90)
    turret_rect = turret.get_rect(center = (x, y))

    #draw image
    screen.blit(turret, turret_rect)

    #event handler
    for event in pygame.event.get():
        #quit program
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.flip()

pygame.quit()