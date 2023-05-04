import json

import pygame
import random
import time
import psycopg2
from levels import levels

DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_PASSWORD = ""

conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS "user"(
    login TEXT PRIMARY KEY,
    positions JSONB,
    fruit_pos JSONB,
    lvl INTEGER
);

CREATE TABLE IF NOT EXISTS user_score(
    login TEXT PRIMARY KEY,
    score INTEGER,
    FOREIGN KEY (login) REFERENCES "user" (login)
);

""")
conn.commit()

pygame.init()
FPS = 10
WIDTH = 800
HEIGHT = 800
board_size = WIDTH * 0.9, HEIGHT * 0.9
window_pos = ((WIDTH - board_size[0]) // 2, (HEIGHT - board_size[1]) // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
pygame.font.init()
font = pygame.font.SysFont(None, 72)
level = 1
class Fruit(object):
    def __init__(self):
        self.window = screen
        self.window_size = board_size
        self.window_pos = window_pos
        self.item_size = 20

        self.color = 221, 75, 57
        self.surface = pygame.image.load('source/snake/apple.png')
        self.randomize()

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.item_size, self.item_size)
        surface = pygame.transform.scale(self.surface, (self.item_size, self.item_size))
        screen.blit(surface, rect)

    def randomize(self):

        while True:
            x = random.randrange(0, board_size[0])
            y = random.randrange(0, board_size[1])

            x += self.window_pos[0]
            y += self.window_pos[1]

            self.x = x - x % self.item_size
            self.y = y - y % self.item_size

            self.fruit_pos = {'x': self.x, 'y': self.y}

            if not self.hasHitWall():
                break

    def hasHitWall(self):

        walls = levels[level]
        for wall in walls:
            rectW = pygame.Rect(wall)
            rectF = pygame.Rect(self.x, self.y, self.item_size, self.item_size)
            if rectW.colliderect(rectF):
                return True

        return False

fruit = Fruit()
fruit.randomize()
username = input("Username: ")
cur.execute("SELECT * FROM \"user\" WHERE login = %s", [username])
record = cur.fetchone()
if record:
    positions = record[1]
    fruit_pos = record[2]
    level = record[3]

    cur.execute("SELECT * FROM user_score WHERE login = %s", [username])
    score = cur.fetchone()[1]



else:
    x = board_size[0] // 2 + window_pos[0]
    y = board_size[1] // 2 + window_pos[1]
    snake = [
        {
            'x': x,
            'y': y
        }
    ]



    positions = snake

    cur.execute("INSERT INTO \"user\"(login, positions, fruit_pos,  lvl) VALUES(%s, %s, %s, %s)", [username, json.dumps(snake), json.dumps(fruit.fruit_pos), 1])
    cur.execute("INSERT INTO user_score (login, score) VALUES(%s, %s)", [username, 0])
    conn.commit()
    level = 1
    score = 0



print("Welcome, ", username)
print("Your level ", level)
print("Your score ", score)

score_next_level = 3
game_over = False
next_level = False
game_started = False

fruit.x = fruit_pos['x']
fruit.y = fruit_pos['y']


class Snake(object):
    def __init__(self):
        self.window = screen
        self.window_size = board_size
        self.window_pos = window_pos
        self.item_size = 20

        self.color = 66, 133, 244
        self.head_color = 70, 100, 232
        self.snake = positions
        self.dx = 1
        self.dy = 0

    def reset(self):
        x = self.window_size[0] // 2 + self.window_pos[0]
        y = self.window_size[1] // 2 + self.window_pos[1]
        self.snake = [
            {
                'x': x,
                'y': y
            }
        ]
        self.future_item = None
        self.dx = 1
        self.dy = 0

    def move(self):
        head = self.snake[0]
        self.future_item = self.snake.pop()
        self.snake.insert(0, {
            'x': (head['x'] - self.window_pos[0] + self.dx * self.item_size) + self.window_pos[0],
            'y': (head['y'] - self.window_pos[1] + self.dy * self.item_size) + self.window_pos[1]
        })

    def draw(self):
        for i, item in enumerate(self.snake):
            color = self.color
            if i == 0:
                color = self.head_color

            self.rect = pygame.draw.rect(
                self.window, color, (item['x'], item['y'], self.item_size, self.item_size))

    def eat(self, fruit):
        head = self.snake[0]
        return abs(head['x'] - fruit.x) < 20 and abs(head['y'] - fruit.y) < 20

    def overlap(self):
        return self.snake.count(self.snake[0]) > 1

    def grow(self):
        self.snake.append(self.future_item)

    def hasHitWall(self):
        rects = []
        for i, item in enumerate(self.snake):
            rect = pygame.Rect((item['x'], item['y'], self.item_size, self.item_size))
            rects.append(rect)

        walls = levels[level]
        for wall in walls:
            rect = pygame.Rect(wall)
            if rect.collidelistall(rects):
                return True

        head = self.snake[0]
        if head['x'] < self.window_pos[0] or head['x'] >= self.window_pos[0] + self.window_size[0]:
            return True
        if head['y'] < self.window_pos[1] or head['y'] >= self.window_pos[1] + self.window_size[1]:
            return True

        return False


class Wall(object):
    def __init__(self):
        self.window = screen
        self.window_size = board_size
        self.window_pos = window_pos
        self.color = (232, 92, 70)

    def draw(self):
        walls = levels[level]

        for wall in walls:
            pygame.draw.rect(screen, self.color, wall)


snake = Snake()

wall = Wall()



apple_image = {
    'size': {
        'width': 40,
        'height': 40
    }
}

apple_image['pos'] = {
    'x': (window_pos[0] - apple_image['size']['width']) // 2,
    'y': (window_pos[1] - apple_image['size']['height']) // 2,
}
apple_image['image'] = pygame.transform.scale(
    pygame.image.load('source/snake/apple.png'), (apple_image['size']['width'], apple_image['size']['height']))

trophy_image = {
    'size': {
        'width': 40,
        'height': 40
    }
}

trophy_image['pos'] = {
    'x': (WIDTH - apple_image['pos']['x'] - trophy_image['size']['width']),
    'y': (window_pos[1] - apple_image['size']['height']) // 2,
}
trophy_image['image'] = pygame.transform.scale(
    pygame.image.load('source/snake/trophy.png'), (trophy_image['size']['width'], trophy_image['size']['height']))

clock = pygame.time.Clock()

game_over_text = font.render('Game Over.', False, (153, 21, 0))
speed = {
    1: FPS,
    2: FPS + 5,
    3: FPS + 10
}

def mode_game_over():
    screen.fill((232, 92, 70))

    screen.blit(
        game_over_text, ((WIDTH - game_over_text.get_width()) // 2,
                         (HEIGHT - game_over_text.get_height() - game_over_text.get_height()) // 2))
    score_text = font.render('Score: %i' % score, False, (153, 21, 0))
    screen.blit(
        score_text,
        ((WIDTH - score_text.get_width()) // 2, (HEIGHT - score_text.get_height() - score_text.get_height()) // 2 + 45))

    pygame.display.update()
    clock.tick(1)


def mode_next_level():

    screen.fill((86, 138, 52))

    next_level_text = font.render('You have passed', False, (153, 21, 0))

    screen.blit(
        next_level_text, ((WIDTH - next_level_text.get_width()) // 2,
                          (HEIGHT - next_level_text.get_height() - next_level_text.get_height()) // 2))

    if level == 3:
        level_text = font.render('game', False, (153, 21, 0))
        screen.blit(
            level_text,
            ((WIDTH - level_text.get_width()) // 2,
             (HEIGHT - level_text.get_height() - level_text.get_height()) // 2 + 45))
        pygame.display.update()
        clock.tick(1)
    level_text = font.render('level %i' % level, False, (153, 21, 0))
    screen.blit(
        level_text,
        ((WIDTH - level_text.get_width()) // 2, (HEIGHT - level_text.get_height() - level_text.get_height()) // 2 + 45))

    pygame.display.update()
    clock.tick(1)



def save_game(level, snake, score, fruit_pos):
    cur.execute("""UPDATE \"user\" SET lvl = %s, positions = %s, fruit_pos=%s WHERE login = %s""", [level, json.dumps(snake), json.dumps(fruit_pos), username])
    cur.execute("""UPDATE user_score SET score = %s WHERE login = %s""", [score, username])
    conn.commit()





while True:

    screen.fill((86, 138, 52))
    pygame.draw.rect(screen, (170, 215, 81),
                     (window_pos[0], window_pos[1], board_size[0], board_size[1]))

    pygame.draw.rect(screen, (74, 117, 44),
                     (0, 0, WIDTH, window_pos[1]))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            game_started = True
            if event.key == pygame.K_LEFT and snake.dx <= 0:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_RIGHT and snake.dx >= 0:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_UP and snake.dy <= 0:
                snake.dx = 0
                snake.dy = -1
            elif event.key == pygame.K_DOWN and snake.dy >= 0:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_SPACE:
                if game_over:
                    snake.reset()
                    fruit.randomize()
                    score = 0
                    game_over = False
                    game_started = False
                elif next_level:
                    snake.reset()
                    fruit.randomize()
                    next_level = False
                    score =0
                    level += 1
                    game_started = False
                    save_game(level, snake.snake, score, fruit.fruit_pos)

                else:
                    game_started = False
                    save_game(level, snake.snake, score, fruit.fruit_pos)


    if game_over:
        mode_game_over()

    elif next_level:
        mode_next_level()


    else:
        score_text = pygame.font.SysFont(None, 20).render(
            str(score), False, (200, 200, 200))
        level_text = pygame.font.SysFont(None, 20).render(
            str(level), False, (200, 200, 200))

        if game_started:
            snake.move()
        fruit.draw()
        wall.draw()
        if snake.eat(fruit):
            snake.grow()
            score += 1
            if score >= score_next_level:
                next_level = True
            fruit.randomize()
        if snake.overlap():
            # game over
            game_over = True
            time.sleep(1)

        if not snake.hasHitWall():
            snake.draw()

        else:
            game_over = True

        screen.blit(
            apple_image['image'], (apple_image['pos']['x'], apple_image['pos']['y']))
        screen.blit(
            score_text, (apple_image['pos']['x'] + apple_image['size']['width'], apple_image['pos']['y'] + 10))
        screen.blit(
            trophy_image['image'], (trophy_image['pos']['x'], trophy_image['pos']['y']))
        screen.blit(
            level_text, (trophy_image['pos']['x'] - 10, trophy_image['pos']['y'] + 10))

        pygame.display.update()

        clock.tick(speed[level])
