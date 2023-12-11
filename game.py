import time
import pygame
from board_graphics import Graphics
from minimax import algorithm


class Game:
    def __init__(self):
        self.selected_piece = (-1, -1)
        self.board_square_size = 56

        # 0 = quit, 1 = white move, 2 = black move
        self.status = 1

        # 1 = white, 2 = black, 3 = white king, 4 = black king
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

        self.num_moves = 0

    """
    This drives the whole game
    """

    def main(self):
        # draw original board
        Graphics.draw_board(self.board_array)

        # loop while the window is not closed
        while self.status != 0:
            # self.AI_event_loop()
            self.event_loop()

    def AI_event_loop(self):
        noise = 0.25  # percentage from 0 to 1

        if self.status == 1:
            self.make_AI_move(True, True, 3, 1, 2, 0, noise)
            self.status = 2
            self.num_moves += 1
        if self.status == 2:
            self.make_AI_move(False, True, 4, 1, 1.5, 0, noise)
            self.status = 1
            self.num_moves += 1

        if self.num_moves >= 50:
            self.status = 0
            white_pieces = algorithm.num_pieces(
                self.board_array, 1
            ) + algorithm.num_pieces(self.board_array, 3)
            black_pieces = algorithm.num_pieces(
                self.board_array, 2
            ) + algorithm.num_pieces(self.board_array, 4)
            print(white_pieces, black_pieces)
            if black_pieces > white_pieces:
                print("*******")
            if black_pieces == white_pieces:
                print("TIE")

    """
    This is what loops repeatedly that monitors for user moves
    And initiates AI moves when it is its turn
    """

    def event_loop(self):
        # check if the current player has any moves left
        if self.is_win_or_lose():
            # game over
            time.sleep(5)
            self.status = 0
            return

        # AI MOVE:
        if self.status == 2:
            self.make_AI_move(False, True, 3, 1, 1.5, 0, 0)
            self.status = 1
            Graphics.draw_board(self.board_array)
            return

        # USER MOVE
        # gets mouse x,y coordinates
        mx, my = pygame.mouse.get_pos()
        location = [mx, my]

        # process all actions in this for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.white_made_selection(location)
                Graphics.draw_board(self.board_array)
                Graphics.draw_moves(
                    algorithm.get_valid_moves(
                        self.selected_piece[0], self.selected_piece[1], self.board_array
                    )
                )

    """
    When the user clicks with the mouse:
    Update selected_piece if they select their own piece
    Move selected_piece to the new location if it is a valid move
    """

    def white_made_selection(
        self,
        location,
    ):
        # make sure its white's move:
        if self.status != 1:
            return

        # x, y of selected piece from 0 to 7
        x = (int)(location[1] / self.board_square_size)
        y = (int)(location[0] / self.board_square_size)

        if self.board_array[x][y] == 0 and self.selected_piece != (-1, -1):
            # check if the move is valid:
            moves = algorithm.get_valid_moves(
                self.selected_piece[0], self.selected_piece[1], self.board_array
            )
            for x1, y1, rm in moves:
                if x1 == x and y1 == y:
                    self.board_array[x][y] = self.board_array[self.selected_piece[0]][
                        self.selected_piece[1]
                    ]
                    self.king_piece(x, y)
                    for x_rm, y_rm in rm:
                        self.board_array[x_rm][y_rm] = 0
                    self.board_array[self.selected_piece[0]][self.selected_piece[1]] = 0
                    self.selected_piece = (-1, -1)

                    # Make it the AI move next:
                    self.status = 2
                    break

        elif self.board_array[x][y] == 1 or self.board_array[x][y] == 3:
            self.selected_piece = (x, y)

    """
    Returns the result of the game if it is over, or return nothing if not
    Uses self.status to see whose turn it is, and to see if there are any moves left
    """

    def is_win_or_lose(self):
        playerPieces = [2, 4]
        if self.status == 1:
            playerPieces = [1, 3]

        for i in range(len(self.board_array)):
            for j in range(len(self.board_array[0])):
                if (
                    self.board_array[i][j] in playerPieces
                    and algorithm.get_valid_moves(i, j, self.board_array) != []
                ):
                    return False

        if self.status == 1:
            print("White has no moves, black wins!")
        else:
            print("Black has no moves, white wins!")
        return True

    def king_piece(self, x, y):
        if (self.board_array[x][y]) == 1 and x == 0:
            self.board_array[x][y] = 3
        elif (self.board_array[x][y]) == 2 and x == 7:
            self.board_array[x][y] = 4
        return

    """
    Makes the AI move using mini-max without pruning
    """

    def make_AI_move(self, isWhite, prune, depth, w1, w2, w3, noise):
        if prune:
            self.board_array = algorithm.alpha_beta(
                self.board_array,
                depth,
                float("-inf"),
                float("inf"),
                isWhite,
                w1,
                w2,
                w3,
                noise,
            )[1]
        else:
            self.board_array = algorithm.minimax(
                self.board_array, depth, isWhite, w1, w2, w3, noise
            )[1]


# start the game
if __name__ == "__main__":
    game = Game()
    game.main()
