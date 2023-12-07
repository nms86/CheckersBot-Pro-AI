import time
import pygame
from board_graphics import Graphics
from copy import deepcopy


def helper():
    return


class Game:
    def __init__(self):
        self.selected_piece = (-1, -1)
        self.board_square_size = 56

        # 0 = quit, 1 = white move, 2 = black move
        self.status = 1

        # 1 = white, 2 = black, 3 = white king, 4 = black king
        self.board_array = [
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 0, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
        ]

    """
    This drives the whole game
    """

    def main(self):
        pygame.init()

        # draw original board
        Graphics.draw_board(self.board_array)

        # loop while the window is not closed
        while self.status != 0:
            self.event_loop()

        pygame.quit()

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
            Graphics.draw_board(self.board_array)
            self.make_AI_move()
            # TODO: uncomment:
            # self.status = 1
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
            moves = self.get_valid_moves(
                self.selected_piece[0], self.selected_piece[1], self.board_array
            )
            for x1, y1, rm in moves:
                if x1 == x and y1 == y:
                    self.board_array[x][y] = 1
                    for x_rm, y_rm in rm:
                        self.board_array[x_rm][y_rm] = 0
                    self.board_array[self.selected_piece[0]][self.selected_piece[1]] = 0
                    self.selected_piece = (-1, -1)
                    break

            # Make it the AI move next:
            # TODO: uncomment:
            # self.status = 2
        elif self.board_array[x][y] == 1:
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
                    and self.get_valid_moves(i, j, self.board_array) != []
                ):
                    return False

        if self.status == 1:
            print("White has no moves, black wins!")
        else:
            print("Black has no moves, white wins!")
        return True

    """
    Returns a list of all 8x8 board arrays that contain a valid move made
    Should use self.status to see whose move it is, either 1 or 2
    """

    def get_valid_boards(self):
        # TODO
        board_list = []
        for x in range(len(self.board_array)):
            for y in range(len(self.board_array)):
                piece_type = self.board_array[x][y]
                if self.board_array[x][y] == 1:
                    new_x = x - 1
                    left_y = y - 1
                    right_y = y + 1
                    if new_x >= 0 and left_y >= 0:
                        if self.board_array[new_x][left_y] == 0:
                            newboard = self.board_array.copy()
                            newboard[new_x][left_y] = 1
                            newboard[x][y] = 0

                    return
        return board_list

    """
    Gets all possible moves from a position, forcing double/triple jumps
    Returns a list of tuples with the new possible possition (x, y) and [removed piece]
    """

    def get_valid_moves(self, x1, y1, board_array):
        final_moves = []
        single_jump_moves = self.get_valid_moves_no_jumps(x1, y1, board_array)

        for x2, y2, removed_pieces in single_jump_moves:
            final_moves.append((x2, y2, removed_pieces))
            if removed_pieces != []:
                board_array_copy = deepcopy(board_array)
                board_array_copy[x2][y2] = board_array[x1][y1]
                second_moves = self.get_valid_moves(x2, y2, board_array_copy)
                for x3, y3, removed_pieces2 in second_moves:
                    if removed_pieces2 != []:
                        final_moves.append((x3, y3, removed_pieces + removed_pieces2))
        return final_moves

    """
    Gets all possible moves with or without a single jump. 
    Returns a list of tuples with the new possible possition x, y and [removed piece]
    """

    def get_valid_moves_no_jumps(self, x, y, board_array):
        board_array = deepcopy(board_array)
        moves = []
        if board_array[x][y] in (1, 3):  # White Non-king Movement
            up_x = x - 1
            left_y = y - 1
            right_y = y + 1
            if up_x >= 0 and left_y >= 0:  # Left Diagonal Non-Capture Move
                if board_array[up_x][left_y] == 0:
                    moves.append((up_x, left_y, []))
                if board_array[up_x][left_y] in (
                    2,
                    4,
                ):  # Left Diagonal Capture Move
                    if (up_x - 1 >= 0 and left_y - 1 >= 0) and board_array[up_x - 1][
                        left_y - 1
                    ] == 0:
                        moves.append((up_x - 1, left_y - 1, [(up_x, left_y)]))

            if up_x >= 0 and right_y < 8:  # Right Diagonal Non-Capture Move
                if board_array[up_x][right_y] == 0:
                    moves.append((up_x, right_y, []))
                if board_array[up_x][right_y] in (
                    2,
                    4,
                ):  # Right Diagonal Capture Move
                    if (up_x - 1 >= 0 and right_y + 1 < 8) and board_array[up_x - 1][
                        right_y + 1
                    ] == 0:
                        moves.append((up_x - 1, right_y + 1, [(up_x, right_y)]))

        if board_array[x][y] == 3:  # White King Movement
            down_x = x + 1
            left_y = y - 1
            right_y = y + 1
            if down_x >= 0 and left_y >= 0:  # Left Backwards Diagonal Non-Capture Move
                if board_array[down_x][left_y] == 0:
                    moves.append((down_x, left_y, []))
                if board_array[down_x][left_y] in (
                    2,
                    4,
                ):  # Left Backwards Diagonal Capture Move
                    if (down_x - 1 >= 0 and left_y - 1 >= 0) and board_array[
                        down_x - 1
                    ][left_y - 1] == 0:
                        moves.append((down_x - 1, left_y - 1, [(down_x, left_y)]))

            if down_x >= 0 and right_y < 8:  # Right Backwards Diagonal Non-Capture Move
                if board_array[down_x][right_y] == 0:
                    moves.append((down_x, right_y, []))
                if board_array[down_x][right_y] in (
                    2,
                    4,
                ):  # Right Backwards Diagonal Capture Move
                    if (down_x - 1 >= 0 and right_y + 1 < 8) and board_array[
                        down_x - 1
                    ][right_y + 1] == 0:
                        moves.append((down_x - 1, right_y + 1, [(down_x, right_y)]))

        if board_array[x][y] in (2, 4):  # Black Non-king Movement
            down_x = x + 1
            left_y = y - 1
            right_y = y + 1
            if down_x < 8 and left_y >= 0:
                if board_array[down_x][left_y] == 0:
                    moves.append((down_x, left_y, []))  # Left Diagonal Non-Capture Move
                if board_array[down_x][left_y] in (1, 3):
                    if (down_x + 1 < 8 and left_y - 1 >= 0) and board_array[down_x + 1][
                        left_y - 1
                    ] == 0:
                        moves.append(
                            (down_x + 1, left_y - 1, [(down_x, left_y)])
                        )  # Left Diagonal Capture Move
            if down_x < 8 and right_y < 8:
                if board_array[down_x][right_y] == 0:
                    moves.append(
                        (down_x, right_y, [])
                    )  # Right Diagonal Non-Capture Move
                if board_array[down_x][right_y] in (1, 3):
                    if (down_x + 1 < 8 and right_y + 1 < 8) and board_array[down_x + 1][
                        right_y + 1
                    ] == 0:
                        moves.append(
                            (down_x + 1, right_y + 1, [(down_x, right_y)])
                        )  # Right Diagonal Capture Move

        if board_array[x][y] == 4:  # Black King Movement
            up_x = x - 1
            left_y = y - 1
            right_y = y + 1
            if up_x >= 0 and left_y >= 0:
                if board_array[up_x][left_y] == 0:
                    moves.append(
                        (up_x, left_y, [])
                    )  # Left Backwards Diagonal Non-Capture Move
                if board_array[up_x][left_y] in (1, 3):
                    if (up_x - 1 >= 0 and left_y - 1 >= 0) and board_array[up_x - 1][
                        left_y - 1
                    ] == 0:
                        moves.append(
                            (up_x - 1, left_y - 1, [(up_x, left_y)])
                        )  # Left Backwards Diagonal Capture Move
            if up_x >= 0 and right_y < 8:
                if board_array[up_x][right_y] == 0:
                    moves.append(
                        (up_x, right_y, [])
                    )  # Right Backwards Diagonal Non-Capture Move
                if board_array[up_x][right_y] in (1, 3):
                    if (up_x - 1 >= 0 and right_y + 1 < 8) and board_array[up_x - 1][
                        right_y + 1
                    ] == 0:
                        moves.append(
                            (up_x - 1, right_y + 1, [(up_x, right_y)])
                        )  # Right Backwards Diagonal Capture Move

        return moves

    """
    Moves a piece to another location on the board if it is a valid move, 
    and returns nothing if it is not a valid move. Checks if piece is in
    king position. Updates the board.  
    """

    def move_piece(self, old_x, old_y, new_x, new_y):
        if (new_x, new_y) in self.get_valid_moves(old_x, old_y, self.board_array):
            self.board_array[new_x][new_y] = self.board_array[old_x][old_y]
            self.board_array[old_x][old_y] = 0
            self.king_piece(new_x, new_y)

        return

    """
    Removes a piece from the board at location x, y
    """

    def remove_piece(self, x, y):
        self.board_array[x][y] = 0
        return

    def king_piece(self, x, y):
        if (self.board_array[x][y]) == 1 and x == 0:
            self.board_array[x][y] = 3
        elif (self.board_array[x][y]) == 2 and x == 7:
            self.board_array[x][y] = 4
        return

    """
    Makes the AI move using mini-max without pruning
    """

    def make_AI_move(self):
        # TODO
        return

    """
    Makes the AI move using mini-max with pruning
    """

    def make_AI_move_pruning(self):
        # TODO
        return

    """
    Evaluate the board passed in, and returns an integer representing how good
    the board is for the black pieces. A larger integer should be better for black. 
    """

    def evaluate_board(self, board):
        # TODO
        return


# start the game
if __name__ == "__main__":
    game = Game()
    game.main()
