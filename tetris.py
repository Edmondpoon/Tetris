import pygame
import pieces as piece
import time
import random

WIDTH = 550
HEIGHT = 600
PIECE_SIZE = 30

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (148, 0, 211)
ORANGE = (255, 100, 10)
SKY_BLUE = (0, 255, 255)

pygame.init()
FONT = pygame.font.SysFont("comicsans", 40)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def row_filled(set_blocks):
    highest_row = 20 - min([block[0][1] for block in set_blocks])
    removed_rows = []
    for y_value in [y * 30 for y in range(highest_row, 20)]:
        if len([True for block in set_blocks if block[0][1] == y_value]) == 10:
            removed_rows.append(y_value)
    for y_value in removed_rows:
        removed_blocks = []
        for block in set_blocks:
            if block[0][1] == y_value:
                removed_blocks.append(block)
        for block in removed_blocks:
            set_blocks.remove(block)
        for block in set_blocks:
            if block[0][1] < y_value:
                block[0][1] += 30

def underneath(current_block, set_blocks):
    SELF = current_block[0]
    for set_block in set_blocks:
        for block in [SELF.block1, SELF.block2, SELF.block3, SELF.block4]:
            if set_block[0][0] == block[0] and set_block[0][1] <= block[1] + 30:
                return True
    return False

def board(window, piece_size, current_block, set_blocks, future_blocks):
    window.fill(BLACK)

    NEXT_TEXT = FONT.render("NEXT", True, WHITE)
    window.blit(NEXT_TEXT, (450, 50))
    pygame.draw.rect(window, WHITE, (445, 90, 85, 200), 2)

    if len(future_blocks) == 3:
        first_future = future_blocks[0]
        second_future = future_blocks[1]
        third_future = future_blocks[2]
        placements = {BLUE : {1 : [[463, 463, 479, 495], [115, 131, 131, 131]], 2 : [[463, 463, 479, 495], [176, 192, 192, 192]], 3 : [[463, 463, 479, 495], [237, 253, 253, 253]], 4 : []},
                    SKY_BLUE : {1 : [[455, 471, 487, 503], [115 for _ in range(4)]], 2 : [[455, 471, 487, 503], [176 for _ in range(4)]], 3 : [[455, 471, 487, 503], [237 for _ in range(4)]], 4 : []},
                    ORANGE : {1 : [[463, 479, 495, 495], [131, 131, 131, 115]], 2 : [[463, 479, 495, 495], [192, 192, 192, 176]], 3 : [[463, 479, 495, 495], [253, 253, 253, 237]], 4 : []},
                    YELLOW : {1 : [[471, 471, 487, 487], [131, 115, 131, 115]], 2 : [[471, 471, 487, 487], [192, 176, 192, 176]], 3 : [[471, 471, 487, 487], [253, 237, 253, 237]], 4 : []},
                    GREEN : {1 : [[463, 479, 479, 495], [131, 115, 131, 115]], 2 : [[463, 479, 479, 495], [192, 176, 192, 176]], 3 : [[463, 479, 479, 495], [253, 237, 253, 237]], 4 : []},
                    PURPLE : {1 : [[463, 479, 479, 495], [131, 115, 131, 131]], 2 : [[463, 479, 479, 495], [192, 176, 192, 192]], 3 : [[463, 479, 479, 495], [253, 237, 253, 253]], 4 : []},
                    RED : {1 : [[463, 479, 479, 495], [115, 115, 131, 131]], 2 : [[463, 479, 479, 495], [176, 176, 192, 192]], 3 : [[463, 479, 479, 495], [237, 237, 253, 253]], 4 : []}}
        for block in range(4):
            pygame.draw.rect(window, first_future.color, (placements[first_future.color][1][0][block], placements[first_future.color][1][1][block], 15, 15))
            if [first_future.color, second_future.color, third_future.color] == [SKY_BLUE for _ in range(3)]:
                pygame.draw.rect(window, second_future.color, (placements[second_future.color][2][0][block], placements[second_future.color][2][1][block] - 15, 15, 15))
                pygame.draw.rect(window, third_future.color, (placements[third_future.color][3][0][block], placements[third_future.color][3][1][block] - 30, 15, 15))
            elif [first_future.color, second_future.color] == [SKY_BLUE, SKY_BLUE]:
                pygame.draw.rect(window, second_future.color, (placements[second_future.color][2][0][block], placements[second_future.color][2][1][block] - 15, 15, 15))
                pygame.draw.rect(window, third_future.color, (placements[third_future.color][3][0][block], placements[third_future.color][3][1][block] - 30, 15, 15))
            elif first_future.color == SKY_BLUE:
                pygame.draw.rect(window, second_future.color, (placements[second_future.color][2][0][block], placements[second_future.color][2][1][block] - 15, 15, 15))
                pygame.draw.rect(window, third_future.color, (placements[third_future.color][3][0][block], placements[third_future.color][3][1][block] - 15, 15, 15))
            elif second_future.color == SKY_BLUE: 
                pygame.draw.rect(window, second_future.color, (placements[second_future.color][2][0][block], placements[second_future.color][2][1][block], 15, 15))
                pygame.draw.rect(window, third_future.color, (placements[third_future.color][3][0][block], placements[third_future.color][3][1][block] - 15, 15, 15))
            else:
                pygame.draw.rect(window, second_future.color, (placements[second_future.color][2][0][block], placements[second_future.color][2][1][block], 15, 15))
                pygame.draw.rect(window, third_future.color, (placements[third_future.color][3][0][block], placements[third_future.color][3][1][block], 15, 15))


    for block in set_blocks:
        pygame.draw.rect(window, block[1], (block[0][0] + 1, block[0][1] + 1, 29, 29))

    for row in range(20):
        for column in range(11):
            if column != 10 and column != 0:
                pygame.draw.line(window, GREY, ((column * piece_size) + 125, 0), ((column * piece_size) + 125, 600))
            elif column == 10:
                pygame.draw.line(window, GREY, ((column * piece_size) + 125, 0), ((column * piece_size) + 125, 600), 2)
            elif column == 0:
                pygame.draw.line(window, GREY, ((column * piece_size) + 125, 0), ((column * piece_size) + 125, 600), 2)
    for row in range(21):
        if row not in [20, 0]:
            pygame.draw.line(window, GREY, (125, row * piece_size), (425, row * piece_size))
        elif row == 0:
            pygame.draw.line(window, GREY, (125, row * piece_size), (425, row * piece_size), 2)
        else:
            pygame.draw.line(window, GREY, (125, (row * piece_size) - 2), (425, (row * piece_size) - 2), 2)

    if current_block != []:
        current_block[0].draw(window)

    pygame.display.update()

def fall(current_block, set_blocks):
    SELF = current_block[0]
    if not underneath(current_block, set_blocks):
        if max([block[1] for block in [SELF.block1, SELF.block2, SELF.block3, SELF.block4]]) + 30 <= 570:
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
    blocks = [SELF.block1, SELF.block2, SELF.block3, SELF.block4]
    x, y = SELF.POR[0], SELF.POR[1]
    dif_blocks = {SKY_BLUE : {1 : [[x, y - 30], [x + 30, y - 30], [x - 30, y - 30], [x - 60, y - 30]], 2 : [[x, y - 30], [x, y + 30], [x, y], [x, y - 60]], 3 : [[x, y], [x + 30, y], [x - 30, y], [x - 60, y]], 4 : [[x - 30, y], [x - 30, y - 30], [x - 30, y - 60], [x - 30, y + 30]]},
                BLUE : {1 : [[x, y], [x - 30, y], [x - 30, y - 30], [x + 30, y]], 2 : [[x, y], [x, y - 30], [x, y + 30], [x + 30, y - 30]], 3 : [[x, y], [x - 30, y], [x + 30, y], [x + 30, y + 30]], 4 : [[x , y], [x, y - 30], [x, y + 30], [x - 30, y + 30]]}, 
                ORANGE : {1 : [[x, y], [x - 30, y], [x + 30, y], [x + 30, y - 30]], 2 : [[x, y], [x, y - 30], [x, y + 30], [x + 30, y + 30]], 3 : [[x, y], [x - 30, y], [x + 30, y], [x - 30, y + 30]], 4 : [[x, y], [x, y + 30], [x, y - 30], [x - 30, y - 30]]}, 
                YELLOW : {1 : [[x, y], [x - 30, y], [x - 30, y - 30], [x, y- 30]], 2 : [[x, y], [x - 30, y], [x - 30, y - 30], [x, y- 30]], 3 : [[x, y], [x - 30, y], [x - 30, y - 30], [x, y- 30]], 4 : [[x, y], [x - 30, y], [x - 30, y - 30], [x, y- 30]]}, 
                GREEN : {1 : [[x, y], [x - 30, y], [x, y - 30], [x + 30, y - 30]], 2 : [[x, y], [x, y - 30], [x + 30, y], [x + 30, y + 30]], 3 : [[x, y], [x + 30, y], [x, y + 30], [x - 30, y + 30]], 4 : [[x, y], [x - 30, y], [x - 30, y - 30], [x, y + 30]]},
                PURPLE : {1 : [[x, y], [x - 30, y], [x + 30, y], [x, y - 30]], 2 : [[x, y], [x, y - 30], [x, y + 30], [x + 30, y]], 3 : [[x, y], [x - 30, y], [x + 30, y], [x, y + 30]], 4 : [[x, y], [x, y - 30], [x, y + 30], [x - 30, y]]}, 
                RED : {1 : [[x, y], [x + 30, y], [x, y - 30], [x - 30, y - 30]], 2 : [[x, y], [x + 30, y], [x, y + 30], [x + 30, y - 30]], 3 : [[x, y], [x - 30, y], [x, y + 30], [x + 30, y + 30]], 4 : [[x, y], [x, y - 30], [x - 30, y], [x - 30, y + 30]]}} 
    POSITION = dif_blocks[SELF.color]
    for pos in range(4):
        for axis in range(2):
            if blocks[pos][axis] - POSITION[current_pos][pos][axis] > 0:
                blocks[pos][axis] -= (blocks[pos][axis] - POSITION[current_pos][pos][axis])
            elif blocks[pos][axis] - POSITION[current_pos][pos][axis] < 0:
                blocks[pos][axis] += (POSITION[current_pos][pos][axis] - blocks[pos][axis])

def main():
    DEBUG_MODE = True
    DEBUG_PAUSE = False
    RUN = True
    CURRENT_BLOCK = []
    FUTURE_BLOCKS = []
    SET_BLOCKS = []
    current_pos = 1
    timer = 40
    movement = 0
    delta_position = 0
    gravity = 0

    while RUN:

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        if len(FUTURE_BLOCKS) != 3:
            chosen_block = random.random()
            if chosen_block <= 0.142857142857143:
                FUTURE_BLOCKS.append(piece.i_block([275, 275 -  30, 275 - 60, 275 + 30], [0 for _ in range(4)]))
            elif chosen_block <= 0.285714285714286:
                FUTURE_BLOCKS.append(piece.j_block([245, 245 - 30, 245 + 30, 245 + 30], [30, 30, 30, 0]))
            elif chosen_block <= 0.428571428571429:
                FUTURE_BLOCKS.append(piece.l_block([245, 245 + 30, 245 - 30,  245 - 30], [30, 30, 30, 0]))
            elif chosen_block <= 0.571428571428571:
                FUTURE_BLOCKS.append(piece.o_block([275, 275, 275 - 30, 275 - 30], [30, 0, 30, 0]))
            elif chosen_block <= 0.714285714285714:
                FUTURE_BLOCKS.append(piece.t_block([245, 245, 245 - 30, 245 + 30], [0, 30, 30, 30]))
            elif chosen_block <= 0.857142857142857:
                FUTURE_BLOCKS.append(piece.z_block([245, 245, 245 - 30, 245 + 30], [30, 0, 0, 30]))
            elif chosen_block < 1:
                FUTURE_BLOCKS.append(piece.s_block([245, 245, 245 - 30, 245 + 30], [30, 0, 30, 0]))

        if CURRENT_BLOCK == []:
            CURRENT_BLOCK = [FUTURE_BLOCKS[0]]
            FUTURE_BLOCKS.pop(0)

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
            if CURRENT_BLOCK[0].side_collision(SET_BLOCKS) == "left":
                pass
            elif min([block[0] for block in [CURRENT_BLOCK[0].block1, CURRENT_BLOCK[0].block2, CURRENT_BLOCK[0].block3, CURRENT_BLOCK[0].block4]]) - 30 >= 125 and movement >= 5:
                for block in [CURRENT_BLOCK[0].block1, CURRENT_BLOCK[0].block2, CURRENT_BLOCK[0].block3, CURRENT_BLOCK[0].block4]:
                    block[0] -= 30
                CURRENT_BLOCK[0].POR[0] -= 30
                movement = 0
            else:
                movement += 1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if CURRENT_BLOCK[0].side_collision(SET_BLOCKS) == "right":
                pass
            elif max([block[0] for block in [CURRENT_BLOCK[0].block1, CURRENT_BLOCK[0].block2, CURRENT_BLOCK[0].block3, CURRENT_BLOCK[0].block4]]) + 30 < 425 and movement >= 5:
                for block in [CURRENT_BLOCK[0].block1, CURRENT_BLOCK[0].block2, CURRENT_BLOCK[0].block3, CURRENT_BLOCK[0].block4]:
                    block[0] += 30
                CURRENT_BLOCK[0].POR[0] += 30
                movement = 0
            else:
                movement += 1
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if current_pos == 4 and delta_position >= 3:
                current_pos = 1
                delta_position = 0
            elif delta_position >= 3:
                current_pos += 1
                delta_position = 0
            else:
                delta_position += 1
            changePosition(current_pos, CURRENT_BLOCK)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            timer += 8
        elif keys[pygame.K_SPACE]:
            if gravity >= 4:
                SELF = CURRENT_BLOCK[0]
                while not underneath(CURRENT_BLOCK, SET_BLOCKS) and max([block[1] for block in [SELF.block1, SELF.block2, SELF.block3, SELF.block4]]) + 30 <= 570:
                    for block in [SELF.block1, SELF.block2, SELF.block3, SELF.block4]:
                        block[1] += 30
                for block in [[SELF.block1, SELF.color],[SELF.block2, SELF.color], [SELF.block3, SELF.color], [SELF.block4, SELF.color]]:
                    SET_BLOCKS.append(block)
                CURRENT_BLOCK.clear()
                CURRENT_BLOCK = [FUTURE_BLOCKS[0]]
                FUTURE_BLOCKS.pop(0)
                gravity = 0
                current_pos = 1
                row_filled(SET_BLOCKS)
            else:
                gravity +=1
        
        if timer >= 50 and not DEBUG_PAUSE:
            if fall(CURRENT_BLOCK, SET_BLOCKS):
                current_pos = 1
                row_filled(SET_BLOCKS)
            else:
                CURRENT_BLOCK[0].POR[1] += 30
            timer = 0
        else:
            timer += 1

        board(WINDOW, PIECE_SIZE, CURRENT_BLOCK, SET_BLOCKS, FUTURE_BLOCKS)
        clock.tick(60)

    pygame.quit()

clock = pygame.time.Clock()
main()
