import pygame
from constants import *
import board
import pieces as piece
import time
import random

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

def pick_block(color):
    if color == SKY_BLUE:
        return piece.i_block([275, 275 -  30, 275 - 60, 275 + 30], [0 for _ in range(4)])
    elif color == BLUE:
        return piece.j_block([245, 245 - 30, 245 + 30, 245 + 30], [30, 30, 30, 0])
    elif color == ORANGE:
        return piece.l_block([245, 245 + 30, 245 - 30,  245 - 30], [30, 30, 30, 0])
    elif color == YELLOW:
        return piece.o_block([275, 275, 275 - 30, 275 - 30], [30, 0, 30, 0])
    elif color == GREEN:
        return piece.t_block([245, 245, 245 - 30, 245 + 30], [0, 30, 30, 30])
    elif color == PURPLE:
        return piece.z_block([245, 245, 245 - 30, 245 + 30], [30, 0, 0, 30])
    elif color == RED:
        return piece.s_block([245, 245, 245 - 30, 245 + 30], [30, 0, 30, 0])

def main():

    #DEBUG mode
    DEBUG_MODE = True
    DEBUG_PAUSE = False

    #movement related variables
    timer = 40
    movement = 0
    delta_position = 0
    gravity = 0

    #oher variables
    RUN = True
    current_block = None
    blocks_list = None
    future_blocks = []
    set_blocks = []
    current_pos = 1

    while RUN:

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        #chooses the first block
        if not current_block:
            current_block = pick_block(random.choice([SKY_BLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED]))
            blocks_list = [current_block.block1, current_block.block2, current_block.block3, current_block.block4]

        #randomly chooses the next 3 future blocks
        if len(future_blocks) != 3:
            eight_sided_rolls = [random.choice([SKY_BLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED, "reroll"]) for roll in range(3)]
            if future_blocks and eight_sided_rolls[0] not in ["reroll", current_block.color]:
                future_blocks.append(pick_block(eight_sided_rolls[0]))
            elif not future_blocks:
                future_blocks.append(pick_block(random.choice([SKY_BLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED])))
            if len(future_blocks) == 1 and eight_sided_rolls[1] not in ["reroll", future_blocks[0].color]:
                future_blocks.append(pick_block(eight_sided_rolls[1]))
            elif len(future_blocks) == 1:
                future_blocks.append(pick_block(random.choice([SKY_BLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED])))
            if len(future_blocks) == 2 and eight_sided_rolls[2] not in ["reroll", future_blocks[1].color]:
                future_blocks.append(pick_block(eight_sided_rolls[2]))
            elif len(future_blocks) == 2:
                future_blocks.append(pick_block(random.choice([SKY_BLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED])))

        #DEBUG MODE
        if pygame.mouse.get_pressed()[0] and DEBUG_MODE:
            x, y =pygame.mouse.get_pos()
            print(x, y)
        if keys[pygame.K_p] and DEBUG_MODE:
            if DEBUG_PAUSE:
                DEBUG_PAUSE = False
            else:
                DEBUG_PAUSE = True

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if current_block.side_collision(set_blocks) == "left":
                pass
            elif min([block[0] for block in blocks_list]) - 30 >= 125 and movement >= 5:
                for block in blocks_list:
                    block[0] -= 30
                current_block.POR[0] -= 30
                movement = 0
            else:
                movement += 1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if current_block.side_collision(set_blocks) == "right":
                pass
            elif max([block[0] for block in blocks_list]) + 30 < 425 and movement >= 5:
                for block in blocks_list:
                    block[0] += 30
                current_block.POR[0] += 30
                movement = 0
            else:
                movement += 1
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            changed = current_block.changePosition(current_pos, set_blocks)
            if current_pos == 4 and delta_position >= 3 and changed:
                current_pos = 1
                delta_position = 0
            elif delta_position >= 3 and changed:
                current_pos += 1
                delta_position = 0
            else:
                delta_position += 1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            timer += 8
        elif keys[pygame.K_SPACE]:
            if gravity >= 4:
                SELF = current_block
                while not current_block.underneath(set_blocks) and max([block[1] for block in blocks_list]) + 30 <= 570:
                    for block in blocks_list:
                        block[1] += 30
                for block in [[blocks_list[index], SELF.color] for index in range(4)]:
                    set_blocks.append(block)
                current_block = future_blocks[0]
                blocks_list = [current_block.block1, current_block.block2, current_block.block3, current_block.block4]
                future_blocks.pop(0)
                gravity = 0
                current_pos = 1
                board.row_filled(set_blocks)
            else:
                gravity +=1

        if timer >= 50 and not DEBUG_PAUSE:
            if current_block.fall(set_blocks, current_block):
                current_pos = 1
                current_block = None
                blocks_list = None
                board.row_filled(set_blocks)
                current_block = future_blocks[0]
                future_blocks.pop(0)
                blocks_list = [current_block.block1, current_block.block2, current_block.block3, current_block.block4]
            else:
                current_block.POR[1] += 30
            timer = 0
        else:
            timer += 1

        board.board_(WINDOW, PIECE_SIZE, current_block, set_blocks, future_blocks)
        clock.tick(60)

    pygame.quit()

clock = pygame.time.Clock()
main()
