from enum import Enum
import pygame
from board_graphics import Graphics


class Game:
    def __init__(self):
        self.selected_piece = (-1, -1)

        # 0 = quit, 1 = white move, 2 = black move
        self.status = 1

        # 1 = white, 2 = black, 3 = white king, 3 = black king
        self.board_array = [
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
        ]

    def main(self):
        pygame.init()

        # draw original board
        Graphics.draw_board(self.board_array)

        while self.status != 0:
            self.event_loop()

        pygame.quit()

    def event_loop(self):
        # gets mouse x,y coordinates
        mx, my = pygame.mouse.get_pos()
        location = [mx, my]

        # process all actions in this for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # check if mouse is on white piece
                # if on black piece, check if valid move
                # if valid move, move the piece and update the board
                self.board_array[5][0] = 0
                self.board_array[4][1] = 1
                Graphics.draw_board(self.board_array)


# start the game
if __name__ == "__main__":
    game = Game()
    game.main()
