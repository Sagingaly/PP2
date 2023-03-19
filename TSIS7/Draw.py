import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Sagingaly_games')

icon = pygame.image.load('images_game/7763771_video_game_ea_icon.png')
pygame.display.set_icon(icon)

ball_position = [400, 300]
speed = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP:
                ball_position[1] -= speed
               elif event.key == pygame.K_DOWN:
                   ball_position[1] += speed
               elif event.key == pygame.K_LEFT:
                   ball_position[0] -= speed
               elif event.key == pygame.K_RIGHT:
                   ball_position[0] += speed

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_UP]:
    #     ball_position[1] -= speed
    # elif keys[pygame.K_DOWN]:
    #     ball_position[1] += speed
    # elif keys[pygame.K_LEFT]:
    #     ball_position[0] -= speed
    # elif keys[pygame.K_RIGHT]:
    #     ball_position[0] += speed

    if ball_position[0] - 25 < 0:
        ball_position[0] = 25
    elif ball_position[0] + 25 > 800:
        ball_position[0] = 800 - 25
    if ball_position[1] - 25 < 0:
        ball_position[1] = 25
    elif ball_position[1] + 25 > 600:
        ball_position[1] = 600 - 25



    ball_position[0] = max(25, min(800 - 25, ball_position[0]))
    ball_position[1] = max(25, min(600 - 25, ball_position[1]))

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, 'Red', ball_position, 25)
    pygame.display.update()