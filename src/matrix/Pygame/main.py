import pygame as pg
import random
#import constants as c
#import variables as v

pg.init()

#create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("SABACC")

#frame rate
clock = pg.time.Clock()
FPS = 60

#Farbe:
#red = True
#yellow = False
v = [1, 2, 3, 4, 5, 6]
cards_value_red = [1, 2, 3, 4, 5, 6, 
                   7, 8, 9, 10, 11, 12, 
                   13, 14, 15, 16, 17, 18]
cards_value_yellow = [1, 2, 3, 4, 5, 6, 
                      7, 8, 9, 10, 11, 12, 
                      13, 14, 15, 16, 17, 18]

cards_used_red = []
cards_used_yellow = []

ind = 0

class Card(pg.sprite.Sprite):
    def __init__(self, color, x, y, type_card, cards):
        pg.sprite.Sprite.__init__(self)
        self.card = 0
        self.type_card = type_card
        if self.card != 0:
            self.type_card = (self.card) % 6

        #set up the color
        self.color = color
        self.ind = ind
        self.x = 0
        if cards != None:
            self.cards = [cards]
        else:
            self.cards = []

        if self.color == True:
            self.cards_value_kind = cards_value_red
            self.cards_used_kind = cards_used_red
            self.spite_color_kind = "hearts"
        elif self.color == False:
            self.cards_value_kind = cards_value_yellow
            self.cards_used_kind = cards_used_yellow
            self.spite_color_kind = "spades"

        #set up the image
        if isinstance(self.type_card, int):
            self.dict_card = f"Pygame/Sabacc/kenney_playing-cards-pack/PNG/Cards (large)/card_{self.spite_color_kind}_0{self.type_card}.png"
        elif isinstance(self.type_card, str):
            self.dict_card = f"Pygame/Sabacc/kenney_playing-cards-pack/PNG/Cards (large)/card_{self.type_card}.png"
        self.image = pg.image.load(self.dict_card).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self):
        print(self.type_card)
        if isinstance(self.type_card, int):
            self.dict_card = f"Pygame/Sabacc/kenney_playing-cards-pack/PNG/Cards (large)/card_{self.spite_color_kind}_0{self.type_card}.png"
        elif isinstance(self.type_card, str):
            self.dict_card = f"Pygame/Sabacc/kenney_playing-cards-pack/PNG/Cards (large)/card_{self.type_card}.png"
        self.image = pg.image.load(self.dict_card).convert_alpha()   

    def draw_a_card(self):
        self.ind += 1
        self.x = random.randint(0, 17-self.ind)
        print(f"{self.ind+1} x:{self.x} Karte:{self.cards_value_kind[self.x]}")
        self.cards_used_kind.append(self.cards_value_kind[self.x])
        del self.cards_value_kind[self.x]
    
    def draw_card(self): #from discard / card pile --> hand
        print("draw_card")
    def discard_card(self): #from hand --> discard pile
        print("discard_card")


class Button(pg.sprite.Sprite):
  def __init__(self, x, y):
    pg.sprite.Sprite.__init__(self)
    self.image = pg.image.load("Pygame/Sabacc/kenney_board-game-icons/PNG/Default (64px)/cards_take.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.mask = pg.mask.from_surface(self.image)
    self.rect.center = (x, y)

class Cursor(pg.sprite.Sprite):
  def __init__(self):
    pg.sprite.Sprite.__init__(self)
    self.image = pg.Surface((10, 10))
    self.rect = self.image.get_rect()
    self.image.fill(c.RED)
    self.mask = pg.mask.from_surface(self.image)

  def update(self, colour):
    pos = pg.mouse.get_pos()
    self.rect.center = (pos)
    self.image.fill(colour)

class Action():
    def __init__(self):
        #import all cardvalues
        self.c_r = card_red.card
        self.c_y = card_yellow.card
        self.p_r = card_pile_r.card
        self.p_y = card_pile_y.card
        self.d_r = card_discardpile_r.card
        self.d_y = card_discardpile_y.card

        #import lists
        self.v_r = v
        self.v_y = cards_value_yellow

        self.ind_r = ind
        self.ind_y = ind
        self.x = 0

    def get_value_red(self):
        self.ind_r += 1
        maximum = len(self.v_r)-self.ind_r
        self.x = random.randint(0, maximum)
        print(f"{self.ind_r+1} x:{self.x} Karte:{self.v_r[self.x]}")
        self.v_r.remove(self.v_r[self.x])
    
    def get_value_yel(self):
        self.ind_y += 1
        maximum = len(self.v_y)-self.ind_y
        x = random.randint(0, maximum)       
        print(f"{self.ind_y+1} x:{x} Karte:{self.v_y[x]}")
        self.v_y.remove(self.v_y[x])
    
    def change_var(self, instance_of_a, new_variable):
        instance_of_a.card = new_variable

    def draw_pr(self):
        self.p_r = 1
        self.get_value_red()
        self.change_var(card_red, 4)
    
    def draw_py(self):
        self.p_y = 1
    
    def draw_dr(self):
        self.d_r = 1
    
    def draw_dy(self):
        self.d_y = 1
    
    def update(self):
        #print(f"c_r:{self.c_r}; c_y:{self.c_y}; p_r:{self.p_r}; p_y:{self.p_y}; d_r:{self.d_r}; d_y:{self.d_y}")
        x = 0
        x += 1
    
    def start(self):
        self.get_value_red()
        


#hide mouse cursor
pg.mouse.set_visible(False)

#create cards
card_red = Card(True, 200, 450, 3, None)
card_yellow = Card(False, 400, 450, 4, None)
card_pile_r = Card(True, 150, 250, "back", cards_value_red)
card_pile_y = Card(False, 450, 250, "back", cards_value_yellow)
card_discardpile_r = Card(True, 250, 250, "joker_red", None)
card_discardpile_y = Card(False, 350, 250, "joker_black", None)

print(f"Pile_r:{card_pile_r.cards}; Pile_y:{card_pile_y.cards}; Discardpile_r:{card_discardpile_r.cards}; Discardpile_y:{card_discardpile_y.cards};Handcard_r:{card_red.cards};Handcard_y:{card_yellow.cards}")

#create buttons
button_red = Button(150, 350)
button_yellow = Button(450, 350)
button_red_d = Button(250, 350)
button_yellow_d = Button(350, 350)

#create instances of cursor
cursor = Cursor()

#main class for all action/ changing values
action = Action()

#create sprite groups
all_cards = pg.sprite.Group()
buttons = pg.sprite.Group()
cursor_group = pg.sprite.Group()

#add instances to groups
all_cards.add(card_red, card_yellow, card_pile_r, card_pile_y, card_discardpile_r, card_discardpile_y)
buttons.add(button_red, button_yellow, button_red_d, button_yellow_d)
cursor_group.add(cursor)

def button_press():
    print("Button has been clicked")
def button_press_red():
    print("RED Button has been clicked")
    action.draw_pr()
def button_press_yellow():
    print("YELLOW Button has been clicked")
    action.draw_py()
def button_press_red_d():
    print("RED_d Button has been clicked")
    action.draw_dr()
def button_press_yellow_d():
    print("YELLOW_d Button has been clicked")
    action.draw_dy()

action.start()
run = True
while run:
      
    clock.tick(FPS)

    screen.fill(c.BG)

    #make the cursor different colors, when hovering over the draw buttons
    if pg.sprite.spritecollide(cursor, buttons, False, pg.sprite.collide_mask):
        if pg.sprite.spritecollide(button_red, cursor_group, False, pg.sprite.collide_mask):
            col = c.RED
        elif pg.sprite.spritecollide(button_yellow, cursor_group, False, pg.sprite.collide_mask):
            col = c.YELLOW
        elif pg.sprite.spritecollide(button_red_d, cursor_group, False, pg.sprite.collide_mask):
            col = c.CYAN
        elif pg.sprite.spritecollide(button_yellow_d, cursor_group, False, pg.sprite.collide_mask):
            col = c.VIOLET
    else:
        col = c.GREEN

    card_red.update()
    cursor_group.update(col)
    #action.update()

    all_cards.draw(screen)
    buttons.draw(screen)
    cursor_group.draw(screen)

    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pg.sprite.spritecollide(button_red, cursor_group, False, pg.sprite.collide_mask):
                    button_press_red()
                elif pg.sprite.spritecollide(button_yellow, cursor_group, False, pg.sprite.collide_mask):
                    button_press_yellow()
                elif pg.sprite.spritecollide(button_red_d, cursor_group, False, pg.sprite.collide_mask):
                    button_press_red_d()
                elif pg.sprite.spritecollide(button_yellow_d, cursor_group, False, pg.sprite.collide_mask):
                    button_press_yellow_d()
        
                
        if event.type == pg.QUIT:
            run = False
    
    pg.display.flip()

pg.quit()