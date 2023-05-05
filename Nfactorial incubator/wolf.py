from pygame import *


class Wolf(sprite.Sprite):
    def __init__(self, player_position):
        sprite.Sprite.__init__(self)
        self.bodyLeft = image.load('images/wlfbodylft.png')
        self.bodyRight = image.load('images/wlfbodyrght.png')
        self.armDownLeft = image.load('images/armdownleft.png')
        self.armDownRight = image.load('images/armdownrt.png')
        self.armUpLeft = image.load('images/armuplt.png')
        self.armUpRight = image.load('images/armuprght.png')

        self.player_position = player_position
        self.arms_position = (0, 0)

    def draw(self, screen, left, up):
        if left:
            screen.blit(self.bodyLeft, self.player_position)
            if up:
                screen.blit(self.armUpLeft, self.arms_position)
            else:
                screen.blit(self.armDownLeft, self.arms_position)
        else:
            screen.blit(self.bodyRight, self.player_position)
            if up:
                screen.blit(self.armUpRight, self.arms_position)
            else:
                screen.blit(self.armDownRight, self.arms_position)