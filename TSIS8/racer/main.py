import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
FPS = 45
FramePerSec = pygame.time.Clock()
  
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
coinscore=0
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black") 
background = pygame.image.load("images/AnimatedStreet.png")
coin= [
         pygame.image.load("coinimages/image_part_001.png"),
#          pygame.image.load("coinimages/image_part_001.png"),
#          pygame.image.load("coinimages/image_part_001.png"),
#          pygame.image.load("coinimages/image_part_001.png"),
#          pygame.image.load("coinimages/image_part_002.png"),
#          pygame.image.load("coinimages/image_part_002.png"),
#          pygame.image.load("coinimages/image_part_002.png"),
#          pygame.image.load("coinimages/image_part_002.png"),
#          pygame.image.load("coinimages/image_part_003.png"),
#          pygame.image.load("coinimages/image_part_003.png"),
#          pygame.image.load("coinimages/image_part_003.png"),
#          pygame.image.load("coinimages/image_part_003.png"),
#          pygame.image.load("coinimages/image_part_004.png"),
#          pygame.image.load("coinimages/image_part_004.png"),
#          pygame.image.load("coinimages/image_part_004.png"),
#          pygame.image.load("coinimages/image_part_004.png"),
#          pygame.image.load("coinimages/image_part_005.png"),
#          pygame.image.load("coinimages/image_part_005.png"),
#          pygame.image.load("coinimages/image_part_005.png"),
#          pygame.image.load("coinimages/image_part_005.png"),
#          pygame.image.load("coinimages/image_part_006.png"),
#          pygame.image.load("coinimages/image_part_006.png"),
#          pygame.image.load("coinimages/image_part_006.png"),
#          pygame.image.load("coinimages/image_part_006.png"),
]
coini=0
coins=0
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
pygame.display.set_caption("Racer")
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-7, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(7, 0)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image=coin[coini]
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(32, SCREEN_WIDTH-32), -31)
        self.a =random.randint(600,1000)    
    def move(self):
        global coinscore
        self.rect.move_ip(0,10)
        if self.rect.top > 600:
            self.rect.top = -62
            self.rect.center = (random.randint(32, SCREEN_WIDTH-32), -31)
        elif self.rect.colliderect(P1):
            coinscore+=1
            self.rect.top = -62
            self.rect.center = (random.randint(32, SCREEN_WIDTH-32), -31)    
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1=Coin()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
Coins= pygame.sprite.Group()
Coins.add(C1)
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
bgy=0
coin_y=-62
coin_x=0
y=0
bgsound=pygame.mixer.Sound("sounds/background.wav")
bgsound.play()
#Game Loop
while True:
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.3     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.blit(background, (0,bgy))
    DISPLAYSURF.blit(background, (0,bgy-600))
    if coini==23:
       coini=0
    else:
       coini+=1
    if bgy<600:
       bgy+=7
    else:
       bgy=0
    # if coins==0:
    #     coin_x=random.randint(0, 400 - 61)
    #     y=random.randint(600, 1000)
    #     coins=1
    scores = font_small.render(str(SCORE), True, "BLACK")
    coinscores = font_small.render(str(coinscore), True, "BLACK")
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coinscores, (360,10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    for el in Coins:
        DISPLAYSURF.blit(el.image, el.rect)
        el.move()
    # if coin_y<=y:
    #     DISPLAYSURF.blit(coin[coini], (coin_x,coin_y))
    #     crect=coin[coini].get_rect()
    #     if crect.colliderect(P1.rect):
    #         coinscore +=1
    #         coins=0
    #         coin_y=-62
    #     else:
    #         if coini==23:
    #           coini=0
    #         else:
    #           coini+=1
    #           coin_y+=7
    #         if coin_y>=y:
    #           coins=0
    #           coin_y=-62 
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('sounds/crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill("RED")
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(1)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)