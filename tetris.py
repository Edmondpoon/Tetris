import pygame
import scores
from constants import *
import board
import pieces as piece
import time
import random

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

def main():

    #DEBUG mode
    DEBUG_MODE = True
    DEBUG_PAUSE = False

    #movement related variables
    timer = 40
    block_speed = 75
    movement = 0
    delta_position = 1
    gravity = 1
    current_pos = 1
    block_switch = 1

    #point system
    level = 0
    rows_cleared = 0
    score = 0

    #other variables
    RUN = True
    current_block = None
    blocks_list = None
    future_blocks = [] #list of 3 future blocks
    set_blocks = [] #list of all set blocks
    held_block = [None, False] #list of block and whether it has been swapped this turn
    while RUN:

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        #chooses the first block
        if not current_block:
            current_block = piece.pick_block(random.choice([SKY_BLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED]))
            blocks_list = [current_block.block1, current_block.block2, current_block.block3, current_block.block4]

        #randomly chooses the next 3 future blocks
        if len(future_blocks) != 3:
            eight_sided_rolls = [random.choice([SKY_BLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED, "reroll"]) for roll in range(3)]
            if future_blocks and eight_sided_rolls[0] not in ["reroll", current_block.color]:
                future_blocks.append(piece.pick_block(eight_sided_rolls[0]))
            elif future_blocks:
                future_blocks.append(piece.pick_block(random.choice([SKY_BLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED])))
            elif not future_blocks:
                future_blocks.append(piece.pick_block(random.choice([SKY_BLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED])))
            if len(future_blocks) == 1 and eight_sided_rolls[1] not in ["reroll", future_blocks[0].color] and len(future_blocks) != 3:
                future_blocks.append(piece.pick_block(eight_sided_rolls[1]))
            elif len(future_blocks) == 1 and len(future_blocks) != 3:
                future_blocks.append(piece.pick_block(random.choice([SKY_BLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED])))
            if len(future_blocks) == 2 and eight_sided_rolls[2] not in ["reroll", future_blocks[1].color] and len(future_blocks) != 3:
                future_blocks.append(piece.pick_block(eight_sided_rolls[2]))
            elif len(future_blocks) == 2 and len(future_blocks) != 3:
                future_blocks.append(piece.pick_block(random.choice([SKY_BLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED])))

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
                while not current_block.underneath(set_blocks, None) and max([block[1] for block in blocks_list]) + 30 <= 570:
                    for block in blocks_list:
                        block[1] += 30
                for block in [[blocks_list[index], current_block.color] for index in range(4)]:
                    set_blocks.append(block)
                if piece.end_game(set_blocks, future_blocks[0].blocks):
                    RUN = False
                else:
                    current_block = future_blocks[0]
                    blocks_list = [current_block.block1, current_block.block2, current_block.block3, current_block.block4]
                    future_blocks.pop(0)
                    gravity = 0
                    current_pos = 1
                    delta_rows = board.row_filled(set_blocks)
                    if delta_rows[0]:
                        rows_cleared += delta_rows[1]
                    level = rows_cleared // 10
                    block_speed = (25 / ((level + 1)) * 0.5) + 25
                    score = scores.score_change(level, delta_rows[1], score)
                    held_block[1] = False
            else:
                gravity +=1
        elif keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            if held_block[0] and not held_block[1] and block_switch >= 4:
                held_block, current_block = [current_block, True], held_block[0]
                current_block.reset()
                held_block[0].reset()
                blocks_list = [current_block.block1, current_block.block2, current_block.block3, current_block.block4]
            elif held_block[0] and not held_block[1]:
                block_switch += 1
            elif not held_block[0]:
                held_block, current_block = [current_block, True], future_blocks[0]
                blocks_list = [current_block.block1, current_block.block2, current_block.block3, current_block.block4]
                future_blocks.pop(0)  

        if timer >= block_speed and not DEBUG_PAUSE:
            if current_block.fall(set_blocks):
                current_pos = 1
                current_block = None
                blocks_list = None
                delta_rows = board.row_filled(set_blocks)
                if delta_rows[0]:
                    rows_cleared += delta_rows[1]
                level = rows_cleared // 10
                block_speed = (25 / ((level + 1) * 0.5)) + 25
                score = scores.score_change(level, delta_rows[1], score)
                if piece.end_game(set_blocks, future_blocks[0].blocks):
                    RUN = False
                else:
                    current_block = future_blocks[0]
                    future_blocks.pop(0)
                    blocks_list = [current_block.block1, current_block.block2, current_block.block3, current_block.block4]
                    held_block[1] = False
            else:
                current_block.POR[1] += 30
            timer = 0
        else:
            timer += 1

        board.board_(WINDOW, PIECE_SIZE, current_block, set_blocks, future_blocks, score, level, rows_cleared, held_block)
        clock.tick(60)
    
    print("You lost!")
    print("""Score: {},
Level: {},
Rows Cleared: {}""".format(score, level, rows_cleared))
    pygame.quit()

clock = pygame.time.Clock()
main()
