import pygame
from constants import BLACK, BLUE, SKY_BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED, WHITE, GREY

pygame.init()
FONT = pygame.font.SysFont("comicsans", 40)
FONT2 = pygame.font.SysFont("comicsans", 35)
FONT3 = pygame.font.SysFont("comicsans", 30)

#clears rows that are filled
def row_filled(set_blocks):
    highest_row = 20 - min([block[0][1] for block in set_blocks])
    removed_rows = []

    #iterates through all the rows with blocks in them and determines whether theyre full or not 
    for y_value in [y * 30 for y in range(highest_row, 20)]:
        if len([True for block in set_blocks if block[0][1] == y_value]) == 10:
            removed_rows.append(y_value)

    #clears the filled rows and moves all the blocks above down one block
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
    return [True, len(removed_rows)] if removed_rows else [False, None]

#generates the board and configures the window
def board_(window, piece_size, current_block, set_blocks, future_blocks, score, level, rows_cleared, held_block):
    window.fill(BLACK)

    #sets up all the text present on the window
    NEXT_TEXT = FONT.render("NEXT", True, WHITE)
    HOLD_TEXT = FONT.render("HOLD", True, WHITE)
    SCORE_TEXT = FONT2.render("SCORE", True, WHITE)
    LEVEL_TEXT = FONT2.render("LEVEL", True, WHITE)
    LINES_TEXT = FONT2.render("LINES", True, WHITE)

    TSCORE_TEXT = FONT3.render(str(score), True, GREY)
    TLEVEL_TEXT = FONT3.render(str(level + 1), True, GREY)
    TLINES_TEXT = FONT3.render(str(rows_cleared), True, GREY)

    pygame.draw.rect(window, WHITE, (445, 90, 85, 200), 2)
    pygame.draw.rect(window, WHITE, (15, 350, 100, 220), 2)
    pygame.draw.rect(window, WHITE, (21, 90, 90, 60), 2)

    window.blit(NEXT_TEXT, (450, 50))
    window.blit(HOLD_TEXT, (25, 50))
    window.blit(SCORE_TEXT, (22, 360))
    window.blit(LEVEL_TEXT, (25, 430))
    window.blit(LINES_TEXT, (27, 500))

    number_placement = {1 : 55, 2 : 50, 3 : 45, 4 : 40, 5 : 35, 6 : 30, 7 : 25, 8 : 20}
    window.blit(TSCORE_TEXT, (number_placement[len(str(score))], 395))
    window.blit(TLEVEL_TEXT, (number_placement[len(str(level))], 465))
    window.blit(TLINES_TEXT, (number_placement[len(str(rows_cleared))], 535))

    #draws the future blocks in the "next blocks" section
    if len(future_blocks) == 3:
        first_future = future_blocks[0]
        second_future = future_blocks[1]
        third_future = future_blocks[2]
        placements = {BLUE : {1 : [[463, 463, 479, 495], [115, 131, 131, 131]], 2 : [[463, 463, 479, 495], [176, 192, 192, 192]], 3 : [[463, 463, 479, 495], [237, 253, 253, 253]]},
                    SKY_BLUE : {1 : [[455, 471, 487, 503], [115 for _ in range(4)]], 2 : [[455, 471, 487, 503], [176 for _ in range(4)]], 3 : [[455, 471, 487, 503], [237 for _ in range(4)]]},
                    ORANGE : {1 : [[463, 479, 495, 495], [131, 131, 131, 115]], 2 : [[463, 479, 495, 495], [192, 192, 192, 176]], 3 : [[463, 479, 495, 495], [253, 253, 253, 237]]},
                    YELLOW : {1 : [[471, 471, 487, 487], [131, 115, 131, 115]], 2 : [[471, 471, 487, 487], [192, 176, 192, 176]], 3 : [[471, 471, 487, 487], [253, 237, 253, 237]]},
                    GREEN : {1 : [[463, 479, 479, 495], [131, 115, 131, 115]], 2 : [[463, 479, 479, 495], [192, 176, 192, 176]], 3 : [[463, 479, 479, 495], [253, 237, 253, 237]]},
                    PURPLE : {1 : [[463, 479, 479, 495], [131, 115, 131, 131]], 2 : [[463, 479, 479, 495], [192, 176, 192, 192]], 3 : [[463, 479, 479, 495], [253, 237, 253, 253]]},
                    RED : {1 : [[463, 479, 479, 495], [115, 115, 131, 131]], 2 : [[463, 479, 479, 495], [176, 176, 192, 192]], 3 : [[463, 479, 479, 495], [237, 237, 253, 253]]}}

        #draws each future block depending on whether its the first, second, or third block
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

    #draws the held block if applicable
    placements = {BLUE : [[37, 37, 57, 77], [100, 120, 120, 120]],
                SKY_BLUE : [[27, 47, 67, 87], [110, 110, 110, 110]],
                ORANGE : [[37, 57, 77, 77], [120, 120, 120, 100]],
                YELLOW : [[47, 47, 67, 67], [120, 100, 120, 100]],
                GREEN : [[37, 57, 57, 77], [120, 100, 120, 100]],
                PURPLE : [[37, 57, 57, 77], [120, 100, 120, 120]],
                RED : [[37, 57, 57, 77], [100, 100, 120, 120]]}
    if held_block[0]:
        for block in range(4):
            pygame.draw.rect(window, held_block[0].color, (placements[held_block[0].color][0][block], placements[held_block[0].color][1][block], 19, 19))

    #draws all the blocks that have been placed
    for block in set_blocks:
        pygame.draw.rect(window, block[1], (block[0][0] + 1, block[0][1] + 1, 29, 29))

    #draws the lines that represent the borders and blocks of the game
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

    #draws the current block
    if current_block:
        current_block.draw(window)

    #draws placed block outline
    if current_block:
        current_block.draw_outline(set_blocks, window)
    pygame.display.update()
