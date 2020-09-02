import pygame
import pieces as piece
import time
import random

WIDTH = 500
HEIGHT = 600
PIECE_SIZE = 30

GREY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (180, 255, 100)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (240, 0, 255)
ORANGE = (255, 100, 10)
SKY_BLUE = (0, 255, 255)


pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def underneath(current_block, set_blocks):
    SELF = current_block[0]
    for set_block in set_blocks:
        for block in [SELF.block1, SELF.block2, SELF.block3, SELF.block4]:
            if set_block[0][0] == block[0] and set_block[0][1] <= block[1] + 30:
                return True
    return False

def board(window, piece_size, current_block, set_blocks):
    window.fill(BLACK)

    for block in set_blocks:
        pygame.draw.rect(window, block[1], (block[0][0] + 1, block[0][1] + 1, 29, 29))

    for row in range(20):
        for column in range(11):
            if column != 10 and column != 0:
                pygame.draw.line(window, GREY, ((column * piece_size) + 100 , 0), ((column * piece_size) + 100, 600))
            elif column == 10:
                pygame.draw.line(window, GREY, ((column * piece_size) + 100 , 0), ((column * piece_size) + 100, 600), 2)
            elif column == 0:
                pygame.draw.line(window, GREY, ((column * piece_size) + 100 , 0), ((column * piece_size) + 100, 600), 2)
    for row in range(21):
        if row not in [20, 0]:
            pygame.draw.line(window, GREY, (100, row * piece_size), (400, row * piece_size))
        elif row == 0:
            pygame.draw.line(window, GREY, (100, row * piece_size), (400, row * piece_size), 2)
        else:
            pygame.draw.line(window, GREY, (100, (row * piece_size) - 2), (400, (row * piece_size) - 2), 2)

    if current_block != []:
        current_block[0].draw(window)

    pygame.display.update()

def fall(current_block, set_blocks):
    SELF = current_block[0]
    if not underneath(current_block, set_blocks):
        if min([block[1] for block in [SELF.block1, SELF.block2, SELF.block3, SELF.block4]]) + 30 <= 570:
            for block in [SELF.block1, SELF.block2, SELF.block3, SELF.block4]:
                block[1] += 30
            return False
        else:
            for block in [[SELF.block1, SELF.color],[SELF.block2, SELF.color], [SELF.block3, SELF.color], [SELF.block4, SELF.color]]:
                set_blocks.append(block)
            current_block.clear()
            return True
    else:
        for block in [[SELF.block1, SELF.color],[SELF.block2, SELF.color], [SELF.block3, SELF.color], [SELF.block4, SELF.color]]:
            set_blocks.append(block)
        current_block.clear()
        return True

def changePosition(current_pos, current_block):
    SELF = current_block[0]
    blocks = [SELF[0].block1, SELF[0].block2, SELF[0].block3, SELF[0].block4]
    if SELF.color == SKY_BLUE:
        x, y = SELF.POR[0], SELF.POR[1]
        POSITION = {1 : [[x, y - 30], [x + 30, y - 30], [x - 30, y - 30], [x - 60, y - 30]], 2 : [[x, y - 30], [x, y + 30], [x, y], [x, y - 60]], 3 : [[x, y], [x + 30, y], [x - 30, y], [x - 60, y]], 4 : [[x - 30, y], [x - 30, y - 30], [x - 30, y - 60], [x - 30, y + 30]]}
        for pos in range(4):
            blocks[pos] = positions[current_pos][pos]
            the block positions dont change once it goes back to main function

def main():
    RUN = True
    STARTx = (5 * 30) + 100
    STARTy = 0
    CURRENT_BLOCK = []
    SET_BLOCKS = []
    CURRENT_POS = 1
    TIMER = 40

    while RUN:

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        if CURRENT_BLOCK == []:
            #randomize blocks here
            if True:
                CURRENT_BLOCK.append(piece.i_block([STARTx, STARTx -  30, STARTx - 60, STARTx + 30], [STARTy for _ in range(4)]))

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if min([block[0] for block in [CURRENT_BLOCK[0].block1, CURRENT_BLOCK[0].block2, CURRENT_BLOCK[0].block3, CURRENT_BLOCK[0].block4]]) - 30 >= 100:
                for block in [CURRENT_BLOCK[0].block1, CURRENT_BLOCK[0].block2, CURRENT_BLOCK[0].block3, CURRENT_BLOCK[0].block4]:
                    block[0] -= 30
                CURRENT_BLOCK[0].POR[0] -= 30
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if max([block[0] for block in [CURRENT_BLOCK[0].block1, CURRENT_BLOCK[0].block2, CURRENT_BLOCK[0].block3, CURRENT_BLOCK[0].block4]]) + 30 < 400:
                for block in [CURRENT_BLOCK[0].block1, CURRENT_BLOCK[0].block2, CURRENT_BLOCK[0].block3, CURRENT_BLOCK[0].block4]:
                    block[0] += 30
                CURRENT_BLOCK[0].POR[0] += 30
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if CURRENT_POS == 4:
                CURRENT_POS = 1
            else:
                CURRENT_POS += 1
            changePosition(CURRENT_POS, CURRENT_BLOCK)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            TIMER += 8
        elif keys[pygame.K_SPACE]:
        #clicking space makes block go to the bottom
            pass

        if TIMER >= 50:
            if fall(CURRENT_BLOCK, SET_BLOCKS):
                CURRENT_POS = 1
            else:
                CURRENT_BLOCK[0].POR[1] += 30
            TIMER = 0
        else:
            TIMER += 1

        board(WINDOW, PIECE_SIZE, CURRENT_BLOCK, SET_BLOCKS)
        clock.tick(60)

    pygame.quit()

clock = pygame.time.Clock()
main()
