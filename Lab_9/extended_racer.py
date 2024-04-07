from re import escape
from unittest import skip
import pygame
import random
import time
pygame.init()
from pygame.locals import*

'''
object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))
 
print(object1.colliderect(object2))
print(object1.collidepoint(50, 75))
'''

#creating variables
sc = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
FPS = 60

W, H = 400, 600
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SPEED = 5
SCORE = 0
MONEY = 0
font = pygame.font.SysFont("Verdana", 60)
small_font = pygame.font.SysFont("verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("AnimatedStreet.png")

#adding event to increase speed of enemies over time and for bunch of coins
INCREASE_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INCREASE_SPEED, 8000)


#defining classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys =pygame.key.get_pressed()
        if self.rect.left >= 0 and self.rect.right <= W:
          if pressed_keys[K_LEFT] and self.rect.left > 7:
              self.rect.move_ip(-7, 0)
          if pressed_keys[K_RIGHT] and self.rect.right < 393:
              self.rect.move_ip(7, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect) 

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("TRUE_COIN_FOR_LAB_8.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global MONEY
        self.rect.move_ip(0, 5)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Bunch_of_coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Bunch of Coins.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global MONEY
        self.rect.move_ip(0, 10)
        if self.rect.top > 600:
            self.rect.top = -1700
            self.rect.center = (random.randint(30, 370), -1700)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


#creating objects
P1 = Player()
E1 = Enemy()
Coin1 = Coin()
Bunch1 = Bunch_of_coins()
'''
E1.draw(sc)
P1.draw(sc)
'''


#creating sprites groups
enemies = pygame.sprite.Group()
items = pygame.sprite.Group()
bunch_item = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
enemies.add(E1)
items.add(Coin1)
bunch_item.add(Bunch1)
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(Coin1)
all_sprites.add(Bunch1)

counter = 0
rar = 0
minus = 0
speed_over_time = 0 #если поменять значение на отличное от 0, то скорость также будет повышаться со временем

#initialising game
pygame.mixer.Sound("background.wav").play(-1)
while True:
    for event in pygame.event.get():
        if event.type == INCREASE_SPEED:
            SPEED += speed_over_time   
            counter += speed_over_time 

        if event.type == QUIT:
            pygame.quit()
            exit()

    if  SPEED - counter + rar - minus == MONEY // 10 + 4:
        SPEED += 2
        minus += 2
        rar += 1

#adding background + all text
    sc.blit(background, (0,0))
    score = small_font.render("SCORE: " + str(SCORE), True, BLACK)
    money_text = small_font.render( "COINS: " + str(MONEY), True, BLACK)
    sc.blit(score, (10, 10))
    sc.blit(money_text, (290, 10))
    

#setting objects on the screen
    for entity in all_sprites:
        sc.blit(entity.image, entity.rect)
        entity.move()


#checking for collision
    if pygame.sprite.spritecollideany(P1, items):
        MONEY += 1
        pygame.display.update()
        Coin1.rect.center = (random.randint(40, W - 40), 0)
    
    if pygame.sprite.spritecollideany(P1, bunch_item):
        MONEY += 2 #money weight of bunch of coins
        pygame.display.update()
        Bunch1.rect.center = (random.randint(40, W - 40), -1700)

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.wav").play()
        sc.fill(RED)
        sc.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
            time.sleep(1)
            pygame.quit()
            exit()
   
    pygame.display.update()
    clock.tick(FPS)
