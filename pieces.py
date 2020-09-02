import pygame

SKY_BLUE = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 100, 10)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (148, 0, 211)
RED = (255, 0, 0)

class allBlocks():
    def draw(self, window):
        for block in [self.block1, self.block2, self.block3, self.block4]:
            pygame.draw.rect(window, self.color, (block[0] + 1, block[1] + 1, 29, 29))

class i_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        self.block1, self.block2, self.block3, self.block4 = [x_pos[0], y_pos[0]], [x_pos[1], y_pos[1]], [x_pos[2], y_pos[2]], [x_pos[3], y_pos[3]]
        self.color = SKY_BLUE
        self.POR = [x_pos[0], 30]

class j_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        self.block1, self.block2, self.block3, self.block4 = [x_pos[0], y_pos[0]], [x_pos[1], y_pos[1]], [x_pos[2], y_pos[2]], [x_pos[3], y_pos[3]]
        self.color = ORANGE
        self.POR = [x_pos[0], 30]

class l_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        self.block1, self.block2, self.block3, self.block4 = [x_pos[0], y_pos[0]], [x_pos[1], y_pos[1]], [x_pos[2], y_pos[2]], [x_pos[3], y_pos[3]]
        self.color = BLUE
        self.POR = [x_pos[0], 30]

class o_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        self.block1, self.block2, self.block3, self.block4 = [x_pos[0], y_pos[0]], [x_pos[1], y_pos[1]], [x_pos[2], y_pos[2]], [x_pos[3], y_pos[3]]
        self.color = YELLOW
        self.POR = [x_pos[0], 30]

class s_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        self.block1, self.block2, self.block3, self.block4 = [x_pos[0], y_pos[0]], [x_pos[1], y_pos[1]], [x_pos[2], y_pos[2]], [x_pos[3], y_pos[3]]
        self.color = GREEN
        self.POR = [x_pos[0], 30]

class t_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        self.block1, self.block2, self.block3, self.block4 = [x_pos[0], y_pos[0]], [x_pos[1], y_pos[1]], [x_pos[2], y_pos[2]], [x_pos[3], y_pos[3]]
        self.color = PURPLE
        self.POR = [x_pos[0], 30]

class z_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        self.block1, self.block2, self.block3, self.block4 = [x_pos[0], y_pos[0]], [x_pos[1], y_pos[1]], [x_pos[2], y_pos[2]], [x_pos[3], y_pos[3]]
        self.color = RED
        self.POR = [x_pos[0], 30]

