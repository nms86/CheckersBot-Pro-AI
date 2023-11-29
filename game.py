import pygame
import board_graphics

board_array = [
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
]


def main():
    pygame.init()

    # draw original board
    board_graphics.draw_board(board_array)

    status = True
    while status:
        # gets mouse x,y coordinates
        mx, my = pygame.mouse.get_pos()
        location = [mx, my]

        # process all actions in this for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board_array[5][0] = 0
                board_array[4][1] = 1
                board_graphics.draw_board(board_array)

    pygame.quit()


if __name__ == "__main__":
    main()
