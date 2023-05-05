from pygame import *
import random
from enum import Enum

# Define the positions of the eggs on the screen
LEFT_UP_POSITIONS = [(60, 120), (90, 140), (120, 160)]
LEFT_DOWN_POSITIONS = [(60, 260), (90, 275), (120, 290)]
RIGHT_UP_POSITIONS = [(520, 120), (495, 135), (460, 160)]
RIGHT_DOWN_POSITIONS = [(520, 260), (495, 270), (460, 290)]

EGG_POSITIONS = [LEFT_UP_POSITIONS, LEFT_DOWN_POSITIONS,
                 RIGHT_UP_POSITIONS, RIGHT_DOWN_POSITIONS]
# Define an enumeration to represent the location of the egg
class EggLocation(Enum):
    LEFT_UP = 0
    LEFT_DOWN = 1
    RIGHT_UP = 2
    RIGHT_DOWN = 3

# Define the Egg class
class Egg(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load('images/nwegg.png')
        self.egg_location = EggLocation(
            random.randint(0, len(EGG_POSITIONS)-1)) # Choose a random location for the egg
        self.positions = EGG_POSITIONS[self.egg_location.value] # Get the list of positions for the chosen location
        self.index = 0
        self.index = 0

    def update(self):
        self.index += 1
        return self.index >= len(self.positions) # Return True if the egg has been displayed at all positions

    def draw(self, screen):
        drawIndex = self.index
        if drawIndex >= len(self.positions):
            drawIndex = len(self.positions)-1
        screen.blit(self.image, self.positions[drawIndex]) # Draw the egg on the screen at the current position

        class BombEgg(Egg):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("images/bomb_egg.png")

            def update(self):
                should_catch = super().update()
                if should_catch:
                    # End the game
                    running = False
                return should_catch

        class FalseEgg(Egg):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("images/false_egg.png")

            def update(self):
                should_catch = super().update()
                if should_catch:
                    # Deduct points from score
                    score = max(0, score - 1)
                return should_catch