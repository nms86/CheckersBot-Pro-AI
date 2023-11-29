import pygame
from board_graphics import Graphics


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
        # AI MOVE:
        if self.status == 2:
            Graphics.draw_board(self.board_array)
            self.make_AI_move()
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
            self.board_array[x][y] = 1
            self.board_array[self.selected_piece[0]][self.selected_piece[1]] = 0
            self.selected_piece = (-1, -1)
        elif self.board_array[x][y] == 1:
            self.selected_piece = (x, y)

    """
    Returns the result of the game if it is over, or return nothing if not
    Uses self.status to see whose turn it is, and to see if there are any moves left
    """

    def is_win_or_lose(self):
        # TODO
        # should use the get_valid_moves function
        return

    """
    Returns a list of all 8x8 board arrays that contain a valid move made
    Should use self.status to see whose move it is, either 1 or 2
    """

    def get_valid_moves(self):
        # TODO
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
