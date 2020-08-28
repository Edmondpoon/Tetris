import pygame
import time
import random

WIDTH = 500
HEIGHT = 600
PIECE_SIZE = 30

GREY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (180,255,100)
YELLOW = (255,255,0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (240,0,255)
ORANGE = (255,100,10)
SKY_BLUE = (0,255,255)


pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

class block():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = SKY_BLUE

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x + 1, self.y + 1, 29, 29))

    def underneath(self, set_blocks):
        for PLACEHOLDER in set_blocks:
            if PLACEHOLDER.x == self.x and PLACEHOLDER.y <=  self.y + 30:
                    return True
        return False

def board(window, piece_size, current_blocks, set_blocks):
    window.fill(BLACK)

    for PLACEHOLDER in set_blocks:
        PLACEHOLDER.draw(window)

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
    if current_blocks != []:    
        for PLACEHOLDER in current_blocks:
            PLACEHOLDER.draw(window)    

    pygame.display.update()

def fall(current_blocks, set_blocks):
    if not len([True for PLACEHOLDER in current_blocks if PLACEHOLDER.underneath(set_blocks)]):
        if min([PLACEHOLDER.y for PLACEHOLDER in current_blocks]) + 30 <= 570:
            for PLACEHOLDER in current_blocks:
                PLACEHOLDER.y += 30 
            return False
        else:
            for PLACEHOLDER in current_blocks:
                set_blocks.append(PLACEHOLDER)
            current_blocks.clear()
            return True
    else:
        for PLACEHOLDER in current_blocks:
            set_blocks.append(PLACEHOLDER)
        current_blocks.clear()
        return True

def main():
    RUN = True
    STARTx = (5 * 30) + 100
    STARTy = 0
    CURRENT_BLOCKS = []
    SET_BLOCKS = []
    CURRENT_POS = 1
    TIMER = 40

    while RUN:
        
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        if CURRENT_BLOCKS == []: 
            #RANDOM>RADNOM to choose block here
            if True:
                for x_pos in [STARTx, STARTx -  30, STARTx - 60, STARTx + 30]:
                    CURRENT_BLOCKS.append(block(x_pos, STARTy))

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if min([PLACEHOLDER.x for PLACEHOLDER in CURRENT_BLOCKS]) - 30 >= 100:
                for PLACEHOLDER in CURRENT_BLOCKS:
                    PLACEHOLDER.x -= 30
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if max([PLACEHOLDER.x for PLACEHOLDER in CURRENT_BLOCKS]) + 30 < 400:
                for PLACEHOLDER in CURRENT_BLOCKS:
                    PLACEHOLDER.x += 30
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if CURRENT_POS == 4:
                CURRENT_POS = 1
            else:
                CURRENT_POS += 1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            TIMER += 8
        elif keys[pygame.K_SPACE]:
        #clicking space makes block go to the bottom
            pass

        if TIMER >= 50:
            if fall(CURRENT_BLOCKS, SET_BLOCKS):
                CURRENT_POS = 1
            TIMER = 0
        else:
            TIMER += 1

        board(WINDOW, PIECE_SIZE, CURRENT_BLOCKS, SET_BLOCKS)
        clock.tick(60)

    pygame.quit()

clock = pygame.time.Clock()
main()
