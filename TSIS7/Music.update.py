import pygame

pygame.init()

window_width = 449
window_height = 800
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Music_player')
icon = pygame.image.load('images_game/211867_note_music_icon.png')
pygame.display.set_icon(icon)
player = pygame.image.load('images_game/photo1679244934.jpeg')

music_sound = [
    pygame.mixer.Sound('Sounds/drake-21-savage-rich-flex-mp3.mp3'),
    pygame.mixer.Sound('Sounds/metro-boomin-travis-scott-young-thug-trance-mp3.mp3'),
    pygame.mixer.Sound('Sounds/instasamka-otklyuchayu-telefon-mp3.mp3')
]

selected_sound_index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                music_sound[selected_sound_index].play()
            elif event.key == pygame.K_DOWN:
                music_sound[selected_sound_index].stop()
            elif event.key == pygame.K_LEFT:
                selected_sound_index = (selected_sound_index - 1) % len(music_sound)
            elif event.key == pygame.K_RIGHT:
                selected_sound_index = (selected_sound_index + 1) % len(music_sound)

    screen.blit(player, (0, 0))
    pygame.display.update()
