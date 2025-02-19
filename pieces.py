import pygame
from constants import SKY_BLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED

def pick_block(color):
    if color == SKY_BLUE:
        return i_block([275, 275 -  30, 275 - 60, 275 + 30], [0 for _ in range(4)])
    elif color == BLUE:
        return j_block([245, 245 - 30, 245 + 30, 245 + 30], [30, 30, 30, 0])
    elif color == ORANGE:
        return l_block([245, 245 + 30, 245 - 30,  245 - 30], [30, 30, 30, 0])
    elif color == YELLOW:
        return o_block([275, 275, 275 - 30, 275 - 30], [30, 0, 30, 0])
    elif color == GREEN:
        return t_block([245, 245, 245 - 30, 245 + 30], [0, 30, 30, 30])
    elif color == PURPLE:
        return z_block([245, 245, 245 - 30, 245 + 30], [30, 0, 0, 30])
    elif color == RED:
        return s_block([245, 245, 245 - 30, 245 + 30], [30, 0, 30, 0])

def end_game(set_blocks, current_block):
    for block in current_block:
        if block in [set_block[0] for set_block in set_blocks]:
            return True
    return False


class allBlocks():
    def __init__(self, x_pos, y_pos):
        self.block1, self.block2, self.block3, self.block4 = [x_pos[0], y_pos[0]], [x_pos[1], y_pos[1]], [x_pos[2], y_pos[2]], [x_pos[3], y_pos[3]]
        self.blocks = [self.block1, self.block2, self.block3, self.block4]
        self.xreset = x_pos
        self.yreset = y_pos

    #draws the block
    def draw(self, window):
        for block in self.blocks:
            pygame.draw.rect(window, self.color, (block[0] + 1, block[1] + 1, 29, 29))

    #checks if there will be collision if you move left/right
    def side_collision(self, set_blocks):
        SET_BLOCKS = [block[0] for block in set_blocks]
        for block in self.blocks:
            if [block[0] + 30, block[1]] in SET_BLOCKS:
                return "right"
            elif [block[0] - 30, block[1]] in SET_BLOCKS:
                return "left"

    #checks if there is a block under the current block
    def underneath(self, set_blocks, outline):
        if not outline:
            SET_BLOCKS = [block[0] for block in set_blocks]
            for block in self.blocks:
                if [block[0], block[1] + 30] in SET_BLOCKS:
                    return True
            return False
        else:
            SET_BLOCKS = [block[0] for block in set_blocks]
            for block in outline:
                if [block[0], block[1] + 30] in SET_BLOCKS:
                    return True
            return False
            

    #moves the block one space down unless it hits another block or reaches the bottom, where it will change the current block instead
    def fall(self, set_blocks):
        if not self.underneath(set_blocks, None):
            if max([block[1] for block in self.blocks]) + 30 <= 570:
                for block in self.blocks:
                    block[1] += 30
                return False
            else:
                for block in [[self.blocks[index], self.color] for index in range(4)]:
                    set_blocks.append(block)
                return True
        else:
            for block in [[self.blocks[index], self.color] for index in range(4)]:
                set_blocks.append(block)
            return True

    #draws the outline of the block if it were to be dropped at any given moment
    def draw_outline(self, set_blocks, window):
        outline_pos = [[block[0], block[1]] for block in self.blocks]
        while not self.underneath(set_blocks, outline_pos) and max([block[1] for block in outline_pos]) + 30 <= 570:
            for block in outline_pos:
                block[1] += 30

        for block in outline_pos:
            pygame.draw.rect(window, self.color, (block[0] + 1, block[1] + 1, 29, 29), 1)
        

    #changes the positions of the 4 blocks that comprise of the whole block
    def changePosition(self, current_pos, set_blocks):
        x, y = self.POR[0], self.POR[1]
        dif_blocks = {SKY_BLUE : {1 : [[x, y - 30], [x + 30, y - 30], [x - 30, y - 30], [x - 60, y - 30]], 2 : [[x, y - 30], [x, y + 30], [x, y], [x, y - 60]], 3 : [[x, y], [x + 30, y], [x - 30, y], [x - 60, y]], 4 : [[x - 30, y], [x - 30, y - 30], [x - 30, y - 60], [x - 30, y + 30]]},
                    BLUE : {1 : [[x, y], [x - 30, y], [x - 30, y - 30], [x + 30, y]], 2 : [[x, y], [x, y - 30], [x, y + 30], [x + 30, y - 30]], 3 : [[x, y], [x - 30, y], [x + 30, y], [x + 30, y + 30]], 4 : [[x , y], [x, y - 30], [x, y + 30], [x - 30, y + 30]]},
                    ORANGE : {1 : [[x, y], [x - 30, y], [x + 30, y], [x + 30, y - 30]], 2 : [[x, y], [x, y - 30], [x, y + 30], [x + 30, y + 30]], 3 : [[x, y], [x - 30, y], [x + 30, y], [x - 30, y + 30]], 4 : [[x, y], [x, y + 30], [x, y - 30], [x - 30, y - 30]]},
                    YELLOW : {1 : [[x, y], [x - 30, y], [x - 30, y - 30], [x, y- 30]], 2 : [[x, y], [x - 30, y], [x - 30, y - 30], [x, y - 30]], 3 : [[x, y], [x - 30, y], [x - 30, y - 30], [x, y- 30]], 4 : [[x, y], [x - 30, y], [x - 30, y - 30], [x, y- 30]]},
                    GREEN : {1 : [[x, y], [x - 30, y], [x, y - 30], [x + 30, y - 30]], 2 : [[x, y], [x, y - 30], [x + 30, y], [x + 30, y + 30]], 3 : [[x, y], [x + 30, y], [x, y + 30], [x - 30, y + 30]], 4 : [[x, y], [x - 30, y], [x - 30, y - 30], [x, y + 30]]},
                    PURPLE : {1 : [[x, y], [x - 30, y], [x + 30, y], [x, y - 30]], 2 : [[x, y], [x, y - 30], [x, y + 30], [x + 30, y]], 3 : [[x, y], [x - 30, y], [x + 30, y], [x, y + 30]], 4 : [[x, y], [x, y - 30], [x, y + 30], [x - 30, y]]},
                    RED : {1 : [[x, y], [x + 30, y], [x, y - 30], [x - 30, y - 30]], 2 : [[x, y], [x + 30, y], [x, y + 30], [x + 30, y - 30]], 3 : [[x, y], [x - 30, y], [x, y + 30], [x + 30, y + 30]], 4 : [[x, y], [x, y - 30], [x - 30, y], [x - 30, y + 30]]}}
        POSITION = dif_blocks[self.color]
        checks = []
        for pos in range(4):
            current_point = []
            for axis in range(2):
                if self.blocks[pos][axis] - POSITION[current_pos][pos][axis] > 0:
                    current_point.append(self.blocks[pos][axis] - (self.blocks[pos][axis] - POSITION[current_pos][pos][axis]))
                elif self.blocks[pos][axis] - POSITION[current_pos][pos][axis] < 0:
                    current_point.append(self.blocks[pos][axis] + (POSITION[current_pos][pos][axis] - self.blocks[pos][axis]))
                elif self.blocks[pos][axis] - POSITION[current_pos][pos][axis] == 0:
                    current_point.append(self.blocks[pos][axis])
            checks.append(current_point)
        if not [False for block in checks if block[0] < 125 or block[0] >= 425 or block in [block[0] for block in set_blocks] or block[1] > 570 or block[1] < 0]:
            for pos in range(4):
                for axis in range(2):
                    if self.blocks[pos][axis] - POSITION[current_pos][pos][axis] > 0:
                        self.blocks[pos][axis] -= (self.blocks[pos][axis] - POSITION[current_pos][pos][axis])
                    elif self.blocks[pos][axis] - POSITION[current_pos][pos][axis] < 0:
                        self.blocks[pos][axis] += (POSITION[current_pos][pos][axis] - self.blocks[pos][axis])
            return True
        change_in_POR = {SKY_BLUE : 60,
                        BLUE : 30,
                        ORANGE : 30,
                        YELLOW : 0,
                        GREEN : 30,
                        PURPLE : 30,
                        RED : 30}
        if max([block[0] for block in checks]) >= 425:
            if len([True for block in checks if [block[0] - change_in_POR[self.color], block[1]] not in [block[0] for block in set_blocks]]) == 4:
                self.POR[0] -= change_in_POR[self.color] 
        elif min([block[0] for block in checks]) < 125:
            if len([True for block in checks if [block[0] + change_in_POR[self.color], block[1]] not in [block[0] for block in set_blocks]]) == 4:
                self.POR[0] += change_in_POR[self.color] 
        elif [True for block in checks if block in [block[0] for block in set_blocks]]:
            if [True for block in self.blocks if [block[0] + 30, block[1]] in [block[0] for block in set_blocks]]:
                if len([True for block in checks if [block[0] - change_in_POR[self.color], block[1]] not in [block[0] for block in set_blocks]]) == 4:
                    self.POR[0] -= change_in_POR[self.color]
            elif [True for block in self.blocks if [block[0] - 30, block[1]] in [block[0] for block in set_blocks]]:
                if len([True for block in checks if [block[0] + change_in_POR[self.color], block[1]] not in [block[0] for block in set_blocks]]) == 4:
                    self.POR[0] += change_in_POR[self.color]
        return False

    def reset(self):
        self.block1, self.block2, self.block3, self.block4 = [self.xreset[0], self.yreset[0]], [self.xreset[1], self.yreset[1]], [self.xreset[2], self.yreset[2]], [self.xreset[3], self.yreset[3]]
        self.blocks = [self.block1, self.block2, self.block3, self.block4]
        self.POR = [self.xreset[0], 30]


class i_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.color = SKY_BLUE
        self.POR = [x_pos[0], 30]

class j_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.color = ORANGE
        self.POR = [x_pos[0], 30]

class l_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.color = BLUE
        self.POR = [x_pos[0], 30]

class o_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.color = YELLOW
        self.POR = [x_pos[0], 30]

class s_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.color = GREEN
        self.POR = [x_pos[0], 30]

class t_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.color = PURPLE
        self.POR = [x_pos[0], 30]

class z_block(allBlocks):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.color = RED
        self.POR = [x_pos[0], 30]

