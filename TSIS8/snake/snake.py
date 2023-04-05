import pygame
import time
import random
 
pygame.init()
 
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 102)
record=0
BLOCK_SIZE = 10
FPS = 10
game=True
FONT_STYLE = pygame.font.SysFont(None, 30)
LOSE_STYLE = pygame.font.SysFont(None, 80)
def show_score(score):

    value = FONT_STYLE.render("Your Score: " + str(score), True, YELLOW)
    window.blit(value, [0, 0])
 
 
def draw_snake(snake_list):
    
    for x in snake_list:
        pygame.draw.rect(window, WHITE, [x[0], x[1], 10, 10])
 
 
def generate_food():
    food_x = round(random.randrange(0, (WINDOW_WIDTH - BLOCK_SIZE) / 10.0)) * 10.0
    food_y = round(random.randrange(0, (WINDOW_HEIGHT - BLOCK_SIZE) / 10.0)) * 10.0
    return [food_x, food_y]
 
def draw_food(food_position):
   
    pygame.draw.rect(window, RED, [food_position[0], food_position[1], BLOCK_SIZE, BLOCK_SIZE])
 
def loose():
    global window
    global x_change
    global y_change
    x_change = 0 
    y_change = 0
    window.fill('red')
    regame=FONT_STYLE.render("Press SPACE to restart!",False,WHITE)
    lose=LOSE_STYLE.render("GAME OVER!!!",False, WHITE)
    window.blit(lose,[60,200])
    window.blit(regame,[140,260])
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
x = WINDOW_WIDTH / 2
y = WINDOW_HEIGHT / 2
 
x_change = 0
y_change = 0
 
food_position = generate_food()
 
snake_body = []
length_of_snake = 1
level=1
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")
bgsound=pygame.mixer.Sound("sounds/bg.mp3")
bite=pygame.mixer.Sound('sounds/bite.mp3')
bgsound.play()
clock = pygame.time.Clock()
a=pygame.USEREVENT+1
pygame.time.set_timer(a,67000)
while True:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == a:
                bgsound.play()
            if game:
              if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change!=BLOCK_SIZE:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change!=-BLOCK_SIZE:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change!=BLOCK_SIZE:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change!=-BLOCK_SIZE:
                    y_change = BLOCK_SIZE
                    x_change = 0
            if not game:
                if event.type == pygame.KEYUP:
                  if event.key == pygame.K_SPACE:
                    food_position=generate_food()
                    window.fill(BLACK)
                    if length_of_snake-1>record:
                        record=length_of_snake-1
                    snake_body=[]
                    length_of_snake=1
                    x=WINDOW_WIDTH / 2
                    y = WINDOW_HEIGHT / 2
                    level=1
                    FPS=10
                    game=True
    x += x_change
    y += y_change

    window.fill(BLACK)
    record_show=FONT_STYLE.render("Record: "+str(record),True,YELLOW)
    show_score(length_of_snake - 1)
    level_show=FONT_STYLE.render("LVL "+str(level),True,YELLOW)
    window.blit(record_show,[390,0])
    window.blit(level_show,[230,0])
    draw_food(food_position)
    
    snake_head = [x, y]
    snake_body.append(snake_head)
    if len(snake_body) > length_of_snake:
        del snake_body[0]
    draw_snake( snake_body)
    for block in snake_body[:-1]:
        if block == snake_head:
            game=False
            loose()
    if (x > WINDOW_WIDTH-5 or x < 0) or (y > WINDOW_HEIGHT-5 or y < 0):
        game=False
        loose()
    pygame.display.update()

    if x == food_position[0] and y == food_position[1]:
        bite.play()
        food_position = generate_food()
        length_of_snake += 1
        if (length_of_snake-1)%10==0:
            FPS+=8
            level+=1

    clock.tick(FPS)