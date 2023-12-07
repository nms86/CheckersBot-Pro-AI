from copy import deepcopy
import pygame


"""
Gets all possible moves from a position, forcing double/triple jumps
Returns a list of tuples with the new possible possition (x, y) and [removed piece]
"""


def get_valid_moves(x1, y1, board_array):
    final_moves = []
    single_jump_moves = get_valid_moves_no_jumps(x1, y1, board_array)

    for x2, y2, removed_pieces in single_jump_moves:
        final_moves.append((x2, y2, removed_pieces))
        if removed_pieces != []:
            board_array_copy = deepcopy(board_array)
            board_array_copy[x2][y2] = board_array[x1][y1]
            second_moves = get_valid_moves(x2, y2, board_array_copy)
            for x3, y3, removed_pieces2 in second_moves:
                if removed_pieces2 != []:
                    final_moves.append((x3, y3, removed_pieces + removed_pieces2))
    return final_moves


"""
Gets all possible moves with or without a single jump. 
Returns a list of tuples with the new possible possition x, y and [removed piece]
"""


def get_valid_moves_no_jumps(x, y, board_array):
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
                if (down_x - 1 >= 0 and left_y - 1 >= 0) and board_array[down_x - 1][
                    left_y - 1
                ] == 0:
                    moves.append((down_x - 1, left_y - 1, [(down_x, left_y)]))

        if down_x >= 0 and right_y < 8:  # Right Backwards Diagonal Non-Capture Move
            if board_array[down_x][right_y] == 0:
                moves.append((down_x, right_y, []))
            if board_array[down_x][right_y] in (
                2,
                4,
            ):  # Right Backwards Diagonal Capture Move
                if (down_x - 1 >= 0 and right_y + 1 < 8) and board_array[down_x - 1][
                    right_y + 1
                ] == 0:
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
                moves.append((down_x, right_y, []))  # Right Diagonal Non-Capture Move
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
Evaluate the board passed in, and returns an integer representing how good
the board is for the black pieces. A larger integer should be better for black. 
"""


def evaluate_board(board):
    return (
        num_pieces(board, 1)
        - num_pieces(board, 2)
        + (num_pieces(board, 3) - num_pieces(board, 4)) * 1.5
    )


def get_piece_locations(board, color):
    locations = []
    colors = (1, 3)
    if color not in colors:
        colors = (2, 4)
    for x in range(8):
        for y in range(8):
            if board[x][y] in colors:
                locations.append((x, y))

    return locations


def king_piece(board, x, y):
    if (board[x][y]) == 1 and x == 0:
        board[x][y] = 3
    elif (board[x][y]) == 2 and x == 7:
        board[x][y] = 4
    return board


"""
Moves a piece to another location on the board if it is a valid move, 
and returns nothing if it is not a valid move. Checks if piece is in
king position. Updates the board.  
"""


def move_piece(board, old_x, old_y, new_x, new_y):
    valid_moves = get_valid_moves(old_x, old_y, board)  # (x, y, [])
    valid_destinations = []

    for x, y, rm in valid_moves:
        valid_destinations.append((x, y))

    if (new_x, new_y) in valid_destinations:
        board[new_x][new_y] = board[old_x][old_y]
        board[old_x][old_y] = 0
        board = king_piece(board, new_x, new_y)

    return board


"""
Removes a piece from the board at location x, y
"""


def remove_piece(board, x, y):
    board[x][y] = 0
    return board


"""
Returns the number of pieces of the color passed in
"""


def num_pieces(board, color):
    count = 0
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == color:
                count += 1
    return count


"""
Given a board, a piece location, a move location, and a capture list, simulates the move 
on a copy of the board and returns it, with captured pieces removed.
"""


def sim_move(x, y, move, board, capture):
    board = move_piece(board, x, y, move[0], move[1])
    if capture:
        for x, y in capture:
            board = remove_piece(board, x, y)
    return board


"""
Given a board and a color, returns a list of all possible moves in the form of
new boards.
"""


def get_all_moves(board, color):  # May be able to replace with get_valid_boards
    moves = []

    for x, y in get_piece_locations(board, color):
        valid_moves = get_valid_moves(x, y, board)
        for x1, y1, capture in valid_moves:
            temp_board = deepcopy(board)
            moves.append(sim_move(x, y, (x1, y1), temp_board, capture))

    return moves


def is_win_or_lose(board):
    if not get_all_moves(board, 1) and not get_all_moves(board, 2):
        return True
    return False


def minimax(board, depth, max_player):
    if depth == 0 or is_win_or_lose(board) == True:
        return evaluate_board(board), board

    best_move = None

    if max_player:
        maxEval = float("-inf")
        for move in get_all_moves(board, 1):
            evaluation = minimax(move, depth - 1, False)[0]
            if maxEval < evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float("inf")
        for move in get_all_moves(board, 2):
            evaluation = minimax(move, depth - 1, True)[0]
            if minEval > evaluation:
                best_move = move

        return minEval, best_move
