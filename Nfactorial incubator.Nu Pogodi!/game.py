#!/usr/bin/env python

import pygame
from pygame import *
import pygame.freetype
from wolf import Wolf
from egg import *
import random

# Set constants
RESOLUTION = (600, 450)
PLAYER_POSITION = (200, 100)
TIME_PER_STEP = 1500
FONT_SIZE = 20
BG_COLOR = "#64B5F6"
TEXT_COLOR = "#E91E63"
MUSIC_PATH = "Sounds/zastavka.mp3"

# Define function to check if the egg should be caught
def catch_egg(egg, bodyIsLeft, armsIsUp):
    if egg.egg_location == EggLocation.LEFT_UP:
        return bodyIsLeft and armsIsUp
    elif egg.egg_location == EggLocation.LEFT_DOWN:
        return bodyIsLeft and not armsIsUp
    elif egg.egg_location == EggLocation.RIGHT_UP:
        return not bodyIsLeft and armsIsUp
    else:
        return not bodyIsLeft and not armsIsUp

# Define main function
def main():
    # Initialize pygame
    pygame.init()
    # Set random seed
    random.seed(None)
    # Set font
    font = pygame.freetype.Font(None, FONT_SIZE)
    # Set screen
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption("Nu Pogodi!")
    # Load images
    bg = image.load("images/background.png")
    chikens = image.load("images/chicken.png")
    # Create wolf object
    wolf = Wolf(PLAYER_POSITION)
    # Set initial wolf state
    bodyIsLeft = True
    armsIsUp = True
    # Create list of eggs
    eggs = []
    # Set initial time
    time = 0
    # Set clock
    timer = pygame.time.Clock()
    # Set running state
    running = True
    # Set initial score
    score = 0
    # Set high score
    high_score = 0
    # Load music
    pygame.mixer.music.load(MUSIC_PATH)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # Main game loop
    while 1:
        # Event handling loop
        for e in pygame.event.get():
            # Quit event
            if e.type == QUIT:
                pygame.quit()
                raise SystemExit("QUIT")
            # Keydown events
            if e.type == KEYDOWN and e.key == K_LEFT:
                bodyIsLeft = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                bodyIsLeft = False
            if e.type == KEYDOWN and e.key == K_UP:
                armsIsUp = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                armsIsUp = False
        # Draw background and wolf
        screen.fill(Color(BG_COLOR))
        screen.blit(chikens, (0, 0))
        wolf.draw(screen, bodyIsLeft, armsIsUp)
        # If the game is running, update time
        if running:
            time += timer.get_time()
            # If time has elapsed, update eggs and score
        if time > TIME_PER_STEP:
            time = 0
            shift = False
            for egg in eggs:
                should_catch = egg.update()
                if should_catch:
                    if catch_egg(egg, bodyIsLeft, armsIsUp):
                        score = score + 1
                        shift = True
                    else:
                        running = False
            if shift:
                eggs.pop(0)
            eggs.append(Egg())
        for egg in eggs:
            egg.draw(screen)
        # Draw score
        font.render_to(screen, (10, 10), f"Score: {score}", Color(TEXT_COLOR))
        # Draw high score
        font.render_to(screen, (10, 30), f"High Score: {high_score}", Color(TEXT_COLOR))
        # If the game is not running, update high score and reset game
        if not running:
            if score > high_score:
                high_score = score
            score = 0
            time = 0
            bodyIsLeft = True
            armsIsUp = True
            eggs = []
            running = True
            # Reset music
            pygame.mixer.music.rewind()
            pygame.mixer.music.play(-1)
        # Update display
        pygame.display.update()
        # Set frame rate
        timer.tick(60)

if __name__ == "__main__":
     main()
