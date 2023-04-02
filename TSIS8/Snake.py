
import pygame
import random
import time

res = 800
size = 50

x, y = random.randrange(0, res, size), random.randrange(0, res, size)
apple = random.randrange(0, res, size), random.randrange(0, res, size)
dris = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
pygame.init()
screen = pygame.display.set_mode((res, res))
clock = pygame.time.Clock()
score = 0
fps = 5
game_over = False
pygame.mixer.init()  # initialize the mixer module
score_sound = pygame.mixer.Sound('Sounds/lab8_data_smb_coin.wav')  # load the sound effect file
while not game_over:
    screen.fill(pygame.Color(0, 154, 255))
    [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, size, size))) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, size, size))

    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = random.randrange(0, res, size), random.randrange(0, res, size)
        length += 1
        fps += 1
        score += 1
        score_sound.play()  # play the sound effect
    if x < 0 or x > res - size or y < 0 or y > res - size:
        game_over = True
    if len(snake) != len(set(snake)):
        game_over = True

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dris['W']:
        dris = {'W': True, 'S': False, 'A': True, 'D': True}
        dx, dy = 0, -1
    if key[pygame.K_s] and dris['S']:
        dx, dy = 0, 1
        dris = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dris['A']:
        dx, dy = -1, 0
        dris = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dris['D']:
        dx, dy = 1, 0
        dris = {'W': True, 'S': True, 'A': False, 'D': True}

# ...previous code...

if game_over:
    screen.fill(pygame.Color(0, 154, 255))
    font_go = pygame.font.SysFont('Times New Roman', 60)
    text_go = font_go.render('Game Over', True, pygame.Color('white'))
    screen.blit(text_go, (res / 2 - text_go.get_width() / 2, res / 2 - text_go.get_height() / 2))
    font_score = pygame.font.SysFont('Arial', 30)
    text_score = font_score.render('Final Score: ' + str(score), True, pygame.Color('white'))
    screen.blit(text_score, (res / 2 - text_score.get_width() / 2, res / 2 + text_score.get_height() / 2))
    pygame.mixer.init()
    game_over_sound = pygame.mixer.Sound('Sounds/lab8_data_smb_gameover.wav')

    pygame.display.flip()
    game_over_sound.play()
    # Wait for 3 seconds before closing the game window
    time.sleep(3)

# End the Pygame module
pygame.quit()