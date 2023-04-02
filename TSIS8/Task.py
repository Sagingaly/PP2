import pygame
import random

pygame.init()

width=800
height =600

screen=pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

ship={
    'speed': 50,
    'x' : width/2,
    'y' : height-50,
}

meteors=[]

game_over=False

for i in range(10):
    meteor = {'x': random.randint(0, width), 'y': random.randint(-500, -50), 'speed': random.randint(45, 65)}
    meteors.append(meteor)

while not game_over:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
            pygame.quit()
            quit()
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        ship['x']-=ship['speed']
    if key[pygame.K_RIGHT]:
        ship['x']+=ship['speed']
    for meteor in meteors:
        meteor['y']+=meteor['speed']

        ship_rect = pygame.Rect(ship['x'], ship['y'], 50, 50)
        meteor_rect = pygame.Rect(meteor['x'], meteor['y'], 30, 30)

        if ship_rect.colliderect(meteor_rect):
            game_over=True
            # pygame.quit()
            # quit()
        
        if meteor['y'] > height:
            meteor['y'] = random.randint(-500, -50)
            meteor['x'] = random.randint(0, width)
        screen.fill('black')
        pygame.draw.rect(screen, 'white', [ship['x'], ship['y'], 50, 50])

        for meteor in meteors:
            pygame.draw.circle(screen, 'red', [meteor['x'], meteor['y']], 15)
        pygame.display.update()
        clock.tick(60)
