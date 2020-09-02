import pygame

SKY_BLUE = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 100, 10)
YELLOW = (255, 255, 0)
GREEN = (180, 255, 100)
PURPLE = (240, 0, 255)
RED = (255, 0, 0)

class allBlocks():
    def draw(self, window):
        for block in [self.block1, self.block2, self.block3, self.block4]:
            if block != None:
                pygame.draw.rect(window, self.color, (block[0] + 1, block[1] + 1, 29, 29))

class i_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        self.block1, self.block2, self.block3, self.block4 = [x_pos[0], y_pos[0]], [x_pos[1], y_pos[1]], [x_pos[2], y_pos[2]], [x_pos[3], y_pos[3]]
        self.color = SKY_BLUE
        self.POR = [x_pos[0], 30]


